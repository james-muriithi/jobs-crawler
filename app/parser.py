from bs4 import BeautifulSoup

from abc import ABC, abstractmethod

class Parser(ABC):
    # get soup object
    def get_soup(self, text):
        return BeautifulSoup(text, "lxml", from_encoding='utf-8')


    # extract company
    @abstractmethod
    def extract_company(self, div): 
        pass


    # extract job salary
    @abstractmethod
    def extract_salary(self, div): 
        pass
        
    @abstractmethod
    def extract_job_type(self, div):
        pass

    # extract job location
    @abstractmethod
    def extract_location(self, div):
        pass


    # extract job title
    @abstractmethod
    def extract_job_title(self, div):
        pass


    # extract jd summary 
    @abstractmethod
    def extract_summary(self, url): 
        pass
    

    # extract link of job description 
    @abstractmethod
    def extract_link(self, div): 
        pass


    # extract date of job when it was posted 
    @abstractmethod
    def extract_date(self, div):
        pass


    # extract full job description from link
    @abstractmethod
    def extract_fulltext(self, url):
        pass


    # write logs to file
    def write_logs(self, text):
        # print(text + '\n')
        f = open('log.txt','a')
        f.write(text + '\n')  
        f.close()