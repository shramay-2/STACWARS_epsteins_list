import data_cleaner as c
import pandas as pd
import matplotlib.pyplot as plt

daily_avg = (c.grouped["Radiation"].mean())
daily_max = (c.grouped["Radiation"].max())

max_rad_date = c.df.loc[(c.df["Radiation"].idxmax()), "Date"]

values_for_max_rad = c.df.loc[(c.df["Radiation"].idxmax()), ["Time","Temperature", "Humidity", "Speed"]]

top_5_days = list(daily_max.nlargest(5).index)

# print(top_5_days)
# print(values_for_max_rad)

# print(daily_avg)
# print(daily_max)

# print(max_rad_date)
# print(values_for_max_rad)

print(top_5_days)