import requests
from bs4 import BeautifulSoup

from app.parser import Parser


class SiteParser(Parser):
    def extract_company(self, div):
        try:
            return (div.find('div', attrs={'class', 'item-data'}).find('div', attrs={'class', 'job-company'}).find('a').text)
        except:
            return ''

    def extract_salary(self, div):
        return 'Ksh Confidential'

    def extract_job_type(self, div):
        return ''

    def extract_location(self, div):
        try:
            return (div.find('div', attrs={'class', 'item-data'})
                    .find('div', attrs={'class', 'job-company'})
                    .find('div', attrs={'class', 'job-location'}).text)
        except:
            return ''

    def extract_job_title(self, div):
        try:
            return (div.find('div', attrs={'class', 'item-data'}).find('h3').find('a').text)
        except:
            return ''

    def extract_summary(self, div):
        try:
            return (div.find('div', attrs={'class', 'item-data'}).find('div', attrs={'class', 'post-description'})
                    .find('a').text)
        except Exception as e:
            self.write_logs(str(e))
            return ''

    def extract_link(self, div):
        myurl = 'https://ihub.co.ke'
        try:
            title = div.find(
                'div', attrs={'class', 'item-data'}).find('h3').find('a')
            return (myurl+title.get('href'))
        except:
            return ''

    # extract date of job when it was posted
    def extract_date(self, div):
        try:
            return (div.find('div', attrs={'class', 'item-data'})
                    .find('div', attrs={'class', 'job-links'})
                    .find('div', attrs={'class', 'job-time'}).text)
        except:
            return ''

    def extract_fulltext(self, url):
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "lxml", from_encoding='utf-8')
            div = soup.find('div', attrs={
                'class': 'job-content'}).find('div', attrs={'class', 'vacancy-description'})
            return '\n'.join(div.stripped_strings)
        except:
            return ''
