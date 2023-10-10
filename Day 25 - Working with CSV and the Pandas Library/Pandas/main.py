# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

print(data["temp"].mean())
"""This method gives the mean of the Series"""

print(data["temp"].max())
"""This method gives the max of the Series"""

print(data[data.day == "Monday"])
"""This method gets the data from the row of 'day' where the value is 'Monday'"""

"""This method first gets the max temp in the data and returns the row where the temp is the max"""
print(data[data.temp == data.temp.max()])

"""How to get the data in the Rows"""
print(data[data.day == "Monday"])
print(type(data[data.day == "Monday"]))
print(data[data.day == "Monday"].temp[0])

"""How to perform Mathematical operations on data from the Pandas"""
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9 / 5 + 32
print(f"Temp in F: {monday_temp_F}")

"""How to create a dataframe from scratch"""
data_dict = {
    "students": ["Amy", "James", "Raghav"],
    "scores": [76, 56, 65],
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
# print(data)
