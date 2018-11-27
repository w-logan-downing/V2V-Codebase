# Simulation code
# Independent code (can run separately from main.py file)
# This code runs the main simulation for V2V information dissemination
# Chooses a random vehicle as initial data carrier;
# Calculates distance of vehicles with no data from vehicles with data;
# Check if vehicle is within transmission range;
# Randomly choose vehicles for transmitting data;
# Update the vehicle characteristics for next time slot

# Developed by: Samarth Jain
# Tested by: Samarth Jain
# 11-19-2018

import os
import pandas as pd
import numpy as np
import csv
import us_101 as us101
import time
import random


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
df_test = df101 #.iloc[:10000,:]
RangeXY = [min(df_test['Local_X']),max(df_test['Local_X']),
        min(df_test['Local_Y']),max(df_test['Local_Y'])]
ID = df_test['Vehicle_ID'].unique()
GT = df_test['Global_Time'].unique()
ID.sort()
GT.sort()

# ---- SIMULATION PARAMETERS - Start time, Duration, Transmission range, Transmission capacity ---- #
sim_start = 500  # Start time of simulation
StartTime = GT[sim_start]
TimePoint = GT[sim_start]
sim_end = 60000  # Duration of simulation (typically 600000)
transRange = 500  # in feet
transCap = 3  # data transmission capacity of a vehicle

carData = {}
for i in ID:
    carData[i] = us101.Vehicle(vID=i)  # store vehicle object in carData dictionary

# ------ Assign data to one random vehicle at beginning of simulation ------ #
# carData[332].haveData = 1
tmp_df = df_test[df_test['Global_Time'] == TimePoint]
tmp_ID = tmp_df['Vehicle_ID'].unique()
rndVehIniData = random.sample(range(len(tmp_ID)), 1)
carData[tmp_ID[rndVehIniData[0]]].haveData = 1

# ---------- Initializing the main loop ---------- #
storeVehicles = []  # stores IDs of all vehicles that enter the simulation
storeVehWithData = []  # stores IDs of all vehicles that have data

# ------ Running the main simulation loop ------ #
while (TimePoint - StartTime) <= sim_end:

    # generate and draw all car objects
    tmp_df = df_test[df_test['Global_Time'] == TimePoint]
    tmp_ID = tmp_df['Vehicle_ID'].unique()

    storeVehicles.append(tmp_ID)  # stores IDs of all vehicles that enter the simulation

    # ------ Find vehicles that already have data (information packet) ------ #
    storeVehWithData = []
    for veh in range(len(tmp_ID)):
        if carData[tmp_ID[veh]].haveData == 1:
            storeVehWithData.append(tmp_ID[veh])  # stores IDs of all vehicles that already have data

    # ------ Checking v2v distance b/w every vehicle with data and without data ------ #
    dist = 0
    for vehWithData in range(len(storeVehWithData)):
        VehInRange_vID = []  # stores IDs of all vehicles that are within transmission range
        VehForTrans = []  # stores IDs of randomly chosen vehicles within transmission range and capacity
        for vehNoData in range(len(tmp_ID)):
            if carData[tmp_ID[vehNoData]].xLoc != -1:
                dist = np.sqrt((carData[storeVehWithData[vehWithData]].xLoc - carData[tmp_ID[vehNoData]].xLoc)**2 +
                               (carData[storeVehWithData[vehWithData]].yLoc - carData[tmp_ID[vehNoData]].yLoc)**2)
            if dist <= transRange and dist > 0:
                VehInRange_vID.append(carData[tmp_ID[vehNoData]].vID)
        if len(VehInRange_vID) > transCap:
            rndVehForTrans = random.sample(range(len(VehInRange_vID)), transCap)
            for i in range(len(rndVehForTrans)):
                VehForTrans.append(VehInRange_vID[rndVehForTrans[i]])  # Vehicle IDs for transmitting data
        else:
            VehForTrans = VehInRange_vID  # Vehicle IDs for transmitting data
        # Passing data to randomly chosen vehicles in transmission range
        for vehDataUpdate in range(len(VehForTrans)):
            carData[VehForTrans[vehDataUpdate]].haveData = 1

    # ------------------ updating the data after t = 100 (0.1 sec) ------------------ #
    TimePoint += 100
    for key in tmp_ID:
        X = float(tmp_df[tmp_df['Vehicle_ID'] == key].Local_X)
        Y = float(tmp_df[tmp_df['Vehicle_ID'] == key].Local_Y)
        carData[key].update(vID=key, xLoc=X, yLoc=Y)

# -------------- For all vehicles that enter the simulation -------------- #
VehAllInSim = np.concatenate(storeVehicles, axis=0)
VehAllInSim = pd.unique(VehAllInSim).tolist()
VehAllInSim.sort()
# print("\nAll vehicles in simulation:", VehAllInSim)
print(len(VehAllInSim))

# -------------- For all vehicles that have data at end of simulation -------------- #
VehWithData = pd.unique(storeVehWithData).tolist()
VehWithData.sort()
# print("\nVehicles with data:", VehWithData)
print(len(VehWithData))

# ------------------ Transmission Efficiency ------------------ #
transEfficiency = (len(storeVehWithData)/len(VehAllInSim))*100
print("\nV2V Transmission Range:", transRange, "feet")
print("\nV2V Data Transmission Capacity:", transCap, "vehicles at once")
print("\nDuration of Simulation:", sim_end/(60*1000), "minutes")
print("\nEfficiency of V2V Information Dissemination:", transEfficiency, "percent")
