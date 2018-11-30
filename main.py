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
import xlsxwriter
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
# sim_end - Duration of simulation
# transRange - V2V transmission range (in feet)
# transCap - V2V data transmission capacity of a vehicle

sim_start = 600  # Start time of simulation
sim_end = [12000] #[6000, 12000, 30000, 48000, 60000, 120000, 300000, 480000, 600000]  # Duration of simulation

# Creating an excel file for output
name = "SimulationOutput" + str(sim_start) + ".xlsx"
workbook = xlsxwriter.Workbook(name)
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})
worksheet.set_column(1, 1, 12)
worksheet.set_column(1, 2, 30)
worksheet.set_column(1, 3, 12)
worksheet.set_column(1, 4, 12)
worksheet.set_column(1, 5, 12)
worksheet.write('A1', 'Sim Start', bold)
worksheet.write('B1', 'Sim Duration', bold)
worksheet.write('C1', 'Sim Duration (in min)', bold)
worksheet.write('D1', 'Trans Capacity', bold)
worksheet.write('E1', 'Trans Range', bold)
worksheet.write('F1', 'Trans Efficiency', bold)
row = 1
col = 0

# SIMULATION RUNS
for simDur in range(len(sim_end)):

    maxTransEfficiency = []
    maxInd = []
    OptTransCap = []
    OptTransRange = []
    SimDuration = []
    storeTransEff = []  # stores V2V transmission efficiency values for different parameter inputs
    storeTransCap = []  # stores V2V data transmission capacity values for different parameter inputs
    storeTransRange = []  # stores V2V transmission range values for different parameter inputs

    for VarTransCap in range(5, 6, 1):
        for VarTransRange in range(50, 51, 50):
            transEfficiency = simFunc.simulation_func(sim_start, sim_end[simDur], VarTransRange, VarTransCap)
            print("\nV2V Data Transmission Capacity:", VarTransCap, "vehicles at once")
            print("V2V Transmission Range:", VarTransRange, "feet")
            print("Duration of Simulation:", sim_end[simDur] / (60 * 1000), "minutes")
            print("Efficiency of V2V Information Dissemination:", "%.6f" % transEfficiency, "percent")
            storeTransEff.append(transEfficiency)
            storeTransCap.append(VarTransCap)
            storeTransRange.append(VarTransRange)
            worksheet.write(row, col, sim_start)
            worksheet.write(row, col + 1, sim_end[simDur])
            worksheet.write(row, col + 2, (sim_end[simDur]/(60 * 1000)))
            worksheet.write(row, col + 3, VarTransCap)
            worksheet.write(row, col + 4, VarTransRange)
            worksheet.write(row, col + 5, transEfficiency)
            row += 1

    # Optimum values for every simulation duration
    maxTransEfficiency = max(storeTransEff)
    maxInd = storeTransEff.index(max(storeTransEff))
    OptTransCap = storeTransCap[maxInd]
    OptTransRange = storeTransRange[maxInd]
    SimDuration = sim_end[simDur]

    # Writing optimum values in excel file
    worksheet.write(row, col, 'Optimum')
    row += 1
    worksheet.write(row, col, sim_start)
    worksheet.write(row, col + 1, SimDuration)
    worksheet.write(row, col + 2, (SimDuration/(60 * 1000)))
    worksheet.write(row, col + 3, OptTransCap)
    worksheet.write(row, col + 4, OptTransRange)
    worksheet.write(row, col + 5, maxTransEfficiency)
    row += 2

    # Printing optimum results for every simulation duration
    print("\nOptimum results")
    print("For simulation start time:", "%.3f" % (sim_start / (60 * 1000)),
          "minutes; simulation duration:", "%.3f" % (SimDuration / (60 * 1000)), "minutes")
    print("Maximum Transmission Efficiency:", "%.4f" % maxTransEfficiency, "percent")
    print("Optimum Transmission Capacity:", OptTransCap, "vehicles at once")
    print("Optimum Transmission Range:", OptTransRange, "feet")

workbook.close()

#
# # ---------------- main loop of the program ---------------- #
# while True:
#
#     # event processing, user does stuff here or game is exited
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit(0) # exit the whole program
#
#     render.Background(screen).draw()  # render the screen
#
#     # generate and draw all car objects
#     tmp_df=df_test[df_test['Global_Time']==TimePoint]
#     tmp_ID=tmp_df['Vehicle_ID'].unique()
#
#     for key in tmp_ID:
#         X=float(tmp_df[tmp_df['Vehicle_ID']==key].Local_X)
#         Y=float(tmp_df[tmp_df['Vehicle_ID']==key].Local_Y)
#         carData[key].update(vID=key,xLoc=X,yLoc=Y)
#
#
#     for key in tmp_ID:
#         item=carData[key]
#         render.Car(screen,x=item.xLoc,y=item.yLoc, color=item.color).draw(RangeXY)
#
#
#     TimePoint += 100
#     '''
#     for i in range(0, len(sorted_df)):
#         timeStep_df = sorted_df[sorted_df['Global_Time'] == time]
#         if(len(timeStep_df) != 0): # loop through the time step dataframe
#             time += 100 # update the time step on each iteration
#             print(timeStep_df)
#
#         #THIS IS WHERE THE OBJECTS WILL BE GENERATED FROM KEYUAN'S OBJECT FILE
#         else:
#             break
#     '''
#
#
#
#
#     '''
#     #Original car rendering from csv
#     for key in carData.keys():
#         render.Car(screen, cid=key, direction=carData[key][0], speed=carData[key][1],
#                    x=carData[key][2], y=carData[key][3]).draw()
#     '''
#
#     # update car x-position
#
#     '''
#     #THIS WAS THE ORIGINAL CARDATA POSITION UPDATE FOR GUI PURPOSES
#     for key in carData.keys():
#         if carData[key][2] <= Size[0]:
#             carData[key][2] += carData[key][1]/5  # speed cut by factor of 5 to prevent cars from looking too fast
#         else:
#             carData[key][2] = -20
#     '''
#
#
#     #NOTE: THIS SECTION NEEDS UPDATED ONCE KEYUAN'S OBJECTS ARE CREATED
#
#     if TimePoint==GT[100]:
#         pass
#         #time.sleep(10)
#
#     pygame.display.update()
#     clock.tick(fps)
