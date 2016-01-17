"""Domain.py

Object-oriented code for setting 3D coordinates: Longitude, Latitude, Pressure, Height.

Code developed by Lanxi Min, University at Albany
lmin@albany.edu

Here is an example to set 3D coordinates

""" 

import numpy as np

data_types = ['era40','erai','ncep','isccp_fd','ceres','mod13c2','abstract']

	
class _Dataset(object):
	def __init__(self, **kwarg):

		
	def set_metadata():
		self.metadata = Metadata()
		
	def get_dataarray():
		self.dataarray = ReadFile()
		
class Index(_Dataset):
	def __init__(self, **kwargs):
		super(Index, self).__init__(**kwargs)
		self.datatype = 'Index'

class ERA40(_Dataset):
	def __init(self, **kwargs):
		super(ERA40, self).__init__(**kwargs)
		self.datatype = 'era40'
		
def set_index_metadata():
	index_metadata = Index()
	return index_metadata

def set_variable_metadata():
	variable_metadata = Variable()
	return variable_metadata
