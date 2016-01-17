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
import datetime as dt
import calendar
from respy.utils import temporal

Datatypes = ['era40','erai','era5','ncep','isccp_fd','ceres','mod13c2','index','abstract']

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
					   spatial_res=2.5,
					   temporal_res='monthly',
					   startdate = dt.datetime(1990,4,1,18),
					   enddate = dt.datetime(2002,2,1,18),
					   mulfile = False,
					   filepath = '',
					   filename = '', 
					   filefix = ['',''],
					   ylen = 4):		
		
		#Dataset Information
		self.datatype = datatype
		self.spatial_res = spatial_res
		self.temporal_res = temporal_res
		
		#Files Temporal Information
		self.startdate = startdate
		self.enddate = enddate
		
		
		self.datelist = []
		if mulfile == False:
			months = temporal.monthdelta(startdate,enddate)
			for i in range(months+1):
				self.datelist.append(temporal.add_months(startdate,i))
		else:
			if temporal_res == 'Yearly':
				years = self.enddate.year - self.startdate.year
				for i in range(years+1):
					self.datelist.append(temporal.add_years(startdate,i))
			
			elif temporal_res == 'JJA':
				years  = self.enddate.year - self.startdate.year
				for i in range(years+1):
					ydate = temporal.add_years(startdate,i)
					self.datelist.append(ydate)
					self.datelist.append(temporal.add_months(ydate,1))
					self.datelist.append(temporal.add_months(ydate,2))
							
		#Data storage info
		self.mulfile = mulfile
		self.filepath = filepath
		self.filename = filename
		self.filefix = filefix
		self.ylen = ylen
		
		if datatype in Datatypes:
			pass
		elif datatype in ['e4']:
			datatype = 'era40'
		else:
			raise ValueError('Date Type %s not recognized' % datatype)
			
		if datatype == 'era5':
			self.lon = np.arange(-180.,180.,5)
			self.lat = np.arange(90.,-90.,-1*5)
			
		if datatype == 'era40':
			self.lev = np.array([1.,2.,3.,5.,7.,10.,20.,30.,50.,70.,100.,150.,
								200.,250.,300.,400.,500.,600.,700.,775.,850.,925.,1000.])
			self.lon = np.arange(-180.,180.,spatial_res)
			self.lat = np.arange(90.,-90.1,-1*spatial_res)
		
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
			self.lev = np.zeros(1)
			self.lon = np.arange(-178.75,180,2.5)
			self.lat = np.arange(-88.75,90.,2.5)
		
		elif datatype == 'ceres':
			self.lev = np.zeros(1)
			self.lon = np.arange(0.5,360.,1.)
			self.lat = np.arange(-89.5,90.,1.)
		
		elif datatype == 'mod13c2':
			self.lev = np.zeros(1)
			self.lon = -140.+np.arange(2000)/20.
			self.lat = 60.-np.arange(1000)/20.
			
###test

'''fp_vimfc = '/Users/minlanxi/Research/01_LAI/dat/ECMWF/E4_QUV_JJA/int_pres/'
e4_d1    = dt.datetime(1970,8,1,18)
e4_vi_d0 = dt.datetime(1960,6,1,18)

e4_vi_meta = Metadata(startdate=e4_vi_d0,enddate=e4_d1,
					  filepath=fp_vimfc,mulfile=True,
					  filefix=['e4_vi_m18_25.','.txt'],
					  ylen=2,temporal_res='Yearly')
'''			
			
'''	@property
	def datatype(self):
		return self.__datatype
	
	@datatype.setter
	def datatype(self, datatype):
		self.__datatype = datatype
		
'''	

		

						
		
			
		
		
		
				 
