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
