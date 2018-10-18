# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 11:00:54 2018

@author: Qicheng

Now is better than never.
"""

import pygame
import render
from constant import *
import csv



pygame.init()  # initialize the pygame framework

# ------------Collect Car Data------------------- #
file = "Data\\exampleData.csv"

carData = {}  # store all data for the cars

with open(file, 'r') as data:
    csv_reader = csv.reader(data)

    next(csv_reader)  # skip past the initial header row
    for line in csv_reader:
        carData[int(line[0])] = [int(i) for i in line[1:]]
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
    for key in carData.keys():
        render.Car(screen, cid=key, direction=carData[key][0], speed=carData[key][1],
                   x=carData[key][2], y=carData[key][3]).draw()

    # update car x-position
    for key in carData.keys():
        if carData[key][2] <= Size[0]:
            carData[key][2] += carData[key][1]/5  # speed cut by factor of 5 to prevent cars from looking too fast
        else:
            carData[key][2] = -20

    pygame.display.update()
    clock.tick(fps)





