# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_files:
#     data = csv.reader(data_files)
#     temperature = []
#     for row in data:
#         # print(row)
#         if row[1]!="temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)