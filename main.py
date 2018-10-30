# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 11:00:54 2018

@author: Qicheng

Now is better than never.
"""

import pygame
import render
from constant import *
import pandas as pd

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


PATH_LOAD = "./Data/us101_test.csv"
df = pd.read_csv(PATH_LOAD)

sorted_df = df.sort_values(by=['Global_Time'])

# ----------------------------------------------- #
screen = pygame.display.set_mode(Size)
print(Size)
pygame.display.set_caption("V2V")

clock = pygame.time.Clock()

# main loop of the program
while True:

    # event processing, user does stuff here or game is exited
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    render.Background(screen).draw()  # render the screen

    # generate and draw all car objects

    for i in range(0, len(sorted_df)):
    timeStep_df = sorted_df[sorted_df['Global_Time'] == time]
    if(len(timeStep_df) != 0): # loop through the time step dataframe
        time += 100 # update the time step on each iteration
        #print(timeStep_df)

        #THIS IS WHERE THE OBJECTS WILL BE GENERATED FROM KEYUAN'S OBJECT FILE
    else:
        break

    '''Original car rendering from csv
    for key in carData.keys():
        render.Car(screen, cid=key, direction=carData[key][0], speed=carData[key][1],
                   x=carData[key][2], y=carData[key][3]).draw()
    '''

    # update car x-position


    
    ''' THIS WAS THE ORIGINAL CARDATA POSITION UPDATE FOR GUI PURPOSES
    for key in carData.keys():
        if carData[key][2] <= Size[0]:
            carData[key][2] += carData[key][1]/5  # speed cut by factor of 5 to prevent cars from looking too fast
        else:
            carData[key][2] = -20
    '''
    
    #NOTE: THIS SECTION NEEDS UPDATED ONCE KEYUAN'S OBJECTS ARE CREATED

    pygame.display.update()
    clock.tick(fps)





