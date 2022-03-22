import time

from brightermondays.main import run as brighter_mondays
from ihub.main import run as ihub
from myjobmag.main import run as myjobmag
from fuzu.main import run as fuzu


if __name__ == "__main__":
    brighter_mondays()
    time.sleep(1)
    ihub()
    time.sleep(1)
    myjobmag()
    time.sleep(1)
    fuzu()
