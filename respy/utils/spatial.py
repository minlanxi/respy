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
import sys
sys.path.append("/Users/minlanxi/Research/01_LAI/respy/")

import numpy as np
from scipy import interpolate
from respy.utils import constants as const

def deg2decimal(deg,min,sec):
	decimal = deg + min/60. + sec/3600.
	return decimal
	
def collocate(lat,lon,pos):
	lat_pos = pos[0]
	lon_pos = pos[1]
	
	lon_clo = (np.abs(lon - lon_pos)).argmin()
	lat_clo = (np.abs(lat - lat_pos)).argmin()
	return lat_clo,lon_clo

def collocate1d(lat,lon,grid,pos):
	lat_pos = pos[0]
	lon_pos = pos[1]
	
	lon_clo = (np.abs(lon - lon_pos)).argmin()
	lat_clo = (np.abs(lat - lat_pos)).argmin()
	#print lon_clo,lat_clo   #,lon[lon_clo],lat[lat_clo]
	grid_col = grid[:,lat_clo,lon_clo]
	return grid_col,lat_clo,lon_clo
	
def collocate2d(lat,lon,grid,pos):
	lon_pos = pos[0]
	lat_pos = pos[1]
	
	delpos  = np.zeros_like(lat)
	
	for i in range(lon.shape[0]):
		for j in range(lon.shape[1]):
			delpos[i,j] = (lon[i,j] - lon_pos)**2 + (lat[i,j] - lat_pos)**2

	collocation = np.unravel_index(delpos.argmin(), delpos.shape)
#	print collocation,lon[collocation[0],collocation[1]],lat[collocation[0],collocation[1]]	
	grid_col = grid[collocation[0],collocation[1]]	
	return grid_col,[collocation[0],collocation[1]]
    
def grid_interpolate(grid,newshape):  
    
    x = np.arange(0,grid.shape[0],1)
    y = np.arange(0,grid.shape[1],1)
    #print x.shape, y.shape, grid.shape
    f = interpolate.interp2d(y,x,grid,kind='cubic')
    xscale = np.float(grid.shape[0])/np.float(newshape[0])
    yscale = np.float(grid.shape[1])/np.float(newshape[1])
    xnew = np.arange(0,grid.shape[0],xscale)
    ynew = np.arange(0,grid.shape[1],yscale)

    gridnew = f(ynew,xnew)
    return gridnew
    
def deresolution(grid,scale,nanval=-9999):
	grid_new = np.zeros([grid.shape[0]/scale,grid.shape[1]/scale])
	flag     = np.zeros_like(grid_new)
	for i in range(grid.shape[0]/scale):
		for j in range(grid.shape[1]/scale):			
			for h in range(scale):
				for k in range(scale):
					if grid[scale*i+h,scale*j+k] != nanval:
						grid_new[i,j] += grid[scale*i+k,scale*j+k]
						flag[i,j]     += 1
			if flag[i,j] == 0:
				grid_new[i,j] = nanval
			else:
				grid_new[i,j] /= np.float(flag[i,j])
	return grid_new

def domian_mean(lat,lon,grid,pos,size):
	#print lon.shape,grid.shape
	flag = 0
	grid_mean = 0
	for i in range(lon.shape[0]):
		for j in range(lon.shape[1]):
			if (lon[i,j]<=pos[0]+size/2. and lon[i,j]>=pos[0]-size/2.) and (lat[i,j]<=pos[1]+size/2. and lat[i,j]>=pos[1]-size/2.):
				#print lon[i,j],lat[i,j]
				if grid[i,j] != -9999:
					grid_mean += grid[i,j]
					flag += 1
					#print grid[i,j]
	if flag == 0:
		grid_mean = -9999
	else:
		#print grid_mean,flag
		grid_mean /= np.float(flag)
	return grid_mean

	

				
    

