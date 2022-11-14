import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_black = data[data["Primary Fur Color"] == "Black"]
fur_gray = data[data["Primary Fur Color"] == "Gray"]
fur_red = data[data["Primary Fur Color"] == "Red"]

fur_dict = {"Fur Color": ["black", "gray", "red"], "Count": [len(fur_black), len(fur_gray), len(fur_red)]}
data_squirrel_count = pandas.DataFrame(fur_dict)
data_squirrel_count.to_csv("squirrel_count.csv")