# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 21:21:51 2018

@author: Qicheng

Now is better than never.
"""
import pygame

fps = 100
Size = Len, Wid = 1280,720#1280, 720
RoadPos = 360
RoadWid = 300
LineWid = int(RoadWid/50)
DashNum = 50
#4 lanes

PosY1 = RoadPos-3/8*RoadWid
PosY2 = RoadPos-1/8*RoadWid
PosY3 = RoadPos+1/8*RoadWid
PosY4 = RoadPos+3/8*RoadWid

grey=[128,128,128]
white=[255,255,255]
yellow=[255,255,0]
imgR=pygame.image.load('CarRight.png')
imgL=pygame.image.load('CarLeft.png')

Xborder=10
Yborder=10