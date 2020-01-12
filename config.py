###################################################################################################
##### Configuration file for all emgfit submodules

# Load packages
import numpy as np
import pandas as pd
import scipy.constants as con

##### Define fundamental constants
global m_e, u_to_keV
m_e = con.physical_constants["electron mass in u"][0]  #548.5799.0907e-06 # electron mass [u] (from AME2016, Huang2017)
u_to_keV = con.physical_constants["atomic mass constant energy equivalent in MeV"][0]*1000 # conversion factor from u to keV

##### Import AME dataframe
df_AME = pd.read_csv("C:/Users/Stefan/Dropbox/Beam time analysis/AME2016/AME2016_formatted.csv",encoding = 'unicode_escape')
df_AME.set_index(['Element','A'],inplace=True)

def mdata_AME(El,A):
    """ Gives atomic mass from AME2016 [u] """
    m_AME = df_AME['ATOMIC MASS [µu]'].loc[(El,A)]*1e-06
    m_AME_error = df_AME['Error ATOMIC MASS [µu]'].loc[(El,A)]*1e-06
    extrapolated_yn = df_AME['Extrapolated?'].loc[(El,A)]
    return [El, A, m_AME, m_AME_error, extrapolated_yn]

###################################################################################################
