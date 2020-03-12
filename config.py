###################################################################################################
##### Configuration file for all emgfit submodules

# Load packages
import numpy as np
import pandas as pd
import scipy.constants as con
from pathlib import Path


##### Define fundamental constants
global m_e, u, u_to_keV
m_e = con.physical_constants["electron mass in u"][0]  #548.5799.0907e-06 # electron mass [u] (from AME2016, Huang2017)
u = con.u
u_to_keV = con.physical_constants["atomic mass constant energy equivalent in MeV"][0]*1000 # conversion factor from u to keV

##### Define constant for fit routines
A_stat = 1.25  # constant of proportionality for calculating statistical mass error of HyperEmg-fits:  stat_error = A_stat * Std. Dev. / sqrt(area)

##### Import AME dataframe
directory = Path(__file__).parent  # get directory containing this file 
filename = str(directory)+"/AME2016/AME2016_formatted.csv"
df_AME = pd.read_csv(filename, encoding = 'unicode_escape') # C:/Users/Stefan/Dropbox/Beam time analysis/
df_AME.set_index(['Element','A'],inplace=True)

def mdata_AME(El,A):
    """ Gives atomic mass from AME2016 [u] """
    m_AME = df_AME['ATOMIC MASS [µu]'].loc[(El,A)]*1e-06
    m_AME_error = df_AME['Error ATOMIC MASS [µu]'].loc[(El,A)]*1e-06
    extrapolated_yn = df_AME['Extrapolated?'].loc[(El,A)]
    return [El, A, m_AME, m_AME_error, extrapolated_yn]

###################################################################################################
