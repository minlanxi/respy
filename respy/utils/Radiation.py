"""insolation.py

This module contains general-purpose routines for computing incoming
solar radiation at the top of the atmosphere.

Currently, only daily average insolation is computed.

Ported and modified from MATLAB code daily_insolation.m
Original authors:
    Ian Eisenman and Peter Huybers, Harvard University, August 2006
Available online at http://eisenman.ucsd.edu/code/daily_insolation.m

If using calendar days, solar longitude is found using an
approximate solution to the differential equation representing conservation
of angular momentum (Kepler's Second Law).  Given the orbital parameters
and solar longitude, daily average insolation is calculated exactly
following Berger 1978.

References:
Berger A. and Loutre M.F. (1991). Insolation values for the climate of
 the last 10 million years. Quaternary Science Reviews, 10(4), 297-317.
Berger A. (1978). Long-term variations of daily insolation and
 Quaternary climatic changes. Journal of Atmospheric Science, 35(12),
 2362-2367.
"""
import sys
sys.path.append("/Users/minlanxi/Research/01_LAI/respy/")

import numpy as np
from respy.utils import constants as const


