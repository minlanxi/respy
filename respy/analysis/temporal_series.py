"""Datastructure.py

Object-oriented code for setting 3D coordinates: Longitude, Latitude, Pressure, Height.

Code developed by Lanxi Min, University at Albany
lmin@albany.edu

Here is an example to set 3D coordinates

""" 

import numpy as np
from respy.io.formatted import ReadFormattedData

data_types = ['era40','erai','ncep','isccp_fd','ceres','mod13c2','abstract']

class PreProcessing(object)

	def __init__(self, input_grid, metadata, Analysis_Trange, temporal_type):      
			 
	def preprocess(self):
				
		Tstart, Tend = convert_t()
		
		var_arr = self.DataArr
		
		var_mon = var_txt.reshape(datashape)[Tstart:Tend,:,:]
		
		Yrange = np.int(self.SpecTrange[1][0:4] - np.int(self.SpecTrange[0][0:4]) + 1
		
		#compute summer average JJA
		var_jja = np.zeros((Yrange,lat.shape[0],lon.shape[0]))
		for i in range(Yrange):
			var_jja[i,:,:] = np.mean([var_mon[[5+i*12],:,:],var_mon[[6+i,:,:],:,:],
									  var_mon[[7+i*12],:,:], axis = 0)		
		return var_jja
		
		
def truncate_t():
	
	datasetTrange = self.dataset_info['temporal_range']
	
	Tstart_year = np.int(self.SpecTrange[0][0:4]) - np.int(datasetTrange[0][0:4])
	Tstart_mon   = np.int(self.SpecTrange[0][4:6]) - np.int(datasetTrange[0][4:6])
	
	Tend_year = np.int(self.SpecTrange[1][0:4]) - np.int(datasetTrange[1][0:4])
	Tend_mon   = np.int(self.SpecTrange[1][4:6]) - np.int(datasetTrange[1][4:6])
	
	if Tstart_mon < 0:
		Tstart_mon  = 12 - Tstart_mon
		Tstart_year = Tstart_year - 1
		
	if Tend_mon < 0:
		Tend_mon  = 12 - Tend_mon
		Tend_year = Tend_year - 1
	
	Tstart = Tstart_mon + Tstart_year * 12
	Tend   = Tend_mon   + Tend_year * 12
	
	return Tstart,Tend	
		
