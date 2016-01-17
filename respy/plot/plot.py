"""readtxt.py

Object-oriented code for reading formatted txt files.

Code developed by Lanxi Min, University at Albany
lmin@albany.edu

Here is an example to read a list of formatted txt files

""" 

from respy.metadata.metadata import Metadata

import numpy as np
import scipy
from scipy import ndimage
from scipy import interpolate
from scipy.optimize import leastsq

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap,shiftgrid,maskoceans

map_glo = Basemap(projection='mill',llcrnrlon=-180,urcrnrlon=180, \
  	      llcrnrlat=-90,urcrnrlat=90, resolution='c')

map_na  = Basemap(projection='mill',llcrnrlon=-140,urcrnrlon=-40, \
  	  	  llcrnrlat=10,urcrnrlat=60, resolution='l')

class Plot(object):

	def __init__(self,datatype='abstract',grid1=None,grid2=None):
	
		self.meta = Metadata(datatype=datatype)
		self.grid1 = grid1
		self.grid2 = grid2

	def geo_plot(self,maptype,vmin=None,vmax=None,scale=11,shift=False,ocean=False,labelname='Untitled'):
		
		if maptype == 'NA':
			map = map_na
		elif maptype == 'Global':
			map = map_glo
		
		shift = False
		
		datatype = self.meta.datatype
		if datatype == 'era40':
			shift = False
			
		if datatype == 'mod13c2':
			shift = False
			
		if datatype == 'isccp_fd':
			shift = False
	
		if shift == False:
			dt_lon   = self.meta.lon
			dt_lat   = self.meta.lat
			var      = self.grid1	
			varshift = self.grid1			
			lonshift = dt_lon
			
		elif shift == True:
			(varshift,lonshift) = shiftgrid(180,var,dt_lon,start=False,cyclic=360.0)
		
		Lon, Lat = np.meshgrid(lonshift,dt_lat)
		Lon = scipy.ndimage.zoom(Lon,3)
		Lat = scipy.ndimage.zoom(Lat,3)
		x, y = map(Lon,Lat)
		zdata = ndimage.interpolation.zoom(varshift,3)
				
		if ocean == False:
			mdata = zdata
		else:
			mdata = maskoceans(Lon, Lat, zdata,inlands=False)
	
		if vmin == None or vmax == None:       
			cs = map.contourf(x,y,mdata,shading='flat',cmap=plt.cm.seismic)
			map.colorbar(cs,location='bottom',pad="5%",label=labelname)        
		else:
			v = np.linspace(vmin, vmax, scale, endpoint=True)        
			cs = map.contourf(x,y,mdata,v,shading='flat',cmap=plt.cm.seismic)
			map.colorbar(cs,ticks=v,location='bottom',pad="5%",label=labelname)
	
		map.drawcoastlines()
		
	def stream_plot(self, maptype, density = 10., ocean=False,labelname='Untitled'):
	
		if maptype == 'NA':
			map = map_na
		elif maptype == 'Global':
			map = map_glo
			
		dt_lon   = self.meta.lon
		dt_lat   = self.meta.lat
		u = self.grid1
		v = self.grid2
	    
		speed = np.sqrt(u**2 + v**2)
		Lon,Lat = np.meshgrid(dt_lon,dt_lat)
		x, y = map(Lon,Lat)
		mdatau = u
		mdatav = v
		if ocean == True:
			mdatau = maskoceans(Lon, Lat, u,inlands=False)
			mdatav = maskoceans(Lon, Lat, v,inlands=False)
		elif ocean == False:
			mdatau = u
			mdatav = v
		map.streamplot(x,y,mdatau,mdatav,color=-u,linewidth=0.25*u,density=density,cmap=plt.cm.seismic_r)
		map.drawcoastlines()
		#return s_plot
	#plt.figure(figsize=(18,16))    
	#stream_plot(ms,e4_u200_meta.lon,e4_u200_meta.lat,u200_aver,v200_aver,10,False,False)

	def uv_plot(self,maptype, scale_factor=10 ,ocean=False,labelname='Untitled'):
		
		if maptype == 'NA':
			map = map_na
		elif maptype == 'Global':
			map = map_glo
			
		dt_lon   = self.meta.lon
		dt_lat   = self.meta.lat
		u = self.grid1
		v = self.grid2		
		
		Lon, Lat = np.meshgrid(dt_lon,dt_lat)
		x, y = map(Lon,Lat)
		
		if ocean == True:
			mdatau = maskoceans(Lon, Lat, u,inlands=False)
			mdatav = maskoceans(Lon, Lat, v,inlands=False)
		elif ocean == False:
			mdatau = u
			mdatav = v
		# now plot.
		speed = np.sqrt(u**2 + v**2)
		Q = map.quiver(x,y,mdatau,mdatav,scale=scale_factor)
		qk = plt.quiverkey(Q, 1., 1., 20., '1 m/s', labelpos='W')
		map.drawcoastlines()

						
		
			
		
		
		
				 
