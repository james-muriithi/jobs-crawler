import os
from datetime import datetime
import time

from .site_parser import SiteParser
from app.crawler import Crawler


class SiteCrawler(Crawler):
    # give the filename the name of the current folder
    folder = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'jobs')

    file_name = os.path.join(folder, 'linkedin-' +
                             datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+'.csv')

    site_parser = SiteParser()

    def __init__(self):
        super().__init__(self.site_parser)


def run():
    pages = [
        'https://www.linkedin.com/jobs/search?keywords=Developer&location=Nairobi%2C%2BKenya&geoId=101339379&trk=public_jobs_jobs-search-bar_search-submit&f_TP=1%2C2&redirect=false&position=1&pageNum=0',
        # 'https://www.linkedin.com/jobs/search?keywords=software&location=Nairobi%2C%2BKenya&geoId=101339379&trk=public_jobs_jobs-search-bar_search-submit&f_TP=1%2C2&redirect=false&position=1&pageNum=0',
        # 'https://www.linkedin.com/jobs/search?keywords=Software%2BEngineer&location=Nairobi%2C%2BKenya&geoId=101339379&trk=public_jobs_jobs-search-bar_search-submit&f_TP=1%2C2&redirect=false&position=1&pageNum=0',
        # 'https://www.linkedin.com/jobs/search?keywords=Technology&location=Nairobi%2C%2BKenya&geoId=101339379&trk=public_jobs_jobs-search-bar_search-submit&f_TP=1%2C2&redirect=false&position=1&pageNum=0'
    ]

    crawler = SiteCrawler()

    for domain in pages:
        crawler.scrap_jobs(domain, jobElement="li",
                           jobElementAttrs={"class": "jobs-search-results__list-item"})
        time.sleep(10)


if __name__ == "__main__":
    run()
