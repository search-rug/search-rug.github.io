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
            'link': self.link,
        }


class RSSContributionScraper():
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
            link = item[0].text

            if re.match(self.exclude_regex, title):
                print(f"RegEx match found. Skipping: {title}")
                continue

            contributions.append(Contribution(title, link))

        return contributions


def save_contributions(contributions, collection_name):
    """Saves contributions to '_data' directory of website."""
    data_dir = Path("_data")
    if not data_dir.exists():
        raise FileNotFoundError("Data dir '_data' does not exist.")

    filepath = data_dir.joinpath(f"{collection_name}.json")
    with open(filepath, "w") as file:
        file.write(contributions_to_json(contributions, pretty=True))


def contributions_to_json(contributions, pretty=False):
    """Convert a list of contributions to JSON."""
    indents = 4 if pretty else None
    return json.dumps([contrib.to_dict() for contrib in contributions], indent=indents)


def main():
    filepath = '_data/contributions.json'
    rss_link = "https://research.rug.nl/en/organisations/software-engineering/datasets/?format=rss"

    scraper = RSSContributionScraper(rss_link)
    contribs = scraper.get_contributions()

    # write file
    with open(filepath, "w") as file:
        file.write(contributions_to_json(contribs, pretty=True))


if __name__ == "__main__":
    main()
