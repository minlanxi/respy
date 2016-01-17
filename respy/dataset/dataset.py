"""Domain.py

Object-oriented code for setting 3D coordinates: Longitude, Latitude, Pressure, Height.

Code developed by Lanxi Min, University at Albany
lmin@albany.edu

Here is an example to set 3D coordinates

""" 

import numpy as np
from respy.metadata.metadata import Metadata
from respy.input.datagrid import DataGrid
	
class Dataset(object):
	def __init__(self, metadata = None, **kwarg):
	    self.meta = metadata
	    self.grid = None

		
	def set_metadata(self):
	    return self.meta
	    
	def get_metadata(self,meta):
		self.meta = meta
		return self.meta
		
	def get_dataarray(self):
	    return self.grid
		
		
class Index(Dataset):
	def __init__(self, **kwargs):
		super(Index, self).__init__(**kwargs)
		self.datatype = 'index'
		#self.meta = Metadata()
		#self.grid = DataGrid()
	
	###metadata###
	def set_metadata(self,startdate,enddate,filepath,filename):
		self.meta = Metadata(datatype='index',
				     startdate=startdate,enddate=enddate,
				     filepath=filepath,filename=filename)
		return self.meta
		

	###griddata###	
	def get_griddata(self,dt0,dt1):
		if self.meta.filename == None:
			StartDate = self.meta.startdate
			EndDate = self.meta.enddate
			Tshape  = EndDate.year-StartDate.year+1
			cutoff1 = dt0.year-StartDate.year
			cutoff2 = Tshape - (EndDate.year-dt1.year)
			grid = self.grid
			#print grid.shape,cutoff1,cutoff2
			self.grid = grid[cutoff1:cutoff2]
		else:  
			index_grid = DataGrid(metadata=self.meta)
			self.grid = index_grid.index_to_grid(dt0,dt1)
		return self.grid                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

		
	def set_griddata(self,grid):
		self.grid = grid
		return self.grid
		
		
		
class ECMWF(Dataset):
	def __init(self, **kwargs):
		super(ECMWF, self).__init__(**kwargs)
		self.datatype = 'era40'
		
		###metadata###
	def set_metadata(self,startdate,enddate,filepath,filename):
		self.meta = Metadata(datatype='e4',
						     startdate=startdate,enddate=enddate,
						     filepath=filepath,filename=filename)
		return self.meta

	###griddata###	
	def get_griddata(self,dt0,dt1,season):
		e4_grid = DataGrid(metadata=self.meta)
		self.grid = e4_grid.field_to_grid(dt0,dt1,season)
		self.meta.startdate = dt0
		self.meta.enddate = dt1
		return self.grid
		
class ISCCP(Dataset):
	def __init(self, **kwargs):
		super(ISCCP, self).__init__(**kwargs)
		self.datatype = 'isccp_fd'
		
		###metadata###
	def set_metadata(self,startdate,enddate,filepath,filename):
		self.meta = Metadata(datatype='isccp_fd',
						     startdate=startdate,enddate=enddate,
						     filepath=filepath,filename=filename)
		return self.meta

	###griddata###	
	def get_griddata(self,dt0,dt1,season):
		is_grid = DataGrid(metadata=self.meta)
		self.grid = is_grid.field_to_grid(dt0,dt1,season)
		self.meta.startdate = dt0
		self.meta.enddate = dt1
		return self.grid
		
class MOD13(Dataset):
	def __init(self, **kwargs):
		super(MOD13, self).__init__(**kwargs)
		self.datatype = 'mod13c2'
		
		###metadata###
	def set_metadata(self,startdate,enddate,filepath,filename):
		self.meta = Metadata(datatype='mod13c2',
						     startdate=startdate,enddate=enddate,
						     filepath=filepath,filename=filename)
		return self.meta

	###griddata###	
	def set_griddata(self,griddata):
		self.grid = griddata
		return self.grid
		
def combine_dataset(dataset1,dataset2):
	dataset = ECMWF()
	dataset.grid = np.vstack([dataset1.grid,dataset2.grid])
	dataset.set_metadata(dataset1.meta.startdate,dataset2.meta.enddate,'','')
	return dataset
	
def ecmwf2index(dataset):
	dt0 = dataset.meta.startdate
	dt1 = dataset.meta.enddate
	
	Tshape = dt1.year-dt0.year+1
	
	ecmwf_grid = dataset.grid 
	index_grid = np.zeros(Tshape)
	
	for i in range(Tshape):
		index_grid[i] = np.nanmean(ecmwf_grid[i,36,:],axis=0)

	index = Index()
	index.grid = index_grid
	index.set_metadata(dataset.meta.startdate,dataset.meta.enddate,None,None)
	index.set_griddata(index_grid)
	return index
