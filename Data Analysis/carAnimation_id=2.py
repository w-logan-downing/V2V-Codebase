import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation as animation

PATH_LOAD = "us-101.csv"
df = pd.read_csv(PATH_LOAD)
dfID2 = df[df['Vehicle_ID'] == 2]

xList = dfID2['Local_X'].tolist()
yList = dfID2['Local_Y'].tolist()

fig = plt.figure()

x= [0] # start point
y= [0]

count = len(dfID2)

def _update_plot(i, fig, scat):
    scat.set_offsets(([xList[i],yList[i]]))
    print('Frames: %d' %i)
    return scat,


ax= fig.add_subplot(111)
ax.grid(True, linestyle = '-', color = '0.75')
ax.set_xlim([0, 50])
ax.set_ylim([0, 2500])

scat = plt.scatter(x, y)
scat.set_alpha(0.8)

anim = animation.FuncAnimation(fig, _update_plot,fargs = (fig, scat), frames =count, interval =50)

plt.show()
