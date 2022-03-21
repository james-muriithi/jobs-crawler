from bs4 import BeautifulSoup

from abc import ABC, abstractmethod

class Parser(ABC):
    # get soup object
    def get_soup(text):
        return BeautifulSoup(text, "lxml", from_encoding='utf-8')


    # extract company
    @abstractmethod
    def extract_company(div): 
        pass


    # extract job salary
    @abstractmethod
    def extract_salary(div): 
        pass
        


    # extract job location
    @abstractmethod
    def extract_location(div):
        pass


    # extract job title
    @abstractmethod
    def extract_job_title(div):
        pass


    # extract jd summary 
    @abstractmethod
    def extract_summary(url): 
        pass
    

    # extract link of job description 
    @abstractmethod
    def extract_link(div): 
        pass


    # extract date of job when it was posted 
    @abstractmethod
    def extract_date(div):
        pass


    # extract full job description from link
    @abstractmethod
    def extract_fulltext(url):
        pass


    # write logs to file
    def write_logs(text):
        # print(text + '\n')
        f = open('log.txt','a')
        f.write(text + '\n')  
        f.close()