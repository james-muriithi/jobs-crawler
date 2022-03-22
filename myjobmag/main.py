import os
from datetime import datetime

from .site_parser import SiteParser
from app.crawler import Crawler


class SiteCrawler(Crawler):
    # give the filename the name of the current folder
    folder = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'jobs')

    file_name = os.path.join(folder, 'myjobmag-' +
                             datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+'.csv')

    site_parser = SiteParser()

    def __init__(self):
        super().__init__(self.site_parser)


def run():
    domain = 'https://www.myjobmag.co.ke/jobs-by-field/information-technology'
    crawler = SiteCrawler()

    crawler.scrap_jobs(domain, jobElement="li",
                       jobElementAttrs={"class": "job-list-li"}, summaryInSamePage=True)


if __name__ == "__main__":
    run()
