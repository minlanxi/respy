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
		datelist = self.metadata.datelist
		
		tres = self.metadata.temporal_res
		StrPath = self.metadata.filepath
		Prefix  = self.metadata.filefix[0]
		Suffix  = self.metadata.filefix[1]
		YLen    = self.metadata.ylen
	
		try:
			YLen > 0
		except:
			raise ValueError('Wrong metadata infomation')		
		return readfiles(datelist,StrPath,Prefix,Suffix,YLen,tres)
	
	def ReadFile(self):
		# Read DataArr
		filepath = self.metadata.filepath
		filename = self.metadata.filename
		DataArr = np.loadtxt(filepath+filename)
		return DataArr
		

def readfiles(datelist,StrPath,Prefix,Suffix,YLen,tres):

	DataList = []
	
	if tres == 'Yearly':
					
		for i in range(len(datelist)):
		
			if YLen == 2:
				stryear = np.str(datelist[i].year)[YLen:YLen+2]
			elif YLen == 4:
				stryear = np.str(datelist[i].year)
		
	
			Date = stryear
			Path = StrPath + Prefix + Date + Suffix
		
			DataLine = np.loadtxt(Path)
			DataList.append(DataLine)
			DataArr = np.vstack(DataList)

		return DataArr
	
	elif tres == 'JJA':
	
		for i in range(len(datelist)):
		
			if YLen == 2:
				stryear = np.str(datelist[i].year)[YLen:YLen+2]
			elif YLen == 4:
				stryear = np.str(datelist[i].year)
		
			Date = stryear + datelist[i].strftime('%m')
			Path = StrPath + Prefix + Date + Suffix
		
			DataLine = np.loadtxt(Path)
			DataList.append(DataLine)
			DataArr = np.vstack(DataList)

		return DataArr

	

	
#class ReadFile(Read):

#class ReadIndex(Read):

#Path = ReadFormattedData(Prefix = 'test')
#print Path.ReadFile()