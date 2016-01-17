"""insolation.py

This module contains general-purpose routines for computing incoming
solar radiation at the top of the atmosphere.

Currently, only daily average insolation is computed.

Ported and modified from MATLAB code daily_insolation.m
Original authors:
    Ian Eisenman and Peter Huybers, Harvard University, August 2006
Available online at http://eisenman.ucsd.edu/code/daily_insolation.m

If using calendar days, solar longitude is found using an
approximate solution to the differential equation representing conservation
of angular momentum (Kepler's Second Law).  Given the orbital parameters
and solar longitude, daily average insolation is calculated exactly
following Berger 1978.

References:
Berger A. and Loutre M.F. (1991). Insolation values for the climate of
 the last 10 million years. Quaternary Science Reviews, 10(4), 297-317.
Berger A. (1978). Long-term variations of daily insolation and
 Quaternary climatic changes. Journal of Atmospheric Science, 35(12),
 2362-2367.
"""
#import sys
#sys.path.append("/Users/minlanxi/Research/01_LAI/respy/")

import numpy as np
import datetime as dt
import calendar
import os
from respy.utils import constants as const

def add_years(datetime,years):
	year  = int(datetime.year + years)
	month = datetime.month
	day   = datetime.day
	hour  = datetime.hour
	return dt.datetime(year,month,day,hour)

def add_months(datetime,months):
    month = datetime.month - 1 + months
    year = int(datetime.year + month / 12 )
    month = month % 12 + 1
    day = min(datetime.day,calendar.monthrange(year,month)[1])
    hour = datetime.hour
    return dt.datetime(year,month,day,hour)
    
def monthdelta(d1, d2):
    delta = 0
    while True:
        mdays = calendar.monthrange(d1.year, d1.month)[1]
        d1 += dt.timedelta(days=mdays)
        if d1 <= d2:
            delta += 1
        else:
            break
    return delta
    
def leap_year(year):
    if year%400==0 or year%4==0 and year%100<>0:
        month = np.array([31,29,31,30,31,30,31,31,30,31,30,31])
    else:
        month = np.array([31,28,31,30,31,30,31,31,30,31,30,31])
    return month
#print leap_year(2012)	

def day_of_year(year,mm,dd):
    #decide if this year is leap year
    month = leap_year(year)
    doy = np.sum(month[0:mm-1])+dd
    return doy

    
def julian2date(year,t):
    month = 0
    day = 0
    hour = (t - int(t))*24
    #print t,int(t)
    minute = (hour - int(hour))*60
    #print minute,hour,int(hour)
    second = (minute - int(minute))*60
    date = int(t)
    mon = leap_year(year)
    
    for i in range(12):
        if date < np.sum(mon[0:i+1]):
            month = i+1 
            day   = date - np.sum(mon[0:i]) + 1
            date  = 999
    #print year,month,day
    #print t,month,year
    dt0 = dt.datetime(np.int(year),np.int(month),np.int(day),np.int(hour),np.int(minute),np.int(second))
    return dt0
    
def date2julian(dt0):
	year   = dt0.year
	month  = dt0.month
	day    = dt0.day
	hour   = dt0.hour
	minute = dt0.minute
	second = dt0.second
	julian = day_of_year(year,month,day)-1+hour/24.+minute/60./24.+second/3600./24.
	return julian
	
#filepath = '/Volumes/Elements/01-RESEARCH/DATA/MOD06/'
#filename = os.listdir(filepath)	

def mod06_time(filename,tzone):
	#print filename
	i = 0
	if filename[0:1]=='._':
		i = 2
	year   = np.int(filename[10+i:14+i])
	doy    = np.int(filename[14+i:17+i])
	hour   = np.int(filename[18+i:20+i]) + tzone
	minute = np.int(filename[20+i:22+i])
	#print year,doy,hour,minute
	t = doy + hour/24. + minute/24./60.
	dt0 = julian2date(year,t)
	return dt0
	
def mod13c1(filename,tzone):
#MOD13C1.A2012177.006.2015247134446
	i = 0
	if filename[0]=='.':
		i = 2
	year   = np.int(filename[9+i:13+i])
	doy    = np.int(filename[13+i:16+i])
	dt0 = julian2date(year,doy)
	return dt0
	
def mod08_time(filename):
	
	year   = np.int(filename[10:14])
	doy    = np.int(filename[14:17])
	#print year,doy,hour,minute
	t = doy
	dt0 = julian2date(year,t)
	return dt0

#print julian2date(2010,234.786)
#fn = 'MOD06_L2.A2010060.0850.006.2015041193542.hdf'
#print modis_time(fn)
    

#print julian2date(2010,80.41666667)
#print julian2date(2010,80.4548611111)
#dt0 = dt.datetime(2010,3,21,11,0,0)
#dt1 = dt.datetime(2010,3,21,10,5,0)
#print date2julian(dt0),date2julian(dt1)
#print modis_time('MOD06_L2.A2010079.1100.006.2015043192310.hdf')