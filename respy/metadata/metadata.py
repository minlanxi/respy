"""Domain.py

Object-oriented code for setting 3D coordinates: Longitude, Latitude, Pressure, Height.

Code developed by Lanxi Min, University at Albany
lmin@albany.edu

Here is an example to set dataset metadata:

Year = np.linspace(1900,2015,116)
Mon  = np.linspace(1,12,12)
Day  = np.linspace(1,31,31)
Hour = np.array([0,6,12,18])

e4_meta = Metadata(datatype='e4', year=Year, month=Mon, day=Day, hour=Hour)

""" 

import numpy as np

Datatypes = ['era40','erai','ncep','isccp_fd','ceres','mod13c2','abstract']

DefaultEndPoints = {'lev': (0., 1000.),
					'lat': (-90., 90.),
					'lon': (-180.,180.),
					'abstract': (0.,10.)}
					
DefaultUnits = {'lev': 'mb',
				'lat': 'degrees',
				'lon': 'degress',
				'abstract': 'none'}

class Metadata(object):

	def __str__(self):
		return ('Data Type is ' + self.datatype)
		
	def __init__(self, datatype='abstract',
					   mulfile = False,
					   shape = [1,1,1]
					   resolution=2.5,
					   year = [''],
					   month = [''],
					   day = [''],
					   hour = [''],
					   strpath = '',
					   filename = '', 
					   startdate = '199004',
					   enddate = '201504',
					   affix = ['',''],
					   ylen = 4):
		
		#Data storage info
		self.strpath = strpath
		self.filename = filename
		self.startmon = startmon
		self.affix = affix
		self.ylen = ylen
		
		#Dataset Information
		self.datatype = datatype
		self.muldata = muldata
		self.resolution = resolution
		
		#Files Temporal Information
		self.year = year
		self.month = month
		self.day = day
		self.hour = hour
		
		#File Temporal Information
		self.startdate = startdate
		self.enddate = enddate
		
		if datatype in Datatypes:
			pass
		elif datatype in ['e4']:
			datatype = 'era40'
		else:
			raise ValueError('Date Type %s not recognized' % datatype)
			
		if datatype == 'era40':
			self.lev = np.array([1.,2.,3.,5.,7.,10.,20.,30.,50.,70.,100.,150.,
								200.,250.,300.,400.,500.,600.,700.,775.,850.,925.,1000.])
			self.lon = np.arange(-180.,180.,2.5)
			self.lat = np.arange(90.,-90.1,-2.5)
		
		elif datatype == 'erai':
			self.lev = np.array([1.,2.,3.,5.,7.,10.,20.,30.,50.,70.,100.,125.,
								150.,175.,200.,225.,250.,300.,350.,400.,450.,
								500.,550.,600.,650.,700.,750.,775.,800.,825.,
								850.,875.,900.,925.,950.,975.,1000.])
			self.lon = np.arange(-180.,180.,2.5)
			self.lat = np.arange(90.,-90.1,-2.5)
		
		elif datatype == 'ncep':
			self.lev = np.array([1000.,925.,850.,700.,600.,500.,400.,300.,250.,200.,
								150.,100.,70.,50.,30.,20.,10.])
			self.lon = np.arange(0,360.,2.5)
			self.lat = np.arange(90,-90.1,-2.5)
		elif datatype == 'isccp_fd':
			self.lev = None
			self.lon = np.arange(-178.75,180,2.5)
			self.lat = np.arange(-88.75,90.,2.5)
		
		elif datatype == 'ceres':
			self.lon = np.arange(0.5,360.,1.)
			self.lat = np.arange(-89.5,90.,1.)
		
		elif datatype == 'mod13c2':
			self.lon = -140.+np.arange(2000)/20.
			self.lat = 60.-np.arange(1000)/20.
			
			
			
'''	@property
	def datatype(self):
		return self.__datatype
	
	@datatype.setter
	def datatype(self, datatype):
		self.__datatype = datatype
		
'''	

		

						
		
			
		
		
		
				 
