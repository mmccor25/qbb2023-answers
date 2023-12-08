#!/usr/bin/env python

import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt

numbats = pd.read_csv("numbats.csv")

coords = numbats.loc[:, ("decimalLatitude", "decimalLongitude")]

latitude = coords.loc[:, "decimalLatitude"].notnull()
longitude = coords.loc[:, "decimalLongitude"].notnull()

coords = coords.loc[latitude & longitude, :]


# map
australia = pd.read_csv("australia_map.csv", header = None)

australia_map, ax = plt.subplots()
ax.scatter(australia[1], australia[0], s=1)
ax.scatter(coords["decimalLongitude"], coords["decimalLatitude"], s=4)
ax.set_title("Numbat sightings in Australia")
ax.set_xlabel("degrees longitude")
ax.set_xlabel("degrees latitude")
australia_map.savefig("australia.png")



#hours of day
hours = numbats.loc[:, ("hour")]

hours_hist, ax = plt.subplots()
ax.hist(hours, bins=list(range(int(max(numbats.loc[numbats["hour"].notnull(), ("hour")])))))
ax.set_title("Numbat sightings over the hours of the day")
ax.set_xlabel("Hour of the day")
hours_hist.savefig("hours_of_day.png")



# months

months = numbats.loc[:, "month"]


months_notnull = numbats.loc[:, ("month")].notnull()
months = months.loc[months_notnull]

month_counts = months.value_counts()

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

monthbar, ax = plt.subplots()
plt.bar(month_names, month_counts.loc[month_names]) 
ax.set_title("Numbat sightings over the months of the year")
monthbar.savefig("months_of_year.png")



