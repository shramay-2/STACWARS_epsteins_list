import pandas as pd
import matplotlib.pyplot as plt
from datetime import time

df = pd.read_csv(r"SolarPrediction.csv")
df = df.rename(columns={"Data" : "Date"})
df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")

df["DateTime"] = pd.to_datetime(df["Date"] + " " + df["Time"]) 

grouped = df.groupby("Date")

day_only = df[(df["DateTime"].dt.time < time(18)) & (df["DateTime"].dt.time > time(6))]#.groupby("Date")
print(df.columns)

df1 = df[['UNIXTime', 'DateTime', 'Radiation', 'Temperature', 'Pressure',
       'Humidity', 'WindDirection(Degrees)', 'Speed', 'TimeSunRise',
       'TimeSunSet',]]

print(df1.head())
 
# print(day_only.shape)
# print(day_only[["Date", "Time", "DateTime"]].head())