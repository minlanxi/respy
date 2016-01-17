#!/usr/bin/env python

#from setuptools import setup
from distutils.core import setup
import distutils
distutils.dir_util.remove_tree

setup(name = 'respy',
	  version = '1.0.0',
	  description = 'Python tools for reading, visualizing and'
	  				'analyzing with remote sensing and meteorology dat.',
	  url = 'http://github.com/respy/respy',
	  
	  author = 'Lanxi Min',
	  author_email = 'lmin@albany.edu',
	  
	  packages = ['respy','respy.input','respy.dataset','respy.metadata','respy.analysis',
	  			  'respy.utils','respy.plot','respy.hdf','respy.aerosol'],
	 )