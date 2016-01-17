"""Domain.py

Object-oriented code for setting 3D coordinates: Longitude, Latitude, Pressure, Height.

Code developed by Lanxi Min, University at Albany
lmin@albany.edu

Here is an example to set 3D coordinates

""" 
import sys
sys.path.append("/Users/minlanxi/Research/01_LAI/respy/")


import numpy as np
import respy
import os
import time

#pos0 = respy.spatial.deg2decimal(24,17,16.25)
#pos1 = respy.spatial.deg2decimal(61,50,36.73)
#pos = [pos0,pos1]

arith_mean = np.array([3.16,3.55,3.98,4.47,5.01,5.62,6.31,7.08,7.94,8.91,10.0,11.2,12.6,
                       14.1,15.8,17.8,20.0,22.4,25.1,28.2,31.6,35.5,39.8,44.7,50.1,56.2,
                       63.1,70.8,79.4,89.1,100.0,112.0,126.0,141.0,158.0,178.0,200.0,224.0,
                       251.0,282.0,316.0,355.0,398.0,447.0,501.0,562.0,631.0,708.0,794.0,891.0,1000.0])
                       
def NumberCon(Dp,time,psd):   
    dN = np.zeros_like(Dp)  
    N  = np.zeros(time)
    L  = len(Dp) 
    border = np.zeros(L+1)
    for i in range(time):
        border[0] = 2*Dp[0]-(Dp[1] + Dp[0])/2.
        for j in range(L-1):
            border[j+1] = (Dp[j+1] + Dp[j])/2.        
        border[L] = 2*Dp[L-1]-(Dp[L-2] + Dp[L-1])/2.
        for j in range(L):
            dN[j]  = psd[i,j] * (np.log10(border[j+1]) - np.log10(border[j]))
        N[i] = np.sum(dN)
    return N

def Diameters(Dp,time,psd):   
    dN = np.zeros_like(Dp)  
    N  = np.zeros(time)
    L  = len(Dp) 
    border = np.zeros(L+1)
    Dpg = np.zeros_like(Dp)
    Dpa = np.zeros_like(Dp)
    S = np.zeros_like(Dp)
    M = np.zeros_like(Dp)
    Dpg_bar = np.zeros(time)
    Dpa_bar = np.zeros(time)
    S_bar = np.zeros(time)
    M_bar = np.zeros(time)
    density = 1.8/10e6
    
    for i in range(time):
        border[0] = 2*Dp[0]-(Dp[1] + Dp[0])/2.
        for j in range(L-1):
            border[j+1] = (Dp[j+1] + Dp[j])/2.              
        border[L] = 2*Dp[L-1]-(Dp[L-2] + Dp[L-1])/2.
        for j in range(L):
            dN[j]  = psd[i,j] * (np.log10(border[j+1]) - np.log10(border[j]))
        N[i] = np.sum(dN)
        for j in range(L):
            Dpg[j] = Dp[j]**(dN[j]/N[i])
            Dpa[j] = Dp[j]*dN[j]/N[i]         
            S[j] = np.pi*Dp[j]**2*dN[j]/N[i]/np.pi
            M[j] = (np.pi/6.)*(Dp[j])**3*dN[j]/N[i]/np.pi*6            
        
        Dpg_bar[i] = np.prod(Dpg)
        Dpa_bar[i] = np.sum(Dpa)
        S_bar[i] = np.sum(S)**0.5
        M_bar[i] = np.sum(M)**(1/3.)
    return Dpg_bar,Dpa_bar,S_bar,M_bar
    
def preprocessing(EBAS): 
	for i in range(8741):
		for j in range(156):
			if EBAS[i,j] == 999999.99:
				EBAS[i,j] = np.nan
			if EBAS[i,j] == 99999.99:
				EBAS[i,j] = np.nan
			if EBAS[i,j] == 9999.99:
				EBAS[i,j] = np.nan
			elif EBAS[i,j] == 999.99:
				EBAS[i,j] = np.nan
			elif EBAS[i,j] == 99.99:
				EBAS[i,j] = np.nan
			elif EBAS[i,j] == 9.99:
				EBAS[i,j] = np.nan
			elif EBAS[i,j] == 0.99:
				EBAS[i,j] = np.nan
			elif EBAS[i,j] == 0.999:
				EBAS[i,j] = np.nan
	return EBAS

                       
def monthly_ccn(filepath,filename):
	filelen  = len(filename)
	N_mon_60 = np.zeros(12*filelen)
	for yy in range(filelen):
		print filepath+filename[yy]
		EBAS0 = np.genfromtxt(filepath+filename[yy],skip_header=200,missing_values=99999.99,filling_values=np.nan)
		EBAS1 = preprocessing(EBAS0)
				
		t = EBAS1[:,0]
		month = np.zeros_like(t)
		for i in range(EBAS1.shape[0]):
			#print t[i]
			dt0 = respy.utils.temporal.julian2date(2001+yy,t[i])
			month[i] = dt0.month
			
		N_60 = NumberCon(arith_mean[27:51],EBAS1.shape[0],EBAS1[:,29:53])            
		
		for i in range(12):
			N_mon_60[yy*12+i] = np.nanmean(N_60[np.where(month==i+1)])
		np.savetxt('N_mon_60.txt',N_mon_60)
		print filename[yy],'done'
	return N_mon_60
	
def daily_ccn(filepath,filename,tlist):
	#filelen  = len(filename[10])
	#for yy in range(filelen):
	EBAS0 = np.genfromtxt(filepath+filename[8],skip_header=200,missing_values=99999.99,filling_values=np.nan)
	EBAS  = preprocessing(EBAS0)
	print EBAS.shape
	t   = EBAS[:,0]
	EBAS1 = EBAS[np.where(np.logical_and(t>=59,t<151))]
	

	N_25 = NumberCon(arith_mean[0:18], EBAS1.shape[0],EBAS1[:,2:20])
	N_60 = NumberCon(arith_mean[27:51],EBAS1.shape[0],EBAS1[:,29:53])

	
	ccn = np.zeros(len(tlist)) 
	npf = np.zeros(len(tlist)) 
	j = 0
	for i in range(EBAS1.shape[0]):
		deltat = np.abs(t[i] - respy.temporal.date2julian(tlist[j]))
		if deltat <= 0.04:
			ccn[j] = np.nanmean([N_60[i-2],N_60[i-1],N_60[i],N_60[i+1],N_60[i+2],N_60[i+3]])
			npf[j] = np.nanmean([N_25[i-2],N_25[i-1],N_25[i],N_25[i+1],N_25[i+2],N_25[i+3]])
			print respy.temporal.date2julian(tlist[j]),npf[j],j
			j += 1
			if j >= len(tlist):
				break
	np.savetxt('npf_daily_2009.txt',npf)
	np.savetxt('ccn_daily_2009.txt',ccn)
	np.savetxt('n25_daily_continnum_2009.txt',N_25)
	np.savetxt('t_continnum_2009.txt',t)
	np.savetxt('npf_event_2009.txt',EBAS1[:,2:53])
	return npf,ccn
	
	

			
			
		
	
        