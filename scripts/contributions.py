import urllib.request
import json
from xml.etree import ElementTree as ET
from pathlib import Path
import re


class Contribution:
    """Represents a contribution loaded from the RSS feed."""

    def __init__(self, title, link):
        self.title = title
        self.link = link

    def to_dict(self):
        return {
            'title': self.title,
            'url': self.link,
        }


class RSSContributionScraper():
    """Scrapes contributions from an RSS source."""

    def __init__(self, rss_link, exclude_regex=None):
        self.rss_link = rss_link
        self.exclude_regex = exclude_regex

    def get_contributions(self):
        """Extracts RSS contibution entries from RSS feed."""
        response = urllib.request.urlopen(self.rss_link)
        rss_doc = ET.fromstring(response.read())
        channels = rss_doc.findall("channel")
        contributions = []

        for item in channels[0]:
            if item.tag != "item":
                continue

            title = item[0].text
            link = item[1].text

            if self.exclude_regex is not None and re.match(self.exclude_regex, title):
                print(f"excluded: {title}")
                continue

            contributions.append(Contribution(title, link))

        return contributions


def save_contributions(directory, contributions, collection_name):
    """Saves contributions to '_data' directory of website."""
    filepath = directory.joinpath(f"{collection_name}.json")
    with open(filepath, "w") as file:
        file.write(contributions_to_json(contributions, pretty=True))


def contributions_to_json(contributions, pretty=False):
    """Convert a list of contributions to JSON."""
    indents = 4 if pretty else None
    return json.dumps([contrib.to_dict() for contrib in contributions], indent=indents)


def main(targets, data_dir):
    """Scrapes and saves all contribution targets.
        targets: List of dict object with `name`, `rss_link` and `exclude_regex`
        data_dir: Path object with website's data directory which is typically `_data` for a jekyll site.
    """

    for target in targets:
        print(f"Scraping {target['name']} ... ")
        scraper = RSSContributionScraper(
            target["rss_link"], target["exclude_regex"])
        contributions = scraper.get_contributions()
        save_contributions(data_dir, contributions, target["name"])


if __name__ == "__main__":
    """Define contribution targets.
    name:           Name of contributions. Will be used as filename with a `.json` suffix.
    rss_link:       Url of a RSS file of contributions from `research.rug.nl`.
    exclude_regex:  RegEx excluding contributions based on its title.
    """
    scrape_targets = [
        {
            "name": "datasets",
            "rss_link": "https://research.rug.nl/en/organisations/software-engineering/datasets/?format=rss",
            "exclude_regex": None
        },
        {
            "name": "publications",
            "rss_link": "https://research.rug.nl/en/organisations/software-engineering/publications/?format=rss",
            "exclude_regex": None
        }
    ]

    root_dir = Path(__file__).parent.parent.absolute()
    data_dir = root_dir.joinpath("_data")

    if not data_dir.exists():
        raise FileNotFoundError(f"Could not find data dir: {data_dir}")

    main(scrape_targets, data_dir)
