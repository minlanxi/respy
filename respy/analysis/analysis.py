"""readtxt.py

Object-oriented code for reading formatted txt files.

Code developed by Lanxi Min, University at Albany
lmin@albany.edu

Here is an example to read a list of formatted txt files

""" 

import numpy as np

class Analysis(object)

	def __init__(self):
		self.variables = DataStructure()
		self.Ystart    = np.int(self.SpecTrange[0][0:4])
		self.Yend      = np.int(self.SpecTrange[1][0:4])
		self.Index     = DataStructure()
	

		
	def composite_difference(Index, variable):
				
		pos = np.where(Index[ystart-1948:Yend+1-1948] > 0.)
		neg = np.where(Index[ystart-1948:yend+1-1948] < 0.)
		
		var_p = var[pos,:,:]
		var_n = var[neg,:,:]
		
		var_pos = np.mean(var_p[0,:,:,:], axis = 0)
		var_neg = np.mean(var_n[0,:,:,:], axis = 0)
		var_dif = np.substract(var_pos,var_neg)
		
		return var_dif

						
		
			
		
		
		
				 
