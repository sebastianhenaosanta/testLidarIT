#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 10:35:13 2020

@author: sebastian
"""
import numpy as np

#function to generate the array of bins depending of the number of  the step space in degress
def ArrayDegbeamns(numBins,spaci):
    a = np.ones(numBins)
    count = 0
    for i in range(0,len(a)):
        if(i == int(len(a)/2)):
            a[i] = -1
            count = 4
        if i < int(len(a)/2):
            a[i] = a[i] + count
            count += spaci 
        elif i > (int(len(a)/2)):
            a[i] = a[i] - count 
            #print(a[i])
            count += spaci
    return a
#This function find the distance from the target point on a plane parallel to Z-axis
def distanceF(d, thetaVD):
    dist = (((d)/np.cos(np.deg2rad(thetaVD))))
    return dist
#final distance
distF = (distanceF(10,ArrayDegbeamns(16,2)))
np.savetxt('vectorDg.txt', ArrayDegbeamns(16,2), delimiter=',')
print(distF)



    