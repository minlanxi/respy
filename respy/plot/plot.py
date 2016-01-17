"""readtxt.py

Object-oriented code for reading formatted txt files.

Code developed by Lanxi Min, University at Albany
lmin@albany.edu

Here is an example to read a list of formatted txt files

""" 

import numpy as np

class ReadFormattedFile(object)

	def __init__(self):
	
	def FileNameGen(iy,im,id,ih):

		StrYear  = np.str(np.int(iy))
		StrMon   = np.str(np.int(im)).zfill(2)
		StrDay   = np.str(np.int(id)).zfill(2)
		StrHour  = np.str(np.int(ih)).zfill(2)				
		FileName = StrYear + StrMon + StrDay + StrHour
		
		return FileName

	def ReadFile(Year,Month,Day,Hour,StrPath,Prefix,Suffix):

		DataList = []
		
		for iy in Year:
			for im in Mon:
				for id in Day:
					for ih in Hour:
						FileName = FileNameGen(iy,im,id,ih)
						DataLine = np.loadtxt(StrPath+Prefix+Filename+Suffix)
						Datalist.append(DataLine)
						DataArray = np.vstack(DataList)
		
		return DataArray
		
	def WriteFile(Year,Month,Day,Hour,StrPath):
		

						
		
			
		
		
		
				 
