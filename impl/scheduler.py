import schedule
import time
from crud_playground.utils.files import FromCSV


def job(file_path):
    print("Start Parsing CSV")
    FromCSV(file_path)


file_path = "~/file.csv"
schedule.every().day.at("10:30").do(job(file_path))

while True:
    schedule.run_pending()
    time.sleep(1)
