import requests
import time

from app.parser import Parser


class SiteParser(Parser):
    def extract_company(self, div):
        try:
            return (div.find('div', attrs={'class', 'card-header'})
                    .find('p', attrs={"class": "b2c-text"}).text.strip())
        except:
            return ''

    def extract_salary(self, div):
        return 'Ksh Confidential'

    def extract_job_type(self, div):
        return ''

    def extract_location(self, div):
        try:
            return (div.find('div', attrs={'class', 'card-content'})
                    .find('p', attrs={'class', 'b2c-text'}).text)
        except:
            return 'Nairobi'

    def extract_job_title(self, div):
        try:
            return (div.find('div', attrs={'class', 'card-content'})
                    .find('h6', attrs={"class": "title"}).text)
        except:
            return ''

    def extract_summary(self, div):
        return ''

    def extract_link(self, div):
        myurl = 'https://www.fuzu.com'
        try:
            return (myurl+div.get('href'))
        except:
            return ''

    # extract date of job when it was posted
    def extract_date(self, div):
        try:
            url = self.extract_link(div)
            page = requests.get(url)
            time.sleep(1)
            soup = self.get_soup(page.text)
            div = soup.find('p', attrs={
                'class': 'published'})

            return div.text.strip()
        except Exception as e:
            print(e)
            return ''

    def extract_fulltext(self, url):
        try:
            page = requests.get(url)
            soup = self.get_soup(page.text)

            div = soup.find('div', attrs={
                'class': 'view-main'}).find("div", attrs={"class": "styled__TabPanel-sc-1s1q1aa-4"})

            return '\n'.join(div.stripped_strings)
        except:
            return ''
