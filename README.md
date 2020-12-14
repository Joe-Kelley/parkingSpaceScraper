# parkingSpaceScraper.py
Parking Space Web-Scraper for Skiing/Snowboarding for Resorts using https://www.parkwhiz.com/



## Dependencies 

```
pip install bs4
```

```
pip install smtplib
```



## Instructions

To edit for your application:

Change URL to desired URL from ParkWhiz

**Line 8:** (Edit) 

```python
url = "https://www.parkwhiz.com/mt-bachelor-ski-resort-parking-2/"
```



**Line 13:**

You can find every date available for a parking location using soup and using *soup.find_all* to collect all dates offered:

```python
scripts = soup.find_all("script", type="application/ld+json")
```



For understanding the return values see:

https://schema.org/Event

https://schema.org/offers

https://schema.org/AggregateOffer

https://schema.org/availability



We want to cross reference with the 'name'  of the item.

**Line 16:** (Edit)

```python
desired_date = ["Dec 18 2020 Daily Parking", "Dec 22 2020 Daily Parking"]
```



Now we check that the name item is available:

```python
all_data = []
for script in scripts:
    all_data += script.contents
    if 'offers' in all_data[num]:
        jsonObj = json.loads(all_data[num])
        if jsonObj['name'] in desired_date:
            if jsonObj['offers']['availability'] == "http://schema.org/InStock":
```



**Lines 44-45:** (Edit)

See: https://stackabuse.com/how-to-send-emails-with-gmail-using-python/

Configure for your email.

```python
conn = smtplib.SMTP('smtp.gmail.com', 587)  # smtp address and port
conn.ehlo()  # call this to start the connection
conn.starttls()  # starts tls encryption. When we send our password it will be encrypted.
conn.login('from@gmail.com', 'pass')
conn.sendmail('from@gmail.com', 'to@gmail.com', 'Subject: Attention! \n\n'                                                                           'Attention!\n\nOne of the desired days is available:\n\n'
                                         '%s' % email_string.join(avail_data))
```


# bachelorParking.bat

Line 1: (Edit)

```
@python.exe "C:\Users\<User>\<yourFilePath>\parkingScraper.py" %*
```





## For Looping the batch file on Windows see:

https://stackoverflow.com/questions/4249542/run-a-task-every-x-minutes-with-windows-task-scheduler

