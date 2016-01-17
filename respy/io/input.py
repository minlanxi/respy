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

class Read(object):
	
	def __init__(self,metadata=None):
		self.metadata = metadata
		self.DataArr = None
		
	def ReadFiles(self):
		# Read DataArr
		Year = metadata.year
		Mon  = metadata.month
		Day  = metadata.month 
		Hour = metadata.hour
		StrPath = metadata.strpath
		Prefix  = metadata.affix[0]
		Suffix  = metadata.affix[1]
	
		try:
			Year.shape[0] > 0
		except:
			raise ValueError('Wrong metadata infomation')		
		return __ReadFiles(self,Year,Mon,Day,Hour,StrPath,Prefix,Suffix)
	
	def ReadFile(self):
		# Read DataArr
		filename = metadata.filename
		DataArr = np.loadtxt(filename)
		return DataArr
		

def __ReadFiles(Year,Mon,Day,Hour,StrPath,Prefix,Suffix):

	DataList = []

	for iy in self.__metadata.year:
		for im in self.__metadata.month:
			for id in self.__metadata.day:
				for ih in self.__metadata.hour:
		
					if iy != '': StrYear  = np.str(np.int(iy))[self.YLen:self.YLen+2]
					else: StrYear = ''
					if im != '': StrMon   = np.str(np.int(im)).zfill(2)
					else: StrMon = ''
					if id != '': StrDay   = np.str(np.int(id)).zfill(2)
					else: StrDay = ''
					if ih != '': StrHour  = np.str(np.int(ih)).zfill(2)	
					else: StrHour = ''
						
					Date = StrYear + StrMon + StrDay + StrHour						
					Path = StrPath + Prefix + Date + Suffix
			
					DataLine = np.loadtxt(Path)
					DataList.append(DataLine)
					DataArr = np.vstack(DataList)

	return DataArr	

	

	
#class ReadFile(Read):

#class ReadIndex(Read):

#Path = ReadFormattedData(Prefix = 'test')
#print Path.ReadFile()