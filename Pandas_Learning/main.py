import pandas as pd

data = pd.read_csv("weather_data.csv")
#print(type(data))
#print(data["temp"])

temp_list = data["temp"].to_list()

print(data["temp"].mean())

print(data["temp"].max())

#Get Data in Columns

print(data)