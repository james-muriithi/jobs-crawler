import os
from datetime import datetime

from .site_parser import SiteParser
from app.crawler import Crawler


class SiteCrawler(Crawler):
    # give the filename the name of the current folder
    folder = os.path.join(os.getcwd(), 'jobs')

    file_name = os.path.join(folder, 'brightermondays-' +
                             datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+'.csv')

    site_parser = SiteParser()

    def __init__(self):
        super().__init__(self.site_parser)


def run():
    domain = 'https://www.brightermonday.co.ke/jobs/it-software'
    crawler = SiteCrawler()

    crawler.scrap_jobs(domain, jobElement="article",
                       jobElementAttrs={"class": "search-result"})


if __name__ == "__main__":
    run()
