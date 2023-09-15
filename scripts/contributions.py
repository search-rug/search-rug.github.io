import urllib.request
import json
from datetime import datetime
from xml.etree import ElementTree as ET
from pathlib import Path
import re


class Contribution:
    """Represents a contribution loaded from the RSS feed."""

    def __init__(self, title, link, description):
        self.title = title
        self.link = link
        self.description = description

    def to_dict(self):
        return {
            'title': self.title,
            'url': self.link,
            'description': self.description,
        }


class RSSContributionScraper():
    """Scrapes contributions from an RSS source."""

    def __init__(self, rss_link, exclude_regex=None):
        self.rss_link = rss_link
        if exclude_regex is None:
            self.exclude_regex = []
        elif not isinstance(exclude_regex, list):
            self.exclude_regex = [exclude_regex]
        else:
            self.exclude_regex = exclude_regex

    @staticmethod
    def _getPubDate(item):
        """Extracts publication date from RSS item."""
        pubdate = item.find("pubDate")
        if pubdate is None:
            return None
        return datetime.strptime(pubdate.text, "%a, %d %b %Y %H:%M:%S %Z")
    
    @staticmethod
    def _cleanDescription(description):
        """Extracts description from RSS item."""
        if description is None:
            return None
        # remove type tag
        description = re.sub(r'<p class="type">.*?</p>', '', description)
        # remove empty link tags
        description = re.sub(re.compile(r'<a[^>]*href="#"[^>]*>(.*?)</a>', re.IGNORECASE), r'\1', description)
        # remove dataset link
        description = re.sub(r'<p class="links-doi">.*?</p>', '', description)
        # for dates, keep only the year
        description = re.sub(r'(<span class="date">)(\d{0,2}-)?(\w{3}-)?(\d{4})(</span>)', r'\1\4\5', description)
        
        return description

    def get_contributions(self):
        """Extracts RSS contibution entries from RSS feed."""
        response = urllib.request.urlopen(self.rss_link)
        rss_doc = ET.fromstring(response.read())
        channels = rss_doc.findall("channel")
        items = sorted(channels[0].findall("item"), key=RSSContributionScraper._getPubDate, reverse=True)
        
        contributions = []

        for item in items:
            title = item.find("title").text
            link = item.find("link").text
            description = RSSContributionScraper._cleanDescription(item.find("description").text)
            
            if any([re.match(regex, title) for regex in self.exclude_regex]):
                print(f"excluded: {title}")
                continue

            contributions.append(Contribution(title, link, description))

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
            "exclude_regex": [r".*SC@RUG.*"]
        }
    ]

    root_dir = Path(__file__).parent.parent.absolute()
    data_dir = root_dir.joinpath("_data")

    if not data_dir.exists():
        raise FileNotFoundError(f"Could not find data dir: {data_dir}")

    main(scrape_targets, data_dir)
