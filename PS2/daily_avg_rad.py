import data_cleaner as c
import pandas as pd
import matplotlib.pyplot as plt

daily_avg = (c.day_only.groupby("Date")["Radiation"].mean())
fig, ax = plt.subplots()



ax.plot(daily_avg.index, daily_avg.values)
fig.autofmt_xdate()
ax.set_xticks(list(daily_avg.index)[::5])

plt.show()