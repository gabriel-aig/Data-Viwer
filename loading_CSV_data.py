# -*- coding: utf-8 -*-

'''
That's a script that will help you to load CSV data using a unique function to do that
over and over. If you are working with a large amount of data I strongly recommend you to
use Spyder and Anaconda.

The repository will contain examples of CSV data.

The function part can be manipulated to generate filters for raw data without the need of repetition
'''

def LOAD():
 
    import pandas as pd
    
    path = 'C:\scripts\data' # Write here the name of the directory to be used
    df_names = pd.DataFrame()
    df_names = pd.read_csv(path + f'\{name}')

    # Changing the default index to a column that contains datetime
    df_names.index=df_names['# Datetime']
    df_names.index=pd.to_datetime(df_names.index, format="%Y-%m-%d %H:%M:%S") # Datetime convertion

    df_names['swh_PNBOIA']=df_names['Wvht']
    df_names['hmax_PNBOIA']=df_names['Wmax']
    df_names['mwd_PNBOIA']=df_names['Mwd']

    # Filters
    x=df_names['swh_PNBOIA']>=0.0
    df_names=df_names[x]

    x=df_names['hmax_PNBOIA']>=0.0
    df_names=df_names[x]
    
    x=df_names['mwd_PNBOIA']>=0.0
    df_names=df_names[x]
    
    if name == 'RIO_GRANDE.csv':
        global df_RIO_GRANDE
        df_RIO_GRANDE = df_names
        
    else:
        if name == 'ITAJAI.csv':
            global df_ITAJAI
            df_ITAJAI = df_names
            
    print(f'{name} worked fine!')
 

import pandas as pd

# RIO_GRANDE
name = 'RIO_GRANDE.csv' # Name of the file
df_RIO_GRANDE = pd.DataFrame()
LOAD()


# ITAJAI
name = 'ITAJAI.csv' # Name of the file
df_ITAJAI = pd.DataFrame()
LOAD()

print('DOOOOOOOONE')
