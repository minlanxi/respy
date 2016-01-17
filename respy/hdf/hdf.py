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
from respy.utils import spatial
import os
import time

#filepath = '/Users/minlanxi/Desktop/'
#filename = ['MOD06_L2.A2010060.0850.006.2015041193542.hdf']

def MOD06_L2(filepath,filename,pos):
	
	filelen  = len(filename)	
	hdf = SD(filepath+filename[0], SDC.READ)
	lat = hdf.select('Latitude')
	lon = hdf.select('Longitude')
	lat0 = lat[:,:]
	lon0 = lon[:,:]
	latnew = respy.spatial.grid_interpolate(lat0,[2030,1354])
	lonnew = respy.spatial.grid_interpolate(lon0,[2030,1354])
	
	B=(3.14*4.*10e5/3.)**(-1.)*(2.*2.*1e-4)**(-0.25)

	cf_pos   = np.zeros(filelen)
	ctp_pos  = np.zeros(filelen)
	cpi_pos  = np.zeros(filelen)

	cwp_5km  = np.zeros(filelen)
	cre_5km  = np.zeros(filelen)
	cot_5km  = np.zeros(filelen)
	cdn_5km  = np.zeros(filelen)
	
	cwp_2deg = np.zeros(filelen)
	cre_2deg = np.zeros(filelen)
	cot_2deg = np.zeros(filelen)
	cdn_2deg = np.zeros(filelen)
	cf_2deg  = np.zeros(filelen)
	ctp_2deg = np.zeros(filelen)
	cpi_2deg = np.zeros(filelen)


	for i in range(filelen):

		start_time = time.time()
		hdf = SD(filepath+filename[i], SDC.READ)
	
		cwp = hdf.select('Cloud_Water_Path') #1km
		cre = hdf.select('Cloud_Effective_Radius') #1km
		cot = hdf.select('Cloud_Optical_Thickness') #1km	
		cf  = hdf.select('Cloud_Fraction')
		ctp = hdf.select('Cloud_Top_Pressure') 
		cpi = hdf.select('Cloud_Phase_Infrared')
	

	############################################################################
	#   Collation of modis and insitu measurement
	############################################################################		

		#cwp_pos[i],loc1 = respy.spatial.collocate2d(latnew,lonnew,cwp[:,:],pos)
		#cf_pos[i],loc5  = respy.spatial.collocate2d(lat0,lon0,cf[:,:],pos)
		loc1 = [594,98]
		loc5 = [120,20]
		
		cwp_2deg[i] = respy.spatial.domian_mean(latnew,lonnew,cwp[:,:],pos,2)
		cre_2deg[i] = respy.spatial.domian_mean(latnew,lonnew,cre[:,:],pos,2)
		cot_2deg[i] = respy.spatial.domian_mean(latnew,lonnew,cot[:,:],pos,2)
		cdn_2deg[i] = 1.11*((cot_2deg[i]*0.01)/(7.54*B**(0.66667)*(cwp_2deg[i])**(0.8333)))**(3)		
		cf_2deg[i]  = respy.spatial.domian_mean(lat0,lon0,cf[:,:], pos,2)
		ctp_2deg[i] = respy.spatial.domian_mean(lat0,lon0,ctp[:,:],pos,2)
		cpi_2deg[i] = respy.spatial.domian_mean(lat0,lon0,cpi[:,:],pos,2)
		
		cf_pos[i]  = cf[:,:][loc5[0],loc5[1]]
		ctp_pos[i] = ctp[:,:][loc5[0],loc5[1]]
		cpi_pos[i] = cpi[:,:][loc5[0],loc5[1]]
	
	#############################################################################
	#   Calculating 5km*5km Regional Mean CWP from 1km*1km point 
	#############################################################################

		flag = 0
		for m in range(5*2):
			for n in range(5*2):
				if cwp[:,:][loc1[0]-5+m,loc1[1]-5+n] != -9999:
					cwp_5km[i] += cwp[:,:][loc1[0]-5+m,loc1[1]-5+n]
					cre_5km[i] += cre[:,:][loc1[0]-5+m,loc1[1]-5+n]
					cot_5km[i] += cot[:,:][loc1[0]-5+m,loc1[1]-5+n]
					flag += 1
		if flag == 0:
			cwp_5km[i] = -9999
			cre_5km[i] = -9999
			cot_5km[i] = -9999
			cdn_5km[i] = -9999
		else:
			cwp_5km[i] /= flag
			cre_5km[i] /= flag
			cot_5km[i] /= flag
			cdn_5km[i]  = 1.11*((cot_5km[i]*0.01)/(7.54*B**(0.66667)*(cwp_5km[i])**(0.8333)))**(3)	
			
	##############################################################################
	
		
		print cwp_5km[i]*0.001,cre_5km[i]*0.01,cot_5km[i]*0.01,cdn_5km[i]*0.00001,filename[i]
		print cwp_2deg[i]*0.001,cdn_2deg[i]*0.00001
		print("--- %s seconds ---" % (time.time() - start_time))
	##############################################################################
	#   Write HDF File
	##############################################################################
	'''	# Create an HDF file
		sd = SD(filename[i][0:22]+'.ATM515.hdf', SDC.WRITE | SDC.CREATE)

		# Create a dataset
		sds = sd.create('lat', SDC.FLOAT64, (270, 406))
		# Fill the dataset with a fill value
		sds.setfillvalue(-9999)
		# Write data
		sds[:] = lat0
		# Close the dataset
		sds.endaccess()	
		print filepath+filename[i][0:22]+'.ATM515.hdf'+' done'

		# Flush and close the HDF file
		sd.end()
		'''
	#######################################################################################
	varlist1 = np.vstack((cwp_5km*0.001,  cre_5km*0.01, cot_5km*0.01, cdn_5km*0.00001, cf_pos*0.01, ctp_pos*0.1))
	varlist2 = np.vstack((cwp_2deg*0.001,cre_2deg*0.01,cot_2deg*0.01,cdn_2deg*0.00001,cf_2deg*0.01,ctp_2deg*0.1))
	np.savetxt('varlist_daily_5km.txt',varlist1)
	np.savetxt('varlist_daily_2deg.txt',varlist2)
	return varlist1,varlist2
	
