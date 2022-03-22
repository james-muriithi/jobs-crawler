import requests
from bs4 import BeautifulSoup

from app.parser import Parser


class SiteParser(Parser):
    def extract_company(self, div):
        try:
            job_title = self.extract_job_title(div)
            return job_title.split(' at ')[1].strip()
        except:
            return ''

    def extract_salary(self, div):
        return 'Ksh Confidential'

    def extract_job_type(self, div):
        return ''

    def extract_location(self, div):
        try:
            return (div.find('div', attrs={'class', 'job-list-content'})
                    .find('div', attrs={'class', 'meta-tag'}).findAll('span')[1].text)
        except:
            return 'Nairobi'

    def extract_job_title(self, div):
        try:
            return (div.find('li', attrs={'class', 'mag-b'}).find('h2').find('a').text)
        except:
            return ''

    def extract_summary(self, div):
        try:
            return (div.find('li', attrs={'class', 'job-desc'}).text)
        except Exception as e:
            self.write_logs(str(e))
            return ''

    def extract_link(self, div):
        myurl = 'https://www.myjobmag.co.ke'
        try:
            title = div.find(
                'li', attrs={'class', 'mag-b'}).find('h2').find('a')
            return (myurl+title.get('href'))
        except:
            return ''

    # extract date of job when it was posted
    def extract_date(self, div):
        try:
            return (div.find('li', attrs={'class', 'job-item'})
                    .find('li', attrs={'id', 'job-date'}).text)
        except:
            return ''

    def extract_fulltext(self, url):
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "lxml", from_encoding='utf-8')
            div = soup.find('div', attrs={
                'class': 'job-details'})
            return '\n'.join(div.stripped_strings)
        except:
            return ''
