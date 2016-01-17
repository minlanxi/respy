"""readtxt.py

Object-oriented code for reading formatted txt files.

Code developed by Lanxi Min, University at Albany
lmin@albany.edu

Here is an example to read a list of formatted txt files

""" 

import numpy as np

class TemporalAnalysis(Analysis)

	def __init__(self):
	def seasonal(self,3dcoordinate,variable,StartYear=1900,StartMon=1,MonNum=0.
						EndYear=1900.EndMon=1.):
						
		####JJA SUMMER####
		jja = [6,7,8]
		
		if StartYear == EndYear:
			if ((StartMon>=jja[0]) & (EndMon<=jja[2])):
				self.Year == 1.
			else:
				self.Year == 0.
		else:		
			if ((StartMon<=jja[0]) & (EndMon<jja[2])):
				self.Year = EndYear - StartYear
			elif ((StartMon>jja[0]) & (EndMon<jja[2])):
				self.Year = EndYear - StartYear - 1
			elif ((StartMon>jja[0])&(EndMon>=jja[2])):
				self.Year = EndYear - StartYear
			elif ((StartMon<=jja[0])&(EndMon>=jja[2])):
				self.Year = EndYear - StartYear + 1
			
			variable_jja = np.zeroslike(3dcoordinate)
				
			for i in range(Year)
				self.variable_jja[i,:,:] = np.mean(variable[jja[0]-StartMon+i*12,:,:],
												   variable[jja[1]-StartMon+i*12,:,:],
												   variable[jja[2]-StartMon+i*12,:,:])
		

						
		
			
		
		
		
				 
