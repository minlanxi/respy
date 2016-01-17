"""readtxt.py

Object-oriented code for reading formatted txt files.

Code developed by Lanxi Min, University at Albany
lmin@albany.edu

Here is an example to read a list of formatted txt files

rff = ReadFormattedFile(StrPath = 'dat/',
						Prefix  = 'dataset',
						Suffix  = '.txt')
rff.ReadFile()


""" 
import sys
sys.path.append("/Users/minlanxi/Research/01_LAI/respy/")

import numpy as np
from respy.io.input import Read

class DataGrid(object):
	
	def __init__(self,metadata=None):
		self.metadata = metadata
		datafile  = Read(metadata)
		if metadata.mulfile == True:
			self.DataArr = datafile.ReadFiles()
		elif metadata.mulfile == False:
			self.DataArr = datafile.ReadFile()
		
	def index_to_grid(self):

		index_all = np.loadtxt(self.metadata.filepath+self.metadata.filename)
		#select interest year from date column
		#for instance, QBO[:,0] is date column
		startyear = self.metadata.startdate.year
		endyear = self.metadata.enddate.year
		index = index_all[np.where((index_all[:,0]>=startyear) & (index_all[:,0]<=endyear))]
		index_jja = np.mean([index[:,5],index[:,6],index[:,7]],axis = 0)
		return index_jja
	
	def field_to_grid(self):
		# Transfer DataArr to formed numpy grid data
		DataArr   = self.DataArr
		LonShape  = self.metadata.lon.shape[0]
		LatShape  = self.metadata.lat.shape[0]
		LevShape  = self.metadata.lev.shape[0] 
	
		StartDate = self.metadata.startdate
		EndDate   = self.metadata.enddate
		DateList  = self.metadata.datelist
		TempRes   = self.metadata.temporal_res
		
		if len(DataArr.shape) == 1:		
			try:
				1 > 0
			except:
				raise ValueError('DataArr data does not match the formed grid.')		
			return _file_to_grid(DataArr,LatShape,LonShape,LevShape,StartDate,EndDate,DateList)
		
		elif len(DataArr.shape) == 2:
			try:
				1 > 0
			except:
				raise ValueError('DataArr data does not match the formed grid.')		
			return _files_to_grid(DataArr,LatShape,LonShape,LevShape,DateList,TempRes)			
		
def _file_to_grid(DataArr,LatShape,Lonshape,LevShape,StartDate,EndDate,DateList):
        
	YearLen = int(EndDate.year) - int(StartDate.year) + 1
	Tshape  = len(DateList) 
	
	cutoff   = 0
	print DataArr.shape,Tshape,LatShape,Lonshape
	MonGrid  = DataArr.reshape(Tshape,LatShape,Lonshape)[cutoff:Tshape,:,:]
	
	DataGrid = np.zeros((YearLen,LatShape,Lonshape))
	
	#select JJA data
	print YearLen
	for i in range(YearLen):
	    DataGrid[i,:,:] = np.mean([MonGrid[[5+i*12],:,:],MonGrid[[6+i*12],:,:],
                            MonGrid[[7+i*12],:,:]], axis = 0)
	return DataGrid
	


def _files_to_grid(DataArr,LatShape,Lonshape,LevShape,DateList,TempRes):

	if TempRes == 'Yearly':
	        YearShape = len(DateList)
		DataGrid = DataArr.reshape(YearShape,LatShape,Lonshape)
	else:
	        MonShape = 3
		DataTemp = DataArr.reshape(YearShape,MonShape,LatShape,Lonshape)
		DataGrid = np.nanmean(DataTemp,axis=1)
		del DataTemp
	
	return DataGrid		
	
#class ReadFile(Read):

#class ReadIndex(Read):

#Path = ReadFormattedData(Prefix = 'test')
#print Path.ReadFile()