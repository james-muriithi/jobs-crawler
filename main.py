import time
import schedule

from brightermondays.main import run as brighter_mondays
from ihub.main import run as ihub
from myjobmag.main import run as myjobmag
from fuzu.main import run as fuzu

schedule.every(3).hours.do(ihub)
schedule.every(3).hours.do(brighter_mondays)
schedule.every(3).hours.do(myjobmag)
schedule.every(3).hours.do(fuzu)

if __name__ == "__main__":
    brighter_mondays()
    time.sleep(1)
    ihub()
    time.sleep(1)
    myjobmag()
    time.sleep(1)
    fuzu()
    time.sleep(1)
    while True:
        schedule.run_pending()
        time.sleep(1)