def MOD08_M3(filepath,filename,pos):
	start_time = time.time()

	filelen  = len(filename)
	tlist    = []
	
	hdf = SD(filepath+filename[0], SDC.READ)
	lat = hdf.select('YDim')
	lon = hdf.select('XDim')
	lon0,lat0 = np.meshgrid(lon[:],lat[:])
	B=(3.14*4.*1e5/3.)**(-1.)*(2.*2.*1e-4)**(-0.25)

	sza_pos  = np.zeros(filelen)
	cwp_pos  = np.zeros(filelen)
	cre_pos  = np.zeros(filelen)
	cot_pos  = np.zeros(filelen)
	cdn_pos  = np.zeros(filelen)
	icwp_pos = np.zeros(filelen)
	icre_pos = np.zeros(filelen)
	icot_pos = np.zeros(filelen)
	icdn_pos = np.zeros(filelen)
	
	cf_pos   = np.zeros(filelen)
	ctp_pos  = np.zeros(filelen)

	loc = [28,204]
	for i in range(filelen):
		dt0 = respy.temporal.mod08_time(filename[i])
		tlist.append(dt0)

		start_time = time.time()
		hdf = SD(filepath+filename[i], SDC.READ)
		
		sza  = hdf.select('Solar_Zenith_Mean_Mean')
		cwp  = hdf.select('Cloud_Water_Path_Liquid_Mean_Mean') 
		cre  = hdf.select('Cloud_Effective_Radius_Liquid_Mean_Mean') 
		cot  = hdf.select('Cloud_Optical_Thickness_Liquid_Mean_Mean') 	
		icwp = hdf.select('Cloud_Water_Path_Ice_Mean_Mean') 
		icre = hdf.select('Cloud_Effective_Radius_Ice_Mean_Mean') 
		icot = hdf.select('Cloud_Optical_Thickness_Ice_Mean_Mean') 
		
		cf   = hdf.select('Cloud_Fraction_Mean_Mean')
		ctp  = hdf.select('Cloud_Top_Pressure_Mean_Mean')

	############################################################################
	#   Collation of modis and insitu measurement
	############################################################################		
		sza_pos[i] = sza[:,:][loc[0],loc[1]]
		cwp_pos[i] = cwp[:,:][loc[0],loc[1]]
		cre_pos[i] = cre[:,:][loc[0],loc[1]]
		cot_pos[i] = cot[:,:][loc[0],loc[1]]
		icwp_pos[i] = icwp[:,:][loc[0],loc[1]]
		icre_pos[i] = icre[:,:][loc[0],loc[1]]
		icot_pos[i] = icot[:,:][loc[0],loc[1]]

		#cdn_pos[i] = 1.11*((cot_pos[i]*0.01)/(7.54*B**(0.66667)*(cwp_pos[i])**(0.8333)))**(3)
		cf_pos[i]  = cf[:,:][loc[0],loc[1]]
		ctp_pos[i] = ctp[:,:][loc[0],loc[1]] 
		cdn_pos[i] = 2**(-2.5)/0.8*(cot_pos[i]*0.01)**(3.)*(cwp_pos[i]*0.001)**(-2.5)*(0.6*np.pi*2.)**(-3.)*(3./4./np.pi/1000)**(-2.)*(1.6*1e-6)**(0.5)
		icdn_pos[i] = 2**(-2.5)/0.8*(icot_pos[i]*0.01)**(3.)*(icwp_pos[i]*0.001)**(-2.5)*(0.6*np.pi*2.)**(-3.)*(3./4./np.pi/1000)**(-2.)*(1.6*1e-6)**(0.5)
		#print cdn_pos[i]/cdn_pos1,i,cdn_pos[i],cdn_pos1
		#cdn_pos[i] = (1.6*1e-6)**(0.5)/0.8*10**(0.5)/4./np.pi/(1000)**(0.5)*(cot_pos[i]*0.01)**(0.5)/(cre_pos[i]*0.01*1e-6)**(2.5)
		print filename[i]+' done'
		
	varlist  = np.vstack((sza_pos*0.01,cwp_pos*0.001,cre_pos*0.01,cot_pos*0.01,cdn_pos*1e-6,cf_pos*1e-5,ctp_pos*0.1))
	ivarlist = np.vstack((sza_pos*0.01,icwp_pos*0.001,icre_pos*0.01,icot_pos*0.01,icdn_pos*1e-6))
	np.savetxt('varlist.txt',varlist)
	np.savetxt('ivarlist.txt',ivarlist)
	print("--- %s seconds ---" % (time.time() - start_time))
	return varlist,tlist	
	
