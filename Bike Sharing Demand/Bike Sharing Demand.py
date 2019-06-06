# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 20:36:11 2018

@author: pc
"""

import pylab
import calendar
import numpy as np
import pandas as pd
import seaborn as sn
from scipy import stats
#import missingno as msno
from datetime import datetime
import matplotlib.pyplot as plt
import warnings
pd.options.mode.chained_assignment = None
warnings.filterwarnings("ignore", category=DeprecationWarning)

dailyData = pd.read_csv(r"C:\Users\pc\Desktop\Data Science Folder\Data_Science_Portfolio\Bike Sharing Demand\train.csv")

print( dailyData )

#print ( dailyData.columns )


#print ( dailyData.sample(10) )

#print ( dailyData.dtypes )

#print ( dailyData.datetime )

dailyData["date"] = dailyData.datetime.apply(lambda x : x.split()[0])

#for x in dailyData['date']:
    #print ( calendar.day_name[datetime.strptime( x ,"%Y-%m-%d").weekday()] )
    
dailyData["hour"] = dailyData.datetime.apply(lambda x : x.split()[1].split(":")[0])

dailyData["weekday"] = dailyData.date.apply(lambda dateString : calendar.day_name[datetime.strptime(dateString,"%Y-%m-%d").weekday()])

print ( dailyData ) 

dailyData["month"] = dailyData.date.apply(lambda dateString : calendar.month_name[datetime.strptime(dateString,"%Y-%m-%d").month])
dailyData["season"] = dailyData.season.map({1: "Spring", 2 : "Summer", 3 : "Fall", 4 :"Winter" })
dailyData["weather"] = dailyData.weather.map({1: " Clear + Few clouds + Partly cloudy + Partly cloudy",\
                                        2 : " Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist ", \
                                        3 : " Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds", \
                                        4 :" Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog " })
    

categoryVariableList = ["hour","weekday","month","season","weather","holiday","workingday"]
for var in categoryVariableList:
    dailyData[var] = dailyData[var].astype("category")
    

dailyData  = dailyData.drop(["datetime"],axis=1)

print ( dailyData.dtypes.value_counts()  )

dataTypeDf = pd.DataFrame(dailyData.dtypes.value_counts()).reset_index().rename(columns={"index":"variableType",0:"count"})


print( dailyData.isnull().sum()
