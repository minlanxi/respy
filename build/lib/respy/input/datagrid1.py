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
import sys
sys.path.append("/Users/minlanxi/Research/01_LAI/respy/")

import numpy as np
from respy.input.input import Read
from respy.utils import temporal

class DataGrid(object):
    
    def __init__(self,metadata=None):
        self.metadata = metadata
        datafile  = Read(metadata)
        if metadata.mulfile == True:
            self.DataArr = datafile.ReadFiles()
        elif metadata.mulfile == False:
            self.DataArr = datafile.ReadFile()
        
    def index_to_grid(self,dt0,dt1):

        index_all = np.loadtxt(self.metadata.filepath+self.metadata.filename)
        #select interest year from date column
        #for instance, QBO[:,0] is date column
        #startyear = self.metadata.startdate.year
        #endyear = self.metadata.enddate.year
        startyear = dt0
        endyear   = dt1
        index = index_all[np.where((index_all[:,0]>=startyear.year)
                          & (index_all[:,0]<=endyear.year))]
        index_jja = np.mean([index[:,5],index[:,6],index[:,7]],axis = 0)
        return index_jja
    
    def field_to_grid(self,dt0,dt1,season):
        # Transfer DataArr to formed numpy grid data
        DataArr   = self.DataArr
        LonShape  = self.metadata.lon.shape[0]
        LatShape  = self.metadata.lat.shape[0]
        LevShape  = self.metadata.lev.shape[0] 
    
        StartDate = self.metadata.startdate
        EndDate   = self.metadata.enddate
        DateList  = self.metadata.datelist
        TempRes   = self.metadata.temporal_res
        
        if self.metadata.mulfile == False:      
            try:
                1 > 0
            except:
                raise ValueError('DataArr data does not match the formed grid.')        
            return _file_to_grid(DataArr,LatShape,LonShape,LevShape,
                                 StartDate,EndDate,DateList,dt0,dt1,season)
        
        elif self.metadata.mulfile == True:
            try:
                1 > 0
            except:
                raise ValueError('DataArr data does not match the formed grid.')        
            return _files_to_grid(DataArr,LatShape,LonShape,LevShape,
                                  DateList,TempRes)         
        
def _file_to_grid(DataArr,LatShape,Lonshape,LevShape,
                  StartDate,EndDate,DateList,dt0,dt1,season):
            
    Tshape  = len(DateList)     
    cutoff1 = temporal.monthdelta(StartDate,dt0)
    cutoff2 = Tshape - temporal.monthdelta(EndDate,dt1) 
    MonGrid  = DataArr.reshape(Tshape,LatShape,Lonshape)[cutoff1:cutoff2,:,:]
    
    if season == False:
        return MonGrid
    elif season == 'JJA':
        #select JJA data    
        YearLen = int(dt1.year) - int(dt0.year) + 1
        Grid = np.zeros((YearLen,LatShape,Lonshape))
        for i in range(YearLen):
            Grid[i,:,:] = np.mean([MonGrid[[5+i*12],:,:],MonGrid[[6+i*12],:,:],
                                   MonGrid[[7+i*12],:,:]], axis = 0)
    return Grid
    


def _files_to_grid(DataArr,LatShape,Lonshape,LevShape,DateList,TempRes):

    if TempRes == 'Yearly':
        YearShape = len(DateList)
        Grid = DataArr.reshape(YearShape,LatShape,Lonshape)
    elif TempRes == 'JJA':
        MonShape = 3
        DataTemp = DataArr.reshape(YearShape,MonShape,LatShape,Lonshape)
        Grid = np.nanmean(DataTemp,axis=1)
        del DataTemp
    
    return Grid     
    

#Path = ReadFormattedData(Prefix = 'test')
#print Path.ReadFile()