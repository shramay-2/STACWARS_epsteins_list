import data_cleaner as c
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

for date, group in c.grouped:
    hour = group["DateTime"].dt.hour
    minunte =  group["DateTime"].dt.minute
    x = hour + minunte/60
    y = group["Radiation"]
    ax.scatter(x,y, alpha=0.2, color = "#C93F21", s=5)

df1 = c.df.copy()

df1["Time"] = df1["DateTime"].dt.round("5min").dt.time

y1 = df1.groupby("Time")["Radiation"].median()

ax.plot(x, y1.values, linewidth = 4, label = 'median')

print(df1.groupby("Time")["Radiation"].median().idxmax())  #prints the time at which the radaiiton is t =he highest

fig.set_label("Variation of Radiation with Time")
ax.set_xlabel("Time")
ax.set_ylabel("Radiation")
ax.set_label('variation of solar radiation with time')
ax.set_xticks(range(25))
ax.set_xticklabels([
    "00:00", "01:00", "02:00", "03:00", "04:00",
    "05:00", "06:00", "07:00", "08:00", "09:00",
    "10:00", "11:00", "12:00", "13:00", "14:00",
    "15:00", "16:00", "17:00", "18:00", "19:00",
    "20:00", "21:00", "22:00", "23:00", "24:00"
])

fig.set_size_inches(30,10)
ax.legend()
ax.grid()

plt.show()