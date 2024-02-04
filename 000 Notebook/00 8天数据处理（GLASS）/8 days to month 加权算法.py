# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 16:50:06 2022

@author: MaYutong
"""

import netCDF4 as nc
import numpy as np
import pandas as pd
import xlsxwriter

df = pd.read_excel('E:/ERA5/每月天数.xlsx')
days = df['平年2']
days[12] = 365

t = np.arange(1, 365, 8)

code=xlsxwriter.Workbook('加权算法.xlsx')
content=code.add_worksheet("data")

for i in range(12):
    if i<11:
        ind = np.logical_and(t>days[i], t<days[i+1])
    else:
        ind = t>days[i]
        
    a = t[ind]
    t_str = []
    [t_str.append(str(x).zfill(3)) for x in a]
    t_str.insert(0, days[i])
    t_str.append(days[i+1])
    t_str = list(map(int, t_str)) 
    print("\n", t_str, "\n")
    for j, x in enumerate(t_str):
        content.write(j+1, i, x)
    
code.close()
