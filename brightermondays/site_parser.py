import requests
from bs4 import BeautifulSoup

from app.parser import Parser


class SiteParser(Parser):
    def extract_company(self, div):

        try:
            return (div.find('div', attrs={'class', 'search-result__job-meta'}).text)
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

    def extract_location(self, div):
        try:
            return (div.find('div', attrs={'class', 'relative h-auto flex-col md:flex-row items-start md:items-center px-5'})
                    .find('div', attrs={"class", "inline-block mr-2"}).text)
        except:
            return ''

    def extract_job_title(self, div):
        try:
            company = div.find(name="h3")
            return (company.text)
        except:
            return ''

    def extract_summary(self, url):
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "lxml", from_encoding='utf-8')
            summary = soup.find('div', attrs={
                                'class': 'job__details__user-edit wrapper--inline-block float--left'})
            summary.h3.decompose()
            return '\n'.join(summary.stripped_strings)
        except Exception as e:
            self.write_logs(str(e))
            return ''
        return ''

    def extract_link(self, div):
        try:
            company = div.find(
                name="a", attrs={"class", "break-words metrics-apply-now"})
            return (company.get('href'))
        except:
            return ''

    # extract date of job when it was posted
    def extract_date(self, div):
        try:
            company = div.find(
                name="div", attrs={"class", "flex items-start py-2 px-5 mt-2 border-t border-gray-300"}).find(name="span", attrs={"class", "ml-auto"})
            if company:
                return (company.text + " ago")
        except:
            return ''

    def extract_fulltext(self, url):
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "lxml", from_encoding='utf-8')
            divs = soup.findAll('div', attrs={
                                'class': 'job__details__user-edit wrapper--inline-block float--left'})
            return '\n'.join(divs[1].stripped_strings)
        except:
            return ''
