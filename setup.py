#!/usr/bin/env python

from distutils.core import setup

setup(name = 'respy',
	  version = '1.0.0',
	  description = 'Python tools for reading, visualizing and'
	  				'analyzing with remote sensing and meteorology dat.',
	  url = 'http://github.com/respy/respy',
	  
	  author = 'Lanxi Min',
	  author_email = 'lmin@albany.edu',
	  
	  packages = ['respy','respy.io','respy.dataset'],
	 )