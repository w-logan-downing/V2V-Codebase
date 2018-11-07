# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 10:25:26 2018

@author: Qicheng

Now is better than never.
"""

import pygame
import numpy as np
from constant import *

class Background:
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        self.screen.fill(white)
        '''
        pygame.draw.line(self.screen, grey, (0, RoadPos), (Len, RoadPos), RoadWid)
        # draw lines
        pygame.draw.line(self.screen, yellow, (0, RoadPos), (Len, RoadPos), LineWid)
        for y in [RoadPos+1/4*RoadWid, RoadPos-1/4*RoadWid]:
            DashLine = np.linspace(0, Len, DashNum)
            for n in range(len(DashLine)-1):
                if n/2 == n//2:
                    x = DashLine[n]
                    x1 = DashLine[n+1]
                    pygame.draw.line(self.screen, yellow,(x, y), (x1, y), LineWid)
                else:
                    continue
        '''
        
class Car:
    def __init__(self, screen, cid=1, color = imgR, direction=1, speed=20, x=10, y=390):
        self.screen = screen
        self.cid = cid
        self.color = color
        self.direction = direction
        self.speed = speed
        self.x = x
        self.y = y

    def draw(self,RangeXY):
        drawX=(Len-2*Xborder)*(self.x-RangeXY[0])/(RangeXY[1]-RangeXY[0])+Xborder
        drawY=(Wid-2*Yborder)*(self.y-RangeXY[2])/(RangeXY[3]-RangeXY[2])+Yborder
        self.screen.blit(self.color, (drawX, drawY))


        
        


