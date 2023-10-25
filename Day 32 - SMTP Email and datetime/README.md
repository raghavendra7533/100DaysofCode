# Day 32 - Send Email & Manage Dates
## SMTPlib
SMTP abbreviated as Simple Mail Transfer Protocol is an internet standard protocol for sending and receiving emails. SMTP is a part of TCP/IP protocol application level. 

>[!note]- SMTP has two types
>1. End to End method
>2. Store and forward method

## Using SMTPlib in Python
1. Establish connection using `connection = smtplib.SMTP(smtp.gmail.com)` and then initialise the `Transfer Layer Security` using `connection.starttls()`  

>[!note]- You can also use `with open` method

2. Pass the login credentials using `connection.login(user=my_email, password=password)`
3. Then send mail using `connection.sendmail(from_adr=my_mail, to_addr=to_address`, msg="Hello")
4. To add a subject line use `msg="Subject: Hello world\n\nThis is the body of the email"` 

## Datetime
- Datetime library is used to fetch enable python to execute Date and Time related tasks.

## Challenge 1 : Send Motivational Quotes
1. Import smtplib, datetime and random libraries
2. Fetch the current datetime using `now = dt.datetime.now()`
3. Filter the weekday out using `weekday = now.weekday()`
4. Define the required constants for the smtp lib
5. Make an if loop to check if the weekday is Monday, and open the `quotes.txt` file and readlines.
6. Use the random library to choose one quote.
7. execute the smtp sendmail with the randomly generated quote in the body

### Code
```py
"""Challenge 1: Send random quotes using smtplib"""  
  
import smtplib  
import datetime as dt  
import random  
  
now = dt.datetime.now()  
weekday = now.weekday()  
my_email = ""  
password = ""  
  
if weekday == 2:  
    with open("quotes.txt") as quote_file:  
        all_quotes = quote_file.readlines()  
        quote = random.choice(all_quotes)  
  
    with smtplib.SMTP("smtp.gmail.com") as connection:  
        connection.starttls()  
        connection.login(user=my_email, password=password)  
        connection.sendmail(  
            from_addr=my_email,  
            to_addrs="raghavendra8076@gmail.com",  
            msg=f"Subject: Motivation\n\n{quote}"  
        )
```

## Birthday Wisher Project

1. Import `smtplib`, `datetime`, `pandas` and `random`
2. Define `my_email` and `password`
3. Fetch today's date and time using `datetime` library
4. Create a tuple with today's date and month
5. Use the pandas library to read the birthdays csv file
6. Create a dictionary with the month and date data in the birthdays csv file with the tuple of the date and month being the key and the data_row being the dictionary
7. Check if there exists a birthday in the dictionary with todays date and month
	1. If true, send the mail using smtp

### Code
```py
import smtplib  
from datetime import datetime  
import pandas  
import random  
  
  
my_email = ""  
password = ""  
  
today = datetime.now()  
today_tuple = (today.month, today.day)  
  
data = pandas.read_csv("birthdays.csv")  
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}  
  
if today_tuple in birthdays_dict:  
    birthday_person = birthdays_dict[today_tuple]  
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"  
    with open(file_path) as letter:  
        content = letter.read()  
        new_content = content.replace("[NAME]", birthday_person["name"])  
  
    with smtplib.SMTP("smtp.gmail.com") as connection:  
        connection.starttls()  
        connection.login(user=my_email, password=password)  
        connection.sendmail(  
            from_addr=my_email,  
            to_addrs="raghavendra8076@gmail.com",  
            msg=f"Subject: Happy Birthday! {birthday_person['name']}\n\n{new_content}"  
        )
```