from abc import ABC, abstractmethod, abstractproperty
from app.parser import Parser
import requests
import pandas as pd
import time
from datetime import datetime
import os
from utils import postJob


class Crawler(ABC):
    # give the filename the name of the current folder
    folder = os.path.join(os.getcwd(), 'jobs')

    file_name = os.path.join(folder, 'brightermondays-' +
                             datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+'.csv')

    @abstractproperty
    def domain(self):
        pass

    # dataframe
    df = pd.DataFrame(columns=['title', 'location', 'company', 'summary',
                      'salary', 'link', 'post_date', 'full_text', 'fetch_date'])

    """
    
    """

    def __init__(self, parser: Parser):
        self.parser = parser

    @abstractmethod
    def scrap_jobs(self, jobElement: str, jobElementAttrs: object):
        print('scrapping jobs from ' + self.domain + '....')

        # get dom
        page = requests.get(self.domain)

        # ensuring at least 1 second between page grabs
        time.sleep(1)

        # fetch data
        soup = self.parser.get_soup(page.text)

        divs = soup.find_all(name=jobElement, attrs=jobElementAttrs)

        # for all jobs on a page
        for div in divs:
            # specifying row num for index of job posting in dataframe
            num = (len(self.df) + 1)
            link = self.parser.extract_link(div)

            # job data after parsing
            job_post = []

            # grabbing job title
            job_post.append(self.parser.extract_job_title(div))

            # grabbing location name
            job_post.append(self.parser.extract_location(div))

            # grabbing company
            job_post.append(self.parser.extract_company(div))

            # grabbing summary text
            job_post.append(self.parser.extract_summary(link))

            # grabbing salary
            job_post.append(self.parser.extract_salary(div))

            # grabbing link
            job_post.append(link)

            # grabbing date
            job_post.append(self.parser.extract_date(div))

            # grabbing full_text
            job_post.append(self.parser.extract_fulltext(link))

            # current time
            job_post.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            # appending list of job post info to dataframe at index num
            self.df.loc[num] = job_post

            postJob(self.df.loc[num].to_dict())

        self.saveCSV()

    def saveCSV(self):
        # saving df as a local csv file
        if not os.path.isdir(self.folder):
            os.makedirs(self.folder)

        self.df.to_csv(self.file_name, encoding='utf-8')
