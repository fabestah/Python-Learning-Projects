import csv

import pandas

temps = []

data = pandas.read_csv("data.csv")

temp_list = data["temp"].to_list()

avg_temp = sum(temp_list) / len(temp_list)

highest_temp = data["temp"].max()

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Rows
print(data.temp == highest_temp)

monday = data[data.day == "Monday"]
temp_c_monday = monday.temp
temp_f_monday = temp_c_monday * 9 / 5 + 32
print(temp_f_monday)

# Create Dataframe from scratch
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 77, 29]}
data = pandas.DataFrame(data_dict)
print(data)

# Create CSV File from Dataframe
data.to_csv("new_data.csv")
