# import smtplib
#
# my_email = "raghavpromo7533@gmail.com"
# password = "vxlvkqdujosmxdbj"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="raghavendra8076@gmail.com",
#         msg="Subject: test\n\nHello smtplib"
#     )
#
#
#
# import datetime as dt
#
#
# now = dt.datetime.now()
# year = now.year
# date = now.day
# month = now.month
# hour = now.hour
# day = now.weekday()
# minutes = now.minute
#
# date_of_birth = dt.datetime(year=2003, day=24, month=10)
#
# print(date_of_birth)
#
# print(f"{day}, {date}-{month}-{year}, {hour}:{minutes}")


"""Challenge 1: Send random quotes using smtplib"""

import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
my_email = "raghavpromo7533@gmail.com"
password = "vxlvkqdujosmxdbj"

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
