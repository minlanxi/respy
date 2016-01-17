"""readtxt.py

Object-oriented code for reading formatted txt files.

Code developed by Lanxi Min, University at Albany
lmin@albany.edu

Here is an example to read a list of formatted txt files

""" 

import numpy as np

class Analysis(object):

	def __init__(self,index=None,field=None):
		
		self.index = index
		self.field_grid = field.grid
		self.dt0 = field.meta.startdate
		self.dt1 = field.meta.enddate
				
	def composite_difference(self):
		
		index_grid = self.index.get_griddata(self.dt0,self.dt1)		
		variable   = self.field_grid	
				
		pos = np.where(index_grid[:] > 0.)
		neg = np.where(index_grid[:] < 0.)
		
		var_p = variable[pos,:,:]
		var_n = variable[neg,:,:]
		
		var_pos = np.mean(var_p[0,:,:,:], axis = 0)
		var_neg = np.mean(var_n[0,:,:,:], axis = 0)
		var_dif = np.subtract(var_pos,var_neg)
		
		return var_dif

						
		
			
		
		
		
				 
