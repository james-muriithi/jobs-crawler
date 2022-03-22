import requests
from bs4 import BeautifulSoup

from app.parser import Parser


class SiteParser(Parser):
    def extract_company(self, div):

        try:
            return (div.find('a', attrs={'class', 'job-card-container__company-name'}).text)
        except:
            return ''

    def extract_salary(self, div):
        try:
            return (div.find('div', attrs={'class', 'search-result__job-salary'}).text.strip())
        except:
            return ''

    def extract_job_type(self, div):
        try:
            return (div.find('span', attrs={'class', 'search-result__job-type'}).text.strip())
        except:
            return ''

    def extract_work_type(self, div):
        try:
            return (div.find('span', attrs={'class', 'job-card-container__metadata-item--workplace-type'}).text.strip())
        except:
            return ''

    def extract_location(self, div):
        try:
            return (div.find('div', attrs={'class', 'job-card-container__metadata-wrapper'})
                    .find('div', attrs={"class", "job-card-container__metadata-item"}).text)
        except:
            return ''

    def extract_job_title(self, div):
        try:
            company = div.find(
                name="a", attrs={"class": "job-card-list__title"})
            return (company.text)
        except:
            return ''

    def extract_summary(self, url):
        try:
            text = self.extract_fulltext(url)
            sentences = text.splitlines()
            return ' '.join(sentences[0:2])
        except Exception as e:
            self.write_logs(str(e))
            return ''
        return ''

    def extract_link(self, div):
        myurl = 'https://linkedin.com/jobs/view/'
        try:
            job_id = div.attrs['data-id']
            return (myurl+job_id)
        except:
            return ''

    # extract date of job when it was posted
    def extract_date(self, div):
        try:
            return (div.find('div', attrs={'class', 'job-result-card__contents'})
                    .find('div', attrs={'class', 'job-result-card__meta'}).find('time').attrs['datetime'])
        except:
            return ''

    def extract_fulltext(self, url):
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "lxml", from_encoding='utf-8')
            div = soup.find('section', attrs={
                'class': 'show-more-less-html'}).find('div', attrs={
                    'class': 'show-more-less-html__markup'})
            return '\n'.join(div.stripped_strings)
        except Exception as e:
            self.write_logs(str(e))
            return ''
        return ''
