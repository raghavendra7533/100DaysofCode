import smtplib
from datetime import datetime
import pandas
import random


my_email = "raghavpromo7533@gmail.com"
password = "vxlvkqdujosmxdbj"

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
