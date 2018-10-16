# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 09:47:47 2018

@author: Qicheng

Now is better than never.
"""

#data_cleaning
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tqdm import tqdm
from pandas.core.frame import DataFrame

if 'df' in vars():
    pass
else:
    df=pd.read_csv("Next_Generation_Simulation__NGSIM__Vehicle_Trajectories_and_Supporting_Data.csv")
    dfCar = df[df['v_Class'] == 2]
    LeftList=['Vehicle_ID','Global_Time','Local_X','Local_Y','Location']
    dfCAR=dfCar[LeftList]
    dfCAR=dfCAR.sort_values(by=['Vehicle_ID','Global_Time'])

##elapsed time from 1970, the time should be bigger than 30 years (CriT /milliseconds)
CriT=30*365*24*3600*1000
WrongT_CAR=dfCAR[dfCAR['Global_Time']<CriT]

#The Vehicle_ID that contain wrong time
WrongT_ID=list(set(list(WrongT_CAR['Vehicle_ID'])))

#The Vehicle_ID of total cars
CAR_ID=list(set(list(dfCAR['Vehicle_ID']))) #nearly half of the vehicles contain wrong time data

#Some examples show that the wrong time data shows no consistency with the remaining data
Vehicle2=dfCAR[dfCAR['Vehicle_ID']==2]
Vehicle4=dfCAR[dfCAR['Vehicle_ID']==4]

#Time Corrected Car data. Write the data to a new csv file
tcCAR=dfCAR[dfCAR['Global_Time']>CriT]
tcCAR=tcCAR.sort_values(by=['Location','Vehicle_ID','Global_Time'])
tcCAR.to_csv('Sorted_Time_Corrected_Data.csv')

#There're only 3 roads left, all the data on location "peachtree" have wrong time
RoadNames=list(set(list(tcCAR['Location'])))
RoadNames.sort()
WrongT_RoadNames=list(set(list(WrongT_CAR['Location'])))

#divide dataset into three based on Location
df80=tcCAR[tcCAR['Location']==RoadNames[0]]
dfLan=tcCAR[tcCAR['Location']==RoadNames[1]]
df101=tcCAR[tcCAR['Location']==RoadNames[2]]

#List the time in order and find how many cars are there at the same time on each road
Tof80=list(set(list(df80['Global_Time'])))
TofLan=list(set(list(dfLan['Global_Time'])))
Tof101=list(set(list(df101['Global_Time'])))
Tof80.sort();TofLan.sort();Tof101.sort()
Nof80=np.zeros(len(Tof80))
NofLan=np.zeros(len(TofLan))
Nof101=np.zeros(len(Tof101))

#find how many cars are there at the same time on us-101 road
n=0
for i in tqdm(Tof80):
    N=len(df80[df80['Global_Time']==i])
    Nof80[n]=N
    n+=1

#find how many cars are there at the same time on us-101 road
n=0
for i in tqdm(TofLan):
    N=len(dfLan[dfLan['Global_Time']==i])
    NofLan[n]=N
    n+=1

#find how many cars are there at the same time on us-101 road
n=0
for i in tqdm(Tof101):
    N=len(df101[df101['Global_Time']==i])
    Nof101[n]=N
    n+=1


plt.close('all')
#show the diagrams of Number_of_Cars vs. time series on each road
plt.figure(1)
plt.plot(range(len(Nof80)),Nof80)
plt.title('i-80 NofCars vs. Time')
plt.xlabel('time sequence /0.1sec')

plt.figure(2)
plt.plot(range(len(NofLan)),NofLan)
plt.title('lankershim NofCars vs. Time')
plt.xlabel('time sequence /0.1sec')

plt.figure(3)
plt.plot(range(len(Nof101)),Nof101)
plt.title('us-101 NofCars vs. Time')
plt.xlabel('time sequence /0.1sec')



