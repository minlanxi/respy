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
#from respy.metadata.metadata import Metadata


class ReadFiles(object):

	def __init__(self, YLen = 4, metadata = None,
					   StrPath = '', Prefix = '', Suffix = '', **kwargs):
					   
		self.Year    = metadata.year
		self.Mon     = metadata.month
		self.Day     = metadata.day
		self.Hour    = metadata.hour
		
		self.YLen    = YLen
		self.StrPath = StrPath
		self.Prefix  = Prefix
		self.Suffix  = Suffix

	def ReadFile(self):

		DataList = []
		
		for iy in self.Year:
			for im in self.Mon:
				for id in self.Day:
					for ih in self.Hour:
					
						if iy != '': StrYear  = np.str(np.int(iy))[self.YLen:self.YLen+2]
						else: StrYear = ''
						if im != '': StrMon   = np.str(np.int(im)).zfill(2)
						else: StrMon = ''
						if id != '': StrDay   = np.str(np.int(id)).zfill(2)
						else: StrDay = ''
						if ih != '': StrHour  = np.str(np.int(ih)).zfill(2)	
						else: StrHour = ''
									
						Date = StrYear + StrMon + StrDay + StrHour						
						Path = self.StrPath + self.Prefix + Date + self.Suffix
						
						DataLine = np.loadtxt(Path)
						DataList.append(DataLine)
						DataArr = np.vstack(DataList)
		
		return DataArr

'''
#	def WriteFile(Year,Month,Day,Hour,StrPath): '''

def to_grid(DataArr, metadata):
	# Transfer DataArr to formed numpy grid data
	TimeShape = DataArr.shape[0]
	LonShape  = metadata.Longitude.shape[0]
	LatShape  = metadata.Latitude.shape[0] 
	MonShape  = metadata.Month.shape[0]
	YearShape = metadata.Year.shape[0]
	try:
		DataArr.shape[1] = LatShape * LonShape
	except:
		raise ValueError('DataArr data does not match the formed grid.')		
	return _to_grid(TimeShape,LatShape,Lonshape), metadata
	
def _to_grid(YearShape,MonShape,LatShape,Lonshape):
	
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