#datastreaming 2.0

import pandas as pd

PATH_LOAD = "./Data/us101_test.csv"
df = pd.read_csv(PATH_LOAD)

sorted_df = df.sort_values(by=['Global_Time'])

#initialized as the first time in the sorted dataframe
time = sorted_df['Global_Time'][0] # UNIX time based

# sorted_df[sorted_df['Global_Time'] == time]

# below can be used to generate objects

for i in range(0, len(sorted_df)):
    timeStep_df = sorted_df[sorted_df['Global_Time'] == time]
    if(len(timeStep_df) != 0): # loop through the time step dataframe
        time += 100 # update the time step on each iteration
        print(timeStep_df)
    else:
        break
