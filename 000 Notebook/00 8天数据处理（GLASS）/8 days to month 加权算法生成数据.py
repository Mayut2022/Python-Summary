# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 11:33:45 2022

@author: MaYutong
"""

import netCDF4 as nc
import numpy as np
import pandas as pd


def read_data(yr, mn):
    inpath = (f"E:/GLASS-ET/AVHRR/{yr}/Glass_ET_{yr}_month{mn}.nc")
    with nc.Dataset(inpath) as f:
        f=nc.Dataset(inpath, mode='r')
        #print(f.variables.keys())
        et=(f.variables['ET'][:])
    
    return et
    


#%%
def month_weighted(et, t):
    t = t.dropna(axis=0)
    if len(t) == 5:
        et_mn = et[0, :, :]*(t[1]-t[0])+\
                et[2, :, :]*(t[4]-t[3])+\
                (et[0, :, :]+et[1, :, :])*(t[2]-t[1])/2+\
                (et[1, :, :]+et[2, :, :])*(t[3]-t[2])/2
    elif len(t) == 6:
        et_mn = et[0, :, :]*(t[1]-t[0])+\
                et[3, :, :]*(t[5]-t[4])+\
                (et[0, :, :]+et[1, :, :])*(t[2]-t[1])/2+\
                (et[1, :, :]+et[2, :, :])*(t[3]-t[2])/2+\
                (et[2, :, :]+et[3, :, :])*(t[4]-t[3])/2
            
    return et_mn

def scalar(et):
    #### 1 w/m^2 = 0.0352653 mm/day
    et = et*0.0352653
    return et
    
def CreatNC(yr, mn, data):
    new_NC = nc.Dataset(rf"E:/GLASS-ET/AVHRR/{yr}/Glass_ET_{yr}_month{mn}_weighted_africa.nc", 'w', format='NETCDF4')
    
    new_NC.createDimension('lat', 1440)
    new_NC.createDimension('lon', 1401)
    
    var=new_NC.createVariable('ET', 'f', ("lat","lon"))
    
    new_NC.variables['ET'][:]=data
        
    var.units = "mm/day (已换算 1 w/m^2 = 0.0352653 mm/day)"
    var.lat = "lat = np.linspace(36.975, -34.975, 1440)"
    var.lon = "lon = np.linspace(-18, 52, 1401)"
    
    #最后记得关闭文件
    new_NC.close()

#%%
df = pd.read_excel('加权算法.xlsx')
df.columns = np.arange(1, 13, 1)
year = np.arange(1982, 2019, 1)
month = np.arange(1, 13, 1)
for yr in year:
    for mn in month:
        t = df[mn]
        print(yr, mn, "\n", t, "\n")
        et = read_data(yr, mn)
        et = month_weighted(et, t)
        et = scalar(et)
        CreatNC(yr, mn, et)
        print(f"{yr} {mn} is done! \n")
        

