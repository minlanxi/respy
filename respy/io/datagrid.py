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

import numpy as np
from respy.io.input import Read	

class DataGrid(object):
	
	def __init__(self,metadata=None):
		self.metadata = metadata
		datafile  = Read(metadata)
		if metadata.mulfiles = True:
			self.DataArr = datafile.Readfiles()
		elif metadata.mulfiles = False:
			self.DataArr = datafile.Readfile()
		
	def to_grid(self):
		# Transfer DataArr to formed numpy grid data
		DataArr   = self.DataArr
		DataShape = self.DataArr.shape
		LonShape  = self.metadata.lon.shape[0]
		LatShape  = self.metadata.lat.shape[0]
		LevShape  = self.metadata.lev.shape[0] 
				
		YearShape = self.metadata.year.shape[0]
		StartDate = self.metadata.startdate
		EndDate   = self.metadata.enddate
		
		if DataShape.shape == 1:		
			try:
				DataArr.shape[0] = LatShape * LonShape * LevShape * MonShape
			except:
				raise ValueError('DataArr data does not match the formed grid.')		
			return _file_to_grid(DataArr,LatShape,Lonshape,LevShape,StartDate,EndDate)
		
		elif DataShape.shape == 2:
			try:
				DataArr.shape[0] = LatShape * LonShape * LevShape * YearShape * MonShape
			except:
				raise ValueError('DataArr data does not match the formed grid.')		
			return _files_to_grid(DataArr,LatShape,Lonshape,LevShape,YearShape,MonShape)			
		
def _file_to_grid(DataArr,LatShape,Lonshape,LevShape,StartDate,EndDate):
	
	YearLen = int(EndDate[0:4]) - int(StartDate[0:4])
	MonLen  = int(EndDate[4:6]) - int(StartDate[4:6])
	TShape  = YearLen * 12 + MonLen + 1 
	
	cutoff   = 12 - StartDate[4:6] + 1
	MonGrid  = np.reshape(Tshape,LatShape,Lonshape)[cutoff:Tshape,:,:]
	DataGrid = np.zeros((YearLen+1,LatShape,Lonshape))
	#select JJA data
	for i in range(YearLen+1):
		DataGrid[i,:,:] = np.mean([MonGrid[[5+i*12],:,:],MonGrid[[6+i*12],:,:],
                                   MonGrid[[7+i*12],:,:]], axis = 0)

	return DataGrid

def _files_to_grid(DataArr,LatShape,Lonshape,LevShape,YearShape,MonShape):

	if metadata.Mon == '':
		DataGrid = DataArr.reshape(YearShape,LatShape,Lonshape)
	else:
		DataTemp = DataArr.reshape(YearShape,MonShape,LatShape,Lonshape)
		DataGrid = np.nanmean(DataTemp,axis=1)
		del DataTemp
	
	return DataGrid		

	

	
#class ReadFile(Read):

#class ReadIndex(Read):

#Path = ReadFormattedData(Prefix = 'test')
#print Path.ReadFile()