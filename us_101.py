# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 23:35:22 2018

@author: V2V
"""

import pandas as pd
import numpy as np
from constant import *

class Vehicle:
    
    """
    This is a standard class for each vehicle.
    Variables:
    vID        is Vehicle_ID  in the processed datasheet.
    globalTime is Global_Time in the processed datasheet.
    xLoc       is Local_X     in the processed datasheet.
    yLoc       is Local_Y     in the processed datasheet.
    vVel       is v_Vel       in the processed datasheet.
    laneID     is Lane_ID     in the processed datasheet.
    move       is Movement    in the processed datasheet.
    transRange is a pre-set parameter for each vehicle.
    haveData   is to indicate if this vehicle has the data or not.

    Main methods:
    update method is to feed real time data to this vehicle and update all its variables.
    """
    
    def __init__(self, vID=-1, color=imgR, globalTime=-1, xLoc=-1, yLoc=-1, vVel=-1, laneID=-1, move = float('nan'), transRange = 500, haveData = 0):
        self.vID = vID
        self.color = color #determines the intial color of the vehicle
        self.globalTime = globalTime
        self.startTime = globalTime # Initialize the startTime for each vehicle by the first globalTime
        self.lastTime = globalTime # Initialize the lastTime for each vehicle by the first globalTime
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.vVel = vVel
        self.laneID = laneID
        self.move = move
        self.transRange = transRange
        self.haveData = haveData
        #self.onRoad = onRoad
        
    def update(self, vID, globalTime=-1, xLoc=-1, yLoc=-1, vVel=-1, laneID=-1, move = float('nan'), currentVehiclesList=[]):
        if vID == self.vID: # Check if the feed data is for the vehicle itself
            self.globalTime = globalTime
            self.xLoc = xLoc
            self.yLoc = yLoc
            self.vVel = vVel
            self.laneID = laneID
            self.move = move
            '''
            if self.checkOnRoad():
                for vehicle in currentVehiclesList:
                    if self.checkVehiclesInRange(vehicle):
                        vehicle.haveData = 1
            else:
                self.haveData = 0 # Re-initialize the haveData in order to make this vehicle as a new vehicle
                self.startTime = globalTime # Re-initialize the startTime for this vehicle by new globalTime
                self.lastTime = globalTime # Re-initialize the lastTime for this vehicle by new globalTime
            '''
    def checkVehiclesInRange(self, other):
        """
        This method is to check if the selected vehicle is within the transmission range.
        """
        distance = np.sqrt( (other.xLoc - self.xLoc)**2 + (other.yLoc - self.yLoc)**2 )
        if distance < self.transRange:
            return True
        else:
            return False
    '''
    def checkOnRoad(self):
        """
        This method is to check if this vehicle is still on the road.
        """
        if self.globalTime == self.lastTime + 100:
            return True
        else:
            return False
    '''
def coveragePercent(currentVehicleList):
    """
    This method is to calculate the percentage of vehicles that have the data in real-time.
    """
    countVehiclesHaveData = 0
    for vehicle in currentVehicleList:
        if vehicle.haveData == 1:
            countVehiclesHaveData += 1
    return countVehiclesHaveData/len(currentVehicleList)

if __name__ == '__main__':
    
    PATH_LOAD = "Data\\us-101.csv"
    df = pd.read_csv(PATH_LOAD)
    print(df.shape)

    print(df.iloc[5:10, :]) # A section of dataframe
    dfID2 = df[df['Vehicle_ID'] == 2]
    print(dfID2.iloc[435:440, :])
