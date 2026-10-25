import data_cleaner as c
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots(3,2) 

tempN = ax[0,0]
tempD = ax[0,1]
humD = ax[1,1]
humN = ax[1,0]
windD = ax[2,1]
windN = ax[2,0]

#day only temp vs rad
tempD.scatter(c.day_only["Temperature"], c.day_only["Radiation"],  
              alpha=0.2, color = "#C93F21", s=5)
y = c.day_only.groupby(["Temperature"])["Radiation"].median()
tempD.plot(y.index, y.values, label = "median")
tempD.set_xlabel("Temperature(F)")
tempD.set_ylabel("Radiation(Watt/m^2)")
tempD.set_title('Temperature vs Radiation vaiation only during daytime')
tempD.grid()
tempD.legend()

#overall temp vs rad
tempN.scatter(c.df["Temperature"], c.df["Radiation"],  alpha=0.2, color = "#C93F21", s=5)
y = c.df.groupby(["Temperature"])["Radiation"].median()
tempN.plot(y.index, y.values, label = "median")
tempN.set_xlabel("Temperature(F)")
tempN.set_ylabel("Radiation(Watt/m^2)")
tempN.set_title('Temperature vs Radiation vaiation throughout the day')
tempN.grid()
tempN.legend()



#day only hum vs rad
humD.scatter(c.day_only["Humidity"], c.day_only["Radiation"],  alpha=0.2, color = "#C93F21", s=5)
y = c.day_only.groupby(["Humidity"])["Radiation"].median()
humD.plot(y.index, y.values, label = "median")
humD.set_xlabel("Humidity(%)")
humD.set_ylabel("Radiation(Watt/m^2)")
humD.set_title('Humidity vs Radiation vaiation only during daytime')
humD.grid()
humD.legend()

#overall hum vs rad
humN.scatter(c.df["Humidity"], c.df["Radiation"],  alpha=0.2, color = "#C93F21", s=5)
y = c.df.groupby(["Humidity"])["Radiation"].median()
humN.plot(y.index, y.values, label = "median")
humN.set_xlabel("Humidity(%)")
humN.set_ylabel("Radiation(Watt/m^2)")
humN.set_title('Humidity vs Radiation vaiation throughout the day')
humN.grid()
humN.legend()



#day only wind vs rad
windD.scatter(c.day_only["Speed"], c.day_only["Radiation"],  alpha=0.2, color = "#C93F21", s=5)
y = c.day_only.groupby(["Speed"])["Radiation"].median()
windD.plot(y.index, y.values, label = "median")
windD.set_xlabel("Speed(miles/hr)")
windD.set_ylabel("Radiation(Watt/m^2)")
windD.set_title('Speed vs Radiation vaiation only during daytime')
windD.grid()
windD.legend()

#overall wind vs rad
windN.scatter(c.df["Speed"], c.df["Radiation"],  alpha=0.2, color = "#C93F21", s=5)
y = c.df.groupby(["Speed"])["Radiation"].median()
windN.plot(y.index, y.values, label = "median")
windN.set_xlabel("Speed(miles/hr)")
windN.set_ylabel("Radiation(Watt/m^2)")
windN.set_title('Speed vs Radiation vaiation throughout the day')
windN.grid()
windN.legend()


# humD.set_visible(False)
# humN.set_visible(False)
# windD.set_visible(False)
# windN.set_visible(False)

fig.tight_layout()
fig.set_size_inches(30,5)
plt.show()