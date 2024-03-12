"""with open("weather_data.csv", mode="r+") as f:
    data = f.readlines()
    for x in data:
        print(x)

"""


# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# data_list = data["temp"].to_list()
# print(data_list)
#
# total_numbers = 0
# sum = 0
#
# for x in data_list:
#     sum += x
#     total_numbers += 1
#
# avg = (sum/total_numbers)
# print(avg)
#
# print(data["temp"].max())

import pandas

Gray_sq = 0
Cinnamon_sq = 0
Black_sq = 0
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240312.csv")
sq_color_list = data["Primary Fur Color"].to_list()

for x in sq_color_list:
    if x == "Gray":
        Gray_sq += 1
    if x == "Cinnamon":
        Cinnamon_sq += 1
    if x == "Black":
        Black_sq += 1

print(Gray_sq)
print(Cinnamon_sq)
print(Black_sq)

data_dict = {
    "Primary Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [Gray_sq, Cinnamon_sq, Black_sq]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Jate.csv")
