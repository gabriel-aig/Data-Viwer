# -*- coding: utf-8 -*-

'''
That's a script that will help you to load Netcdf data using a unique function to do that
over and over. If you are working with a large amount of data I strongly recommend you to
use Spyder and Anaconda.

The repository will contain examples of Netcdf data.

The function part can be manipulated to generate filters for raw data without the need of repetition
'''

def LOAD():
 
    import pandas as pd
    import xarray as xr
    

    path = 'C:\\scripts\\data' # Write here the name of the directory to be used
    df_names = pd.DataFrame()
    df_names = xr.open_mfdataset(path + f'\\{name}')
    df_names = df_names.sel().to_dataframe()
    df_names = df_names.reset_index(level=['latitude', 'longitude'])

    # Choose the range and the latitude and longitude of your spot, if that's your goal.
    if name == 'era5_Boia_Recife.nc':
        global df_RECIFE
        #df_RECIFE = df_names.sel(longitude=longitude,latitude=latitude, method='nearest').to_dataframe()
        df_RECIFE = df_names[(df_names.index>=starting_date) & (df_names.index<=ending_date)] 
        
    print(f'{name} worked fine!')
 

import pandas as pd

# Recife
name = 'era5_Boia_Recife.nc' # Name of the file
#longitude = -49.50
#latitude = -31.33
starting_date = '2009-04-29 20:00'
ending_date = '2019-03-09 17:00'
df_RECIFE = pd.DataFrame()
LOAD()



print('DOOOOOOOONE')
