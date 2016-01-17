"""Domain.py

Object-oriented code for setting 3D coordinates: Longitude, Latitude, Pressure, Height.

Code developed by Lanxi Min, University at Albany
lmin@albany.edu



""" 
import sys
sys.path.append("/Users/minlanxi/Research/01_LAI/respy/")

from pyhdf.SD import *
import numpy as np
import respy
import os
import time

#filepath = '/Users/minlanxi/Desktop/'
#filename = ['MOD06_L2.A2010060.0850.006.2015041193542.hdf']

filepath1 = '/Volumes/Elements/01-RESEARCH/DATA/MOD08/'
filename1 = os.listdir(filepath1)
pos0 = respy.utils.spatial.deg2decimal(24,17,16.25)
pos1 = respy.utils.spatial.deg2decimal(61,50,36.73)
pos = [pos0,pos1]

#varlist,tlist = respy.hdf.MOD06_L2(filepath1,filename1,pos)
varlist,tlist = respy.hdf.MOD08_M3(filepath1,filename1,pos)
	
