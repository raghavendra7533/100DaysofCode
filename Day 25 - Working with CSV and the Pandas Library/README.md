## Reading a `.csv` file
If we need to read a .csv file we have to import the csv library.
```py
import csv  
  
with open("weather_data.csv") as data_file:  
    data = csv.reader(data_file)  
    temperatures = []  
    for row in data:  
        if row[1] != "temp":  
            temperatures.append(int(row[1]))  
    print(temperatures)
```

Extracting only the Temperatures from the csv file

>[!success]- Output
>[12, 14, 15, 14, 21, 22, 24]

## Installing Pandas Library
Install the pandas library in PyCharm

## Using the Pandas
### Executing [[#Reading a `.csv` file]] using Pandas
Filtering out a column using pandas is much more easier than manually writing out code that ignores the heading of each column.

The same code that filter outs only the temperatures when written out using pandas will be
```py
import pandas  
  
data = pandas.read_csv("weather_data.csv")  
temp = data["temp"]  
print(temp)
```

>[!question]
>When I gave `print(type(temp))` it is giving me some datatype called `pandas.core.series.Series`. 

>[!success] Answer
>There are only 2 types of data structures in pandas. One is Series and the other is DataFrame.
>1. Series is 1-Dimensional
>2. DataFrame is 2-Dimensional

## Challenge 1 - Find the average of all the temperatures
I used a for loop to iterate through the list and sum it up and use the length operator to divide it by the total number of temperatures.
```py
import pandas

data = pandas.read_csv("weather_data.csv")  
temp = data["temp"]  
print(temp)  
  
sum_of_temp = 0  
for _ in temp:  
    sum_of_temp = sum_of_temp + _  
  
average_temp = sum_of_temp / len(temp)  
  
print(average_temp)
```
But, in the course there was a much easier way to do it
```py
import pandas  
  
data = pandas.read_csv("weather_data.csv")  
temp = data["temp"]  
  
temp_list = temp.to_list()  
average_temp = sum(temp_list) / len(temp_list)  
print(average_temp)
```
The pandas module comes with even more powerful methods. There is a better way to find the mean using the library.
```py
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
```
If I want to get hold of the row where the day is Monday.
```py 
import pandas

data = pandas.read_csv("weather_data.csv")
print(data[data.day == "Monday"])
```

## How to perform Mathematical operations on data from the Pandas
```py
import pandas

data = pandas.read_csv("weather_data.csv")
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(f"Temp in F: {monday_temp_F}")
```

## How to create a DataFrame from scratch
```py
data_dict = {
	"students": {"Amy", "James", "Raghav"}
	"scores": [76, 56, 65]
}
data = pandas.DataFrame(data.dict)
data.to_csv("new_data.csv")
print(data)
```

## Challenge 2 - Great Squirrel Census
1. Import Pandas
2. Open the `csv` file
3. Declare variables for Grey, Black and Cinnamon coloured squirrels.
	```py
	gray_squirrels = len(main_data[main_data["Primary Fur Color"] == "Gray"])
	black_squirrels = len(main_data[main_data["Primary Fur Color"] == "Black"])
	cinnamon_squirrels = len(main_data[main_data["Primary Fur Color"] == "Cinnamon"])
	```
4. Create a dict containing the keys `Fur Color` and `Count`. In which the count is a list of values of the variables.
5. Creating another variable in which, the dict is converted to a DataFrame.
6. And then using the Pandas library to convert that variable to create and store the value in the variable.
#### Full Code
```py
import pandas  
  
main_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")  
gray_squirrels = len(main_data[main_data["Primary Fur Color"] == "Gray"])  
black_squirrels = len(main_data[main_data["Primary Fur Color"] == "Black"])  
cinnamon_squirrels = len(main_data[main_data["Primary Fur Color"] == "Cinnamon"])  
  
data_dict = {  
    "Fur Color": ["Gray", "Black", "Cinnamon"],  
    "Count": [gray_squirrels, black_squirrels, cinnamon_squirrels]  
}  
  
df = pandas.DataFrame(data_dict)  
df.to_csv("squirrel_count.csv")
```

## Project: United States Game
- Use the `turtle` library and use the screen attribute to add a shape to the screen using the `screen.addshape()` and then change the turtle shape to the image.
- Prompt the user to give an answer to the game.
##### Todo
- [x] Convert the guess to Title case
- [x] Check if the guess is among the 50 states
- [x] Write correct guesses onto the map
- [x] Use a loop to allow the user to keep guessing 
- [x] Record the correct guesses in a list
- [x] Keep track of the score