def MOD13C1(filepath,filename):
	EVI_TOTAL  = []
	start_time = time.time()

	filelen  = len(filename)
	tlist    = []

	lon = -180.+np.arange(7200)/20.
	lat =   90.-np.arange(3600)/20.
	
	longrid,latgrid = np.meshgrid(lon[:],lat[:])
	
	lat0,lon0 = spatial.collocate(lat,lon,[60,-140])
	lat1,lon1 = spatial.collocate(lat,lon,[10,-40])
	print lon0,lon1,lat0,lat1
	print lon[lon0],lon[lon1],lat[lat0],lat[lat1]
	
	j = 0

	for i in range(filelen):
		dt0 = respy.temporal.mod13c1(filename[i],0)
		tlist.append(dt0)

		start_time = time.time()
		hdf  = SD(filepath+filename[i], SDC.READ)
		NDVI = hdf.select('CMG 0.05 Deg 16 days NDVI')
		EVI  = hdf.select('CMG 0.05 Deg 16 days EVI')

	############################################################################
	#   Collation of modis and insitu measurement
	############################################################################		
		NDVI_NA = NDVI[:,:][lat0:lat1,lon0:lon1]
		EVI_NA  =  EVI[:,:][lat0:lat1,lon0:lon1]
		print lon0,lon1,lat0,lat1
		print EVI_NA.shape
		#if (j <= 7):
		#	EVI_TOTAL.append(EVI_NA)
		#	j = j + 1
		print filename[i]+' done'
		#else:
			#EVI_ARR = np.vstack(EVI_TOTAL)
			#EVI_ARR.astype(float)
			#EVI_ARR[EVI_ARR==-3000] = np.nan
			#EVI_MEAN = np.nanmean(EVI_ARR, axis=0)
			#print EVI_MEAN.shape
		np.savetxt('/Volumes/DATA/'+'EVI_NA'+filename[i]+'.txt',EVI_NA)
			#EVI_TOTAL = []
			#EVI_TOTAL.append(EVI_NA)
			#EVI_ARR = np.vstack(EVI_TOTAL)
		
	#varlist  = np.vstack((sza_pos*0.01,cwp_pos*0.001,cre_pos*0.01,cot_pos*0.01,cdn_pos*1e-6,cf_pos*1e-5,ctp_pos*0.1))
	#ivarlist = np.vstack((sza_pos*0.01,icwp_pos*0.001,icre_pos*0.01,icot_pos*0.01,icdn_pos*1e-6))
	
	print("--- %s seconds ---" % (time.time() - start_time))
	#
	return EVI_NA.shape
	#varlist,tlist	

		
#filepath1 = '/Volumes/DATA/MODC13/'
#filename1 = os.listdir(filepath1)
#MOD13C1(filepath1,filename1)
	
