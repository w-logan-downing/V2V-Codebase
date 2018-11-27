# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 11:00:54 2018

@author: Qicheng

Now is better than never.
"""
import sys
import os
import pygame
import render
from constant import *
import pandas as pd
import numpy as np
import csv
import us_101 as us101
import time
import random
import simulation_func as simFunc

pygame.init()  # initialize the pygame framework

# ------------Collect Car Data------------------- #
'''
file = "Data\\exampleData.csv"
    
carData = {}  # store all data for the cars
    
with open(file, 'r') as data:
    csv_reader = csv.reader(data)
    
    next(csv_reader)  # skip past the initial header row
    for line in csv_reader:
        carData[int(line[0])] = [int(i) for i in line[1:]]
'''

#------------change the directory to your own-----------------#
#os.chdir('D:\Purdue\CS501\V2V\Code\Github\V2V-Codebase')
os.getcwd()
PATH_LOAD = "./Data/us-101.csv"
#PATH_LOAD = "./Data/lankershim.csv"
if 'df101' in vars():
    pass
else:
    df101 = pd.read_csv(PATH_LOAD)

#----test data----#
df_test=df101 #.iloc[:10000,:]
RangeXY=[min(df_test['Local_X']),max(df_test['Local_X']),
        min(df_test['Local_Y']),max(df_test['Local_Y'])]
ID=df_test['Vehicle_ID'].unique()
GT=df_test['Global_Time'].unique()
ID.sort()
GT.sort()
StartTime=GT[0]
TimePoint=GT[0]

carData={}
for i in ID:
    carData[i]=us101.Vehicle(vID=i, color=random.choice([imgR,imgB])) # store vehicle object in carData dictionary
# ----------------------------------------------- #
screen = pygame.display.set_mode(Size)
#print(Size)
pygame.display.set_caption("V2V")

clock = pygame.time.Clock()


# ---------- Finding efficiency of information dissemination with different parameters ---------- #
# Needs simulation_func.py file
# Developed by: Samarth Jain
# Tested by: Samarth Jain

# VARIABLES
# transRange - V2V transmission range (in feet)
# transCap - V2V data transmission capacity of a vehicle

sim_start = 10000  # Start time of simulation
sim_end = 6000  # Duration of simulation (typically 600000)
storeTransEff = []  # stores V2V transmission efficiency values for different parameter inputs
storeTransRange = []  # stores V2V transmission range values for different parameter inputs
storeTransCap = []  # stores V2V data transmission capacity values for different parameter inputs

# SIMULATION RUNS
for VarTransCap in range(1, 6, 1):
    for VarTransRange in range(50, 501, 50):
        transEfficiency = simFunc.simulation_func(sim_start, sim_end, VarTransRange, VarTransCap)
        print("\nV2V Data Transmission Capacity:", VarTransCap, "vehicles at once")
        print("V2V Transmission Range:", VarTransRange, "feet")
        print("Duration of Simulation:", sim_end / (60 * 1000), "minutes")
        print("Efficiency of V2V Information Dissemination:", "%.6f" % transEfficiency, "percent")
        storeTransEff.append(transEfficiency)
        storeTransRange.append(VarTransRange)
        storeTransCap.append(VarTransCap)

# OPTIMUM VALUES
maxTransEfficiency = max(storeTransEff)
maxInd = storeTransEff.index(max(storeTransEff))
OptTransCap = storeTransCap[maxInd]
OptTransRange = storeTransRange[maxInd]

print("\nOptimum results")
print("For simulation start time:", "%.2f" % (sim_start/(60*1000)),
      "minutes; simulation duration:", "%.2f" % (sim_end/(60 * 1000)), "minutes")
print("Maximum Transmission Efficiency:", "%.4f" % maxTransEfficiency, "percent")
print("Optimum Transmission Capacity:", OptTransCap, "vehicles at once")
print("Optimum Transmission Range:", OptTransRange, "feet")


# ---------------- main loop of the program ---------------- #
while True:

    # event processing, user does stuff here or game is exited
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0) # exit the whole program
    
    render.Background(screen).draw()  # render the screen
    
    # generate and draw all car objects
    tmp_df=df_test[df_test['Global_Time']==TimePoint]
    tmp_ID=tmp_df['Vehicle_ID'].unique()
    
    for key in tmp_ID:
        X=float(tmp_df[tmp_df['Vehicle_ID']==key].Local_X)
        Y=float(tmp_df[tmp_df['Vehicle_ID']==key].Local_Y)
        carData[key].update(vID=key,xLoc=X,yLoc=Y)


    for key in tmp_ID:
        item=carData[key]
        render.Car(screen,x=item.xLoc,y=item.yLoc, color=item.color).draw(RangeXY)


    TimePoint += 100
    '''
    for i in range(0, len(sorted_df)):
        timeStep_df = sorted_df[sorted_df['Global_Time'] == time]
        if(len(timeStep_df) != 0): # loop through the time step dataframe
            time += 100 # update the time step on each iteration
            print(timeStep_df)

        #THIS IS WHERE THE OBJECTS WILL BE GENERATED FROM KEYUAN'S OBJECT FILE
        else:
            break
    '''




    '''
    #Original car rendering from csv
    for key in carData.keys():
        render.Car(screen, cid=key, direction=carData[key][0], speed=carData[key][1],
                   x=carData[key][2], y=carData[key][3]).draw()
    '''

    # update car x-position

    '''
    #THIS WAS THE ORIGINAL CARDATA POSITION UPDATE FOR GUI PURPOSES
    for key in carData.keys():
        if carData[key][2] <= Size[0]:
            carData[key][2] += carData[key][1]/5  # speed cut by factor of 5 to prevent cars from looking too fast
        else:
            carData[key][2] = -20
    '''


    #NOTE: THIS SECTION NEEDS UPDATED ONCE KEYUAN'S OBJECTS ARE CREATED

    if TimePoint==GT[100]:
        pass
        #time.sleep(10)

    pygame.display.update()
    clock.tick(fps)
    





