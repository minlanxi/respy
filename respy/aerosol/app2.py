"""Domain.py

Object-oriented code for setting 3D coordinates: Longitude, Latitude, Pressure, Height.

Code developed by Lanxi Min, University at Albany
lmin@albany.edu

Here is an example to set 3D coordinates

""" 
import sys
sys.path.append("/Users/minlanxi/Research/01_LAI/respy/")


import numpy as np
import respy
from respy.aerosol import aerosol
import os
import time

#pos0 = respy.spatial.deg2decimal(24,17,16.25)
#pos1 = respy.spatial.deg2decimal(61,50,36.73)
#pos = [pos0,pos1]
			
#filepath1 = '/Volumes/Elements/01-RESEARCH/DATA/MOD06/'
filepath1 = '/Volumes/DATA/MOD06_L2_2009_Spring/'
filename1 = os.listdir(filepath1)	
tlist = []
filelen1 = len(filename1)
doy = np.zeros(filelen1)
filelen1 = len(filename1)
for i in range(filelen1):
	dt0 = respy.temporal.mod06_time(filename1[i],2.)
	doy[i] = respy.temporal.date2julian(dt0)
	tlist.append(dt0)
np.savetxt('tlist_doy_2009.txt',doy)


filepath = '/Users/minlanxi/Desktop/Fall_2015/ATM515/Final_Project/PSD/'
filename = os.listdir(filepath)
npf,ccn = aerosol.daily_ccn(filepath,filename,tlist)

#N100 = aerosol.monthly_ccn(filepath,filename)
		
	
        