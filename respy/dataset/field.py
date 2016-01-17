#  Trying a new data model for state variables and domains:
#  Create a new sub-class of numpy.ndarray
#  that has as an attribute the metadata itself

# Following a tutorial on subclassing ndarray and climlab code by Prof. Rose
#
# http://docs.scipy.org/doc/numpy/user/basics.subclassing.html

import numpy as np

'''test usage:
import numpy as np
A = np.linspace(0., 10., 30)
d = domain.single_column()
atm = d['atm']
s = field.Field(A, domain=atm)
print s
print s.domain
# can slice this and it preserves the domain
#  a more full-featured implementation would have intelligent slicing
#  like in iris
s.shape == s.domain.shape
s[:1].shape == s[:1].domain.shape
#  But some things work very well. E.g. new field creation:
s2 = np.zeros_like(s)
print s2
print s2.domain
'''
class Field(np.ndarray):
	'''Custom class for all the remote sensing or reanalysis grid data 
	for data analysis. This class behaves like numpy.ndarray. 
	But every object has an attribute called metadata
	which is the metadata associated with that field. '''
	
	def __new__(cls, input_array, metadata = None):
		# cls behaves much like self, however, self points to an instance, 
		# cls points to an class.
		# Each grid variables will be processed into an formed ndarray instance
		# Input array is this already formed ndarray instance
		# Firstly, cast to be our class types
		# obj = np.asarray(input_array).view(cls)
		# This should ensure that shape is (1.) for scalar input
		obj = np.atleast_1d(input_array).view(cls)
		# add the new attribute metadata to the created instance
		# do some checking for correct dimensions
		
		if obj.shape == metadata.shape:
			print obj.shape, metadata.shape
			obj.metadata = metadata
		else:
			raise ValueError('input_array and domian have different shapes.')
			
		# would be nice to have some automatic domain creation here if none given
		# Finally, we must return the newly created object:
		return obj
	
    def __array_finalize__(self, obj):
        # ``self`` is a new object resulting from
        # ndarray.__new__(Field, ...), therefore it only has
        # attributes that the ndarray.__new__ constructor gave it -
        # i.e. those of a standard ndarray.
        #
        # We could have got to the ndarray.__new__ call in 3 ways:
        # From an explicit constructor - e.g. Field():
        #    obj is None
        #    (we're in the middle of the Field.__new__
        #    constructor, and self.domain will be set when we return to
        #    Field.__new__)
        if obj is None: return
        # From view casting - e.g arr.view(Field):
        #    obj is arr
        #    (type(obj) can be Field)
        # From new-from-template - e.g statearr[:3]
        #    type(obj) is Field
        #
        # Note that it is here, rather than in the __new__ method,
        # that we set the default value for 'domain', because this
        # method sees all creation of default objects - with the
        # Field.__new__ constructor, but also with
        # arr.view(Field).

        self.metadata = getattr(obj, 'metadata', None)
        # We do not need to return anything


'''def global_mean(field):
    #Calculate global mean of a field with latitude dependence.
    try:
        #lat = field.domain.axes['lat'].points
        lat = field.metadata.Longitude
    except:
        raise ValueError('No latitude axis in input field.')
    lat_radians = np.deg2rad(lat)
    return _global_mean(field.squeeze(), lat_radians)


def _global_mean(array, lat_radians):
    return np.sum(array * np.cos(lat_radians)) / np.sum(np.cos(lat_radians))
'''