import urllib.request
import json
from urllib import response
from xml.etree import ElementTree as ET
import logging
import sys


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
  def __init__(self, rss_link):
    self.rss_link = rss_link

  def get_contributions(self):
    """Extracts RSS contibution entries from RSS feed."""
    response = urllib.request.urlopen(self.rss_link)
    rss_doc = ET.fromstring(response.read())
    channels = rss_doc.findall("channel")
    return [Contribution(item[0].text, item[1].text) for item in channels[0] if item.tag == "item"]


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
