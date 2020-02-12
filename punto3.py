#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 10:33:53 2020

@author: sebastian
"""


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

trama =  np.array(['A','A','A','B','X','G','H','J','A','X','G','H','J','H','B','B',\
'X','H','J','K','I','A','X','G','J','S','K','D','U','H','D','J','K','S','H','B','X',\
'A','G','D','J','J','F','K','F','A','X','X','A','F','D','G'])
counter = 0
for i in range(0,len(trama)):
    if(i == 51):
        break
    if(trama[i] == 'B' and  trama[i+1] == 'X'):
        for j in range(i+2,len(trama)):
            if(trama[j] == 'A' and  trama[j+1] == 'X'):
                counter += 1
                break

print(counter)   
        