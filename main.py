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
import csv
import us_101 as us101
import time


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
os.chdir('D:\Purdue\CS501\V2V\Code\Github\V2V-Codebase')
os.getcwd()
PATH_LOAD = "./Data/us-101.csv"
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
    carData[i]=us101.Vehicle(vID=i)
# ----------------------------------------------- #
screen = pygame.display.set_mode(Size)
#print(Size)
pygame.display.set_caption("V2V")

clock = pygame.time.Clock()

# main loop of the program

while True:

    # event processing, user does stuff here or game is exited
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0) #for spyder to exit the whole program
            #quit() #for IDLE?
    
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
        render.Car(screen,x=item.xLoc,y=item.yLoc).draw(RangeXY)
    
    
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
    





