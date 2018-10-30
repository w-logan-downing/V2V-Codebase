#datastreaming 2.0

import pandas as pd

PATH_LOAD = "./Data/us101_test.csv"
df = pd.read_csv(PATH_LOAD)

sorted_df = df.sort_values(by=['Global_Time'])


time = '49:39.7'

sorted_df.Vehicle_ID.dtype

'''
for i in range(0, len(sorted_df)):
    print(sorted_df.iloc[i, :])
'''

sorted_df["Global_Time"][0]

