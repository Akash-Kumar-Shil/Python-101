from time import sleep
from datetime import datetime

def get_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
    current_date = now.strftime("%Y-%m-%d")
    print(f"📅 Date: {current_date} | ⏰ Time: {current_time}", end="\r")

while True:
    get_time()
    sleep(1)
