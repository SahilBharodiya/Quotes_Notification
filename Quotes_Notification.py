import time
from plyer import notification
import pandas as pd
from random import randint

x = randint(0,1665)
d = pd.read_csv('quotes.csv')

if __name__ == "__main__":
    while True:
        notification.notify(title=d['Author'][x],
                            message=d['Quote'][x],
                            app_icon="E:\python_projects\projects\logo.ico",
                            timeout=15)
        time.sleep(60*60)
