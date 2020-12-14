# Web-scraper to alert for ski resort parking spots

from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import smtplib

url = "https://www.parkwhiz.com/mt-bachelor-ski-resort-parking-2/"

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "lxml")
scripts = soup.find_all("script", type="application/ld+json")

# Desired Dates from ParkWhiz Website/App
desired_date = ["Dec 18 2020 Daily Parking", "Dec 19 2020 Daily Parking", "Dec 17 2020 Daily Parking",
                "Dec 22 2020 Daily Parking"]
all_data = []
date_available = False
avail_data = []

num = 0
for script in scripts:
    all_data += script.contents
    if 'offers' in all_data[num]:
        jsonObj = json.loads(all_data[num])
        if jsonObj['name'] in desired_date:
            if jsonObj['offers']['availability'] == "http://schema.org/InStock":
                print(jsonObj['name'] + "  (PARKING AVAILABLE)  " + jsonObj['offers']['availability'] + " -> " +
                      jsonObj['url'])
                avail_data += [jsonObj['name'] + "  (PARKING AVAILABLE)  " + jsonObj['offers']['availability']
                               + " -> " + jsonObj['url']]
                date_available = True
            else:
                print(jsonObj['name'] + "  (No Parking)  " + jsonObj['offers']['availability'])
    num += 1

email_string = " "

if date_available:
    conn = smtplib.SMTP('smtp.gmail.com', 587)  # smtp address and port
    conn.ehlo()  # call this to start the connection
    conn.starttls()  # starts tls encryption. When we send our password it will be encrypted.
    conn.login('from@gmail.com', 'pass')
    conn.sendmail('from@gmail.com', 'to@gmail.com', 'Subject: RESERVE PARKING NOW!\n\n'
                                                                               'Attention!\n\nOne of the desired days '
                                                                               'is available at Bachelor:\n\n'
                                                                               '%s' % email_string.join(avail_data))
    conn.quit()
else:
    print('Not Available')


