# with open("./data/weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)


# import csv
#
# with open("./data/weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)


import pandas

data = pandas.read_csv("./data/weather_data.csv")
# print(data)

data_dict = data.to_dict()
# print(data_dict)

# temp_list = data.to_list()
# print(temp_list)

# print(f"average of temp: {data['temp'].mean()}")
# print(f"min temp: {data['temp'].min()}")
# print(f"max temp: {data['temp'].max()}")

# print(data[data.temp == data.temp.max()])

