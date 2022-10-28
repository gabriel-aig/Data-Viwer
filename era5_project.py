# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:36:58 2022

@author: gabri
"""

# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt                                                                                                                          
import numpy as np
randn = np.random.randn
import xarray as xr                                                                                                                                      
import pandas as pd
import seaborn as sns
from sklearn.metrics import mean_squared_error
import skill_metrics as sm
from windrose import WindroseAxes
import matplotlib.cm as cm
from astropy.stats.circstats import circcorrcoef
from astropy import units as u



####################### Já está de 1h em 1h ############################ 
#   Talvez eu tenha que mudar o uso das variáveis
# Erro: Domínio espectral ou do tempo? MODELOS FAZEM O ESPECTRAL


# Consertar caso as variáveis estejam erradas





###########################################################################################################################
#########################################       RIO GRANDE      ###############################################
###########################################################################################################################

#ABRINDO OS DADOS DE NC DO ERA5
ds_wave=xr.open_mfdataset('C:\\Users\\gabri\\Desktop\\sepia\\ERA5\\ERA5_Boia_Rio_Grande.nc') #abrindo os arquivos nc


#DEFININDO O PONTO DO ERA5 RELATIVO À POSIÇÃO DO PNBOIA, ajustar
df_RIO_GRANDE = ds_wave.sel().to_dataframe()

df_RIO_GRANDE = df_RIO_GRANDE.reset_index(level=['latitude', 'longitude'])


# Como estamos trabalhando para RIO_GRANDE, ajustar datas
df_RIO_GRANDE=df_RIO_GRANDE[(df_RIO_GRANDE.index>='2009-04-29 20:00') & (df_RIO_GRANDE.index<='2019-03-09 17:00')] 


#abrindo o arquivo do PNBOIA RIO_GRANDE, direto do site
PNBOIA_RIO_GRANDE = pd.read_csv('C:\\IC PYTHON\\Distribuição espectral\\Rio Grande Def\\Rio Grande.csv')

#Transoformando Datetime em um índice
PNBOIA_RIO_GRANDE.index=PNBOIA_RIO_GRANDE['DATE    ']
PNBOIA_RIO_GRANDE.index=pd.to_datetime(PNBOIA_RIO_GRANDE.index, format=" %Y-%m-%d %H:%M(UTC)") #CONVERTENDO PRA DATETIME


df_RIO_GRANDE['swh_PNBOIA']=PNBOIA_RIO_GRANDE['Hm0                            ']
df_RIO_GRANDE['mwd_PNBOIA']=PNBOIA_RIO_GRANDE['Mean Magnetic Direction        ']
df_RIO_GRANDE['mwp_PNBOIA']=PNBOIA_RIO_GRANDE['Mean Period                    ']

df_RIO_GRANDE['swh_ERA5']=df_RIO_GRANDE['wav_hs']
df_RIO_GRANDE['mwd_ERA5']=df_RIO_GRANDE['wav_dm']
df_RIO_GRANDE['mwp_ERA5']=df_RIO_GRANDE['wav_tmm10']


##removendo os flags
#tirando os nans
x=df_RIO_GRANDE['swh_PNBOIA']>=0.0
df_RIO_GRANDE=df_RIO_GRANDE[x]

x=df_RIO_GRANDE['mwd_PNBOIA']>=0.0
df_RIO_GRANDE=df_RIO_GRANDE[x]

x=df_RIO_GRANDE['mwp_PNBOIA']>=0.0
df_RIO_GRANDE=df_RIO_GRANDE[x]

###########################################################################################################################
########################################################    ITAJAÍ  #########################################
###########################################################################################################################


#ABRINDO OS DADOS DE NC DO ERA5
ds_wave=xr.open_mfdataset('C:\\Users\\gabri\\Desktop\\sepia\\ERA5\\ERA5_Boia_ITAJAI.nc') #abrindo os arquivos nc


#DEFININDO O PONTO DO ERA5 RELATIVO À POSIÇÃO DO PNBOIA, ajustar
df_ITAJAI = ds_wave.sel().to_dataframe()

df_ITAJAI = df_ITAJAI.reset_index(level=['latitude', 'longitude'])




# Como estamos trabalhando para ITAJAI, ajustar datas
df_ITAJAI=df_ITAJAI[(df_ITAJAI.index>='2009-04-23 15:00') & (df_ITAJAI.index<='2019-10-19 23:00')] 


#abrindo o arquivo do PNBOIA ITAJAI, direto do site
PNBOIA_ITAJAI = pd.read_csv('C:\\IC PYTHON\\Distribuição espectral\\Itajaí Def\\Itajai.csv')

#Transoformando Datetime em um índice
PNBOIA_ITAJAI.index=PNBOIA_ITAJAI['DATE    ']
PNBOIA_ITAJAI.index=pd.to_datetime(PNBOIA_ITAJAI.index, format=" %Y-%m-%d %H:%M(UTC)") #CONVERTENDO PRA DATETIME



df_ITAJAI['swh_PNBOIA']=PNBOIA_ITAJAI['Hm0                            ']
df_ITAJAI['mwd_PNBOIA']=PNBOIA_ITAJAI['Mean Magnetic Direction        ']
df_ITAJAI['mwp_PNBOIA']=PNBOIA_ITAJAI['Mean Period                    ']

df_ITAJAI['swh_ERA5']=df_ITAJAI['wav_hs']
df_ITAJAI['mwd_ERA5']=df_ITAJAI['wav_dm']
df_ITAJAI['mwp_ERA5']=df_ITAJAI['wav_tmm10']


##removendo os flags
#tirando os nans
x=df_ITAJAI['swh_PNBOIA']>=0.0
df_ITAJAI=df_ITAJAI[x]

x=df_ITAJAI['mwd_PNBOIA']>=0.0
df_ITAJAI=df_ITAJAI[x]

x=df_ITAJAI['mwp_PNBOIA']>=0.0
df_ITAJAI=df_ITAJAI[x]




###########################################################################################################################
########################################################    SANTOS  #########################################
###########################################################################################################################

#ABRINDO OS DADOS DE NC DO ERA5
ds_wave=xr.open_mfdataset('C:\\Users\\gabri\\Desktop\\sepia\\ERA5\\ERA5_Boia_SANTOS.nc') #abrindo os arquivos nc


#DEFININDO O PONTO DO ERA5 RELATIVO À POSIÇÃO DO PNBOIA, ajustar
df_SANTOS = ds_wave.sel().to_dataframe()

df_SANTOS = df_SANTOS.reset_index(level=['latitude', 'longitude'])

# Como estamos trabalhando para SANTOS, ajustar datas
df_SANTOS=df_SANTOS[(df_SANTOS.index>='2011-04-12 19:00') & (df_SANTOS.index<='2018-12-09 09:00')] 



#abrindo o arquivo do PNBOIA SANTOS, direto do site
PNBOIA_SANTOS = pd.read_csv('C:\\IC PYTHON\\Distribuição espectral\\Santos Def\\Santos.csv')
#Outros dados PNBOIA


#Transoformando Datetime em um índice
PNBOIA_SANTOS.index=PNBOIA_SANTOS['DATE    ']
PNBOIA_SANTOS.index=pd.to_datetime(PNBOIA_SANTOS.index, format=" %Y-%m-%d %H:%M(UTC)") #CONVERTENDO PRA DATETIME


df_SANTOS['swh_PNBOIA']=PNBOIA_SANTOS['Hm0                            ']
df_SANTOS['mwd_PNBOIA']=PNBOIA_SANTOS['Mean Magnetic Direction        ']
df_SANTOS['mwp_PNBOIA']=PNBOIA_SANTOS['Mean Period                    ']

df_SANTOS['swh_ERA5']=df_SANTOS['wav_hs']
df_SANTOS['mwd_ERA5']=df_SANTOS['wav_dm']
df_SANTOS['mwp_ERA5']=df_SANTOS['wav_tmm10']


##removendo os flags
#tirando os nans
x=df_SANTOS['swh_PNBOIA']>=0.0
df_SANTOS=df_SANTOS[x]

x=df_SANTOS['mwd_PNBOIA']>=0.0
df_SANTOS=df_SANTOS[x]

x=df_SANTOS['mwp_PNBOIA']>=0.0
df_SANTOS=df_SANTOS[x]





###########################################################################################################################
########################################################    CABO_FRIO  #########################################
###########################################################################################################################

#ABRINDO OS DADOS DE NC DO ERA5
ds_wave=xr.open_mfdataset('C:\\Users\\gabri\\Desktop\\sepia\\ERA5\\ERA5_Boia_CABO_FRIO.nc') #abrindo os arquivos nc


#DEFININDO O PONTO DO ERA5 RELATIVO À POSIÇÃO DO PNBOIA, ajustar
df_CABO_FRIO = ds_wave.sel().to_dataframe()

df_CABO_FRIO = df_CABO_FRIO.reset_index(level=['latitude', 'longitude'])


# Como estamos trabalhando para CABO_FRIO, ajustar datas
df_CABO_FRIO=df_CABO_FRIO[(df_CABO_FRIO.index>='2016-07-20 18:00') & (df_CABO_FRIO.index<='2018-10-31 11:00')] 



#abrindo o arquivo do PNBOIA CABO_FRIO, direto do site
PNBOIA_CABO_FRIO = pd.read_csv('C:\\IC PYTHON\\Distribuição espectral\\Cabo Frio Def\\Cabo Frio.csv')
#Outros dados PNBOIA

#Transoformando Datetime em um índice
PNBOIA_CABO_FRIO.index=PNBOIA_CABO_FRIO['DATE    ']
PNBOIA_CABO_FRIO.index=pd.to_datetime(PNBOIA_CABO_FRIO.index, format=" %Y-%m-%d %H:%M(UTC)") #CONVERTENDO PRA DATETIME



df_CABO_FRIO['swh_PNBOIA']=PNBOIA_CABO_FRIO['Hm0                            ']
df_CABO_FRIO['mwd_PNBOIA']=PNBOIA_CABO_FRIO['Mean Magnetic Direction        ']
df_CABO_FRIO['mwp_PNBOIA']=PNBOIA_CABO_FRIO['Mean Period                    ']

df_CABO_FRIO['swh_ERA5']=df_CABO_FRIO['wav_hs']
df_CABO_FRIO['mwd_ERA5']=df_CABO_FRIO['wav_dm']
df_CABO_FRIO['mwp_ERA5']=df_CABO_FRIO['wav_tmm10']


##removendo os flags
#tirando os nans
x=df_CABO_FRIO['swh_PNBOIA']>=0.0
df_CABO_FRIO=df_CABO_FRIO[x]

x=df_CABO_FRIO['mwd_PNBOIA']>=0.0
df_CABO_FRIO=df_CABO_FRIO[x]

x=df_CABO_FRIO['mwp_PNBOIA']>=0.0
df_CABO_FRIO=df_CABO_FRIO[x]







###########################################################################################################################
########################################################    VITORIA  #########################################
###########################################################################################################################


#ABRINDO OS DADOS DE NC DO ERA5
ds_wave=xr.open_mfdataset('C:\\Users\\gabri\\Desktop\\sepia\\ERA5\\ERA5_Boia_VITORIA.nc') #abrindo os arquivos nc


#DEFININDO O PONTO DO ERA5 RELATIVO À POSIÇÃO DO PNBOIA, ajustar
df_VITORIA = ds_wave.sel().to_dataframe()

df_VITORIA = df_VITORIA.reset_index(level=['latitude', 'longitude'])

# Como estamos trabalhando para VITORIA, ajustar datas
df_VITORIA=df_VITORIA[(df_VITORIA.index>='2015-10-13 17:00') & (df_VITORIA.index<='2017-07-23 04:00')] 



#abrindo o arquivo do PNBOIA VITORIA, direto do site
PNBOIA_VITORIA = pd.read_csv('C:\\IC PYTHON\\Distribuição espectral\\Vitória Def\\Vitoria.csv')


#Transoformando Datetime em um índice
PNBOIA_VITORIA.index=PNBOIA_VITORIA['DATE    ']
PNBOIA_VITORIA.index=pd.to_datetime(PNBOIA_VITORIA.index, format=" %Y-%m-%d %H:%M(UTC)") #CONVERTENDO PRA DATETIME



df_VITORIA['swh_PNBOIA']=PNBOIA_VITORIA['Hm0                            ']
df_VITORIA['mwd_PNBOIA']=PNBOIA_VITORIA['Mean Magnetic Direction        ']
df_VITORIA['mwp_PNBOIA']=PNBOIA_VITORIA['Mean Period                    ']

df_VITORIA['swh_ERA5']=df_VITORIA['wav_hs']
df_VITORIA['mwd_ERA5']=df_VITORIA['wav_dm']
df_VITORIA['mwp_ERA5']=df_VITORIA['wav_tmm10']


##removendo os flags
#tirando os nans
x=df_VITORIA['swh_PNBOIA']>=0.0
df_VITORIA=df_VITORIA[x]

x=df_VITORIA['mwd_PNBOIA']>=0.0
df_VITORIA=df_VITORIA[x]

x=df_VITORIA['mwp_PNBOIA']>=0.0
df_VITORIA=df_VITORIA[x]






###########################################################################################################################
########################################################    PORTO_SEGURO  #########################################
###########################################################################################################################


#ABRINDO OS DADOS DE NC DO ERA5
ds_wave=xr.open_mfdataset('C:\\Users\\gabri\\Desktop\\sepia\\ERA5\\ERA5_Boia_PORTO_SEGURO.nc') #abrindo os arquivos nc


#DEFININDO O PONTO DO ERA5 RELATIVO À POSIÇÃO DO PNBOIA, ajustar
df_PORTO_SEGURO = ds_wave.sel().to_dataframe()

df_PORTO_SEGURO = df_PORTO_SEGURO.reset_index(level=['latitude', 'longitude'])


# Como estamos trabalhando para PORTO_SEGURO, ajustar datas
df_PORTO_SEGURO=df_PORTO_SEGURO[(df_PORTO_SEGURO.index>='2012-07-06 04:00') & (df_PORTO_SEGURO.index<='2016-12-19 09:00')] 



#abrindo o arquivo do PNBOIA PORTO_SEGURO, direto do site
PNBOIA_PORTO_SEGURO = pd.read_csv('C:\\IC PYTHON\\Distribuição espectral\\Porto Seguro Def\\Porto Seguro.csv')
#Outros dados PNBOIA

#Transoformando Datetime em um índice
PNBOIA_PORTO_SEGURO.index=PNBOIA_PORTO_SEGURO['DATE    ']
PNBOIA_PORTO_SEGURO.index=pd.to_datetime(PNBOIA_PORTO_SEGURO.index, format=" %Y-%m-%d %H:%M(UTC)") #CONVERTENDO PRA DATETIME





df_PORTO_SEGURO['swh_PNBOIA']=PNBOIA_PORTO_SEGURO['Hm0                            ']
df_PORTO_SEGURO['mwd_PNBOIA']=PNBOIA_PORTO_SEGURO['Mean Magnetic Direction        ']
df_PORTO_SEGURO['mwp_PNBOIA']=PNBOIA_PORTO_SEGURO['Mean Period                    ']


df_PORTO_SEGURO['swh_ERA5']=df_PORTO_SEGURO['wav_hs']
df_PORTO_SEGURO['mwd_ERA5']=df_PORTO_SEGURO['wav_dm']
df_PORTO_SEGURO['mwp_ERA5']=df_PORTO_SEGURO['wav_tmm10']


##removendo os flags
#tirando os nans
x=df_PORTO_SEGURO['swh_PNBOIA']>=0.0
df_PORTO_SEGURO=df_PORTO_SEGURO[x]

x=df_PORTO_SEGURO['mwd_PNBOIA']>=0.0
df_PORTO_SEGURO=df_PORTO_SEGURO[x]

x=df_PORTO_SEGURO['mwp_PNBOIA']>=0.0
df_PORTO_SEGURO=df_PORTO_SEGURO[x]







###########################################################################################################################
########################################################    RECIFE  #########################################
###########################################################################################################################

#ABRINDO OS DADOS DE NC DO ERA5
ds_wave=xr.open_mfdataset('C:\\Users\\gabri\\Desktop\\sepia\\ERA5\\ERA5_Boia_RECIFE.nc') #abrindo os arquivos nc


#DEFININDO O PONTO DO ERA5 RELATIVO À POSIÇÃO DO PNBOIA, ajustar
df_RECIFE = ds_wave.sel().to_dataframe()

df_RECIFE = df_RECIFE.reset_index(level=['latitude', 'longitude'])


# Como estamos trabalhando para RECIFE, ajustar datas
df_RECIFE=df_RECIFE[(df_RECIFE.index>='2012-09-21 09:00') & (df_RECIFE.index<='2016-04-06 05:00')] 


#abrindo o arquivo do PNBOIA RECIFE, direto do site
PNBOIA_RECIFE = pd.read_csv('C:\\IC PYTHON\\Distribuição espectral\\Recife Def\\Recife.csv')
#Outros dados PNBOIA

#Transoformando Datetime em um índice
PNBOIA_RECIFE.index=PNBOIA_RECIFE['DATE    ']
PNBOIA_RECIFE.index=pd.to_datetime(PNBOIA_RECIFE.index, format=" %Y-%m-%d %H:%M(UTC)") #CONVERTENDO PRA DATETIME



df_RECIFE['swh_PNBOIA']=PNBOIA_RECIFE['Hm0                            ']
df_RECIFE['mwd_PNBOIA']=PNBOIA_RECIFE['Mean Magnetic Direction        ']
df_RECIFE['mwp_PNBOIA']=PNBOIA_RECIFE['Mean Period                    ']

df_RECIFE['swh_ERA5']=df_RECIFE['wav_hs']
df_RECIFE['mwd_ERA5']=df_RECIFE['wav_dm']
df_RECIFE['mwp_ERA5']=df_RECIFE['wav_tmm10']


##removendo os flags
#tirando os nans
x=df_RECIFE['swh_PNBOIA']>=0.0
df_RECIFE=df_RECIFE[x]

x=df_RECIFE['mwd_PNBOIA']>=0.0
df_RECIFE=df_RECIFE[x]

x=df_RECIFE['mwp_PNBOIA']>=0.0
df_RECIFE=df_RECIFE[x]







###########################################################################################################################
########################################################    FORTALEZA  #########################################
###########################################################################################################################

#ABRINDO OS DADOS DE NC DO ERA5
ds_wave=xr.open_mfdataset('C:\\Users\\gabri\\Desktop\\sepia\\ERA5\\ERA5_Boia_FORTALEZA.nc') #abrindo os arquivos nc


#DEFININDO O PONTO DO ERA5 RELATIVO À POSIÇÃO DO PNBOIA, ajustar
df_FORTALEZA = ds_wave.sel().to_dataframe()

df_FORTALEZA = df_FORTALEZA.reset_index(level=['latitude', 'longitude'])

# Como estamos trabalhando para FORTALEZA, ajustar datas
df_FORTALEZA=df_FORTALEZA[(df_FORTALEZA.index>='2016-11-18 20:00') & (df_FORTALEZA.index<='2018-05-20 19:00')] 

#abrindo o arquivo do PNBOIA FORTALEZA, direto do site
PNBOIA_FORTALEZA = pd.read_csv('C:\\IC PYTHON\\Distribuição espectral\\Fortaleza Def\\Fortaleza.csv')
#Outros dados PNBOIA


#Transoformando Datetime em um índice
PNBOIA_FORTALEZA.index=PNBOIA_FORTALEZA['DATE    ']
PNBOIA_FORTALEZA.index=pd.to_datetime(PNBOIA_FORTALEZA.index, format=" %Y-%m-%d %H:%M(UTC)") #CONVERTENDO PRA DATETIME




df_FORTALEZA['swh_PNBOIA']=PNBOIA_FORTALEZA['Hm0                            ']
df_FORTALEZA['mwd_PNBOIA']=PNBOIA_FORTALEZA['Mean Magnetic Direction        ']
df_FORTALEZA['mwp_PNBOIA']=PNBOIA_FORTALEZA['Mean Period                    ']

df_FORTALEZA['swh_ERA5']=df_FORTALEZA['wav_hs']
df_FORTALEZA['mwd_ERA5']=df_FORTALEZA['wav_dm']
df_FORTALEZA['mwp_ERA5']=df_FORTALEZA['wav_tmm10']


##removendo os flags
#tirando os nans
x=df_FORTALEZA['swh_PNBOIA']>=0.0
df_FORTALEZA=df_FORTALEZA[x]

x=df_FORTALEZA['mwd_PNBOIA']>=0.0
df_FORTALEZA=df_FORTALEZA[x]

x=df_FORTALEZA['mwp_PNBOIA']>=0.0
df_FORTALEZA=df_FORTALEZA[x]









#########################################################################################################################
#########################################################################################################################
#####################################################    SCATTER  PLOTS     ####################################################
#########################################################################################################################
#########################################################################################################################








#########################################################################################################################
#######################################################     RIO_GRANDE  ###################################################
#########################################################################################################################


#######################################################         HS      ##############################################################################################################



##QQPLOTS
#criando linha que corta o eixo para todos os plots
df_RIO_GRANDE['linha_corte']=np.nan
rng = np.random.default_rng()
i=0
while i < len(df_RIO_GRANDE['linha_corte']):
    df_RIO_GRANDE['linha_corte'][i]=rng.integers(0, 360)
    i=i+1
df_RIO_GRANDE['linha_corte'][0]=360

df_RIO_GRANDE['linha_corte2']=np.nan
df_RIO_GRANDE['linha_corte2']=df_RIO_GRANDE['linha_corte']




####        Plotando HS
# Passei os filtros para a parte de Aquisição e tratamento dos dados


#Plotando e calculando correlacao
correlacao=df_RIO_GRANDE['swh_PNBOIA'].corr(df_RIO_GRANDE['swh_ERA5'])
dif=df_RIO_GRANDE['swh_PNBOIA']-df_RIO_GRANDE['swh_ERA5']
media=dif.mean()

p=sns.jointplot(x=df_RIO_GRANDE['swh_PNBOIA'], y=df_RIO_GRANDE['swh_ERA5'], data=df_RIO_GRANDE, 
                xlim=(0, 6), ylim=(0, 6), kind='reg', color='red', height=20, ratio=7)
sns.lineplot(x="linha_corte2", y="linha_corte", data=df_RIO_GRANDE, color='black')
ax = plt.gca()
p.fig.suptitle("Altura Significativa de Onda ERA5 x PNBOIA - Boia Rio Grande (2009-2019)", fontsize=25)
p.ax_joint.set_xlabel('Altura Significativa de Onda - PNBOIA (m)', fontsize=20)
p.ax_joint.set_ylabel('Altura Significativa de Onda - ERA5 (m)', fontsize=20)
p.fig.tight_layout()
p.fig.subplots_adjust(top=0.94) # Reduce plot to make room 
ax.text(0.95, 0.01, 'R= {}'.format(str(correlacao)),
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=20)
plt.savefig('C:\IC PYTHON\Plots Definitivo\RIO GRANDE\qqplot_PNBOIA_ERA5_RIO_GRANDE_swh.png', fontsize=14, dpi=300)
plt.clf() 



#######################################################           Mwd           #######################################################


#######################################################         Mwp             #######################################################     




#####################################################################################################################################################################
#######################################################     ITAJAI  ###################################################
#####################################################################################################################################################################


#######################################################         HS      ##############################################################################################################


##QQPLOTS
#criando linha que corta o eixo para todos os plots
df_ITAJAI['linha_corte']=np.nan
rng = np.random.default_rng()
i=0
while i < len(df_ITAJAI['linha_corte']):
    df_ITAJAI['linha_corte'][i]=rng.integers(0, 360)
    i=i+1
df_ITAJAI['linha_corte'][0]=360

df_ITAJAI['linha_corte2']=np.nan
df_ITAJAI['linha_corte2']=df_ITAJAI['linha_corte']






####        Plotando HS
# Passei os filtros para a parte de Aquisição e tratamento dos dados


#Plotando e calculando correlacao
correlacao=df_ITAJAI['swh_PNBOIA'].corr(df_ITAJAI['swh_ERA5'])
dif=df_ITAJAI['swh_PNBOIA']-df_ITAJAI['swh_ERA5']
media=dif.mean()

p=sns.jointplot(x=df_ITAJAI['swh_PNBOIA'], y=df_ITAJAI['swh_ERA5'], data=df_ITAJAI, 
                xlim=(0, 6), ylim=(0, 6), kind='reg', color='red', height=20, ratio=7)
sns.lineplot(x="linha_corte2", y="linha_corte", data=df_ITAJAI, color='black')
ax = plt.gca()
p.fig.suptitle("Altura Significativa de Onda ERA5 x PNBOIA - Boia Itajaí (2009-2019)", fontsize=25)
p.ax_joint.set_xlabel('Altura Significativa de Onda - PNBOIA (m)', fontsize=20)
p.ax_joint.set_ylabel('Altura Significativa de Onda - ERA5 (m)', fontsize=20)
p.fig.tight_layout()
p.fig.subplots_adjust(top=0.94) # Reduce plot to make room 
ax.text(0.95, 0.01, 'R= {}'.format(str(correlacao)),
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=20)
plt.savefig('C:\IC PYTHON\Plots Definitivo\ITAJAI\qqplot_PNBOIA_ERA5_ITAJAI_swh.png', fontsize=14, dpi=300)
plt.clf() 



#######################################################           Mwd           #######################################################


#######################################################         Mwp             #######################################################     




#########################################################################################################################
#######################################################     SANTOS  ###################################################
#########################################################################################################################


#######################################################         HS      ##############################################################################################################


##QQPLOTS
#criando linha que corta o eixo para todos os plots
df_SANTOS['linha_corte']=np.nan
rng = np.random.default_rng()
i=0
while i < len(df_SANTOS['linha_corte']):
    df_SANTOS['linha_corte'][i]=rng.integers(0, 360)
    i=i+1
df_SANTOS['linha_corte'][0]=360

df_SANTOS['linha_corte2']=np.nan
df_SANTOS['linha_corte2']=df_SANTOS['linha_corte']







####        Plotando HS
# Passei os filtros para a parte de Aquisição e tratamento dos dados


#Plotando e calculando correlacao
correlacao=df_SANTOS['swh_PNBOIA'].corr(df_SANTOS['swh_ERA5'])
dif=df_SANTOS['swh_PNBOIA']-df_SANTOS['swh_ERA5']
media=dif.mean()

p=sns.jointplot(x=df_SANTOS['swh_PNBOIA'], y=df_SANTOS['swh_ERA5'], data=df_SANTOS, 
                xlim=(0, 6), ylim=(0, 6), kind='reg', color='red', height=20, ratio=7)
sns.lineplot(x="linha_corte2", y="linha_corte", data=df_SANTOS, color='black')
ax = plt.gca()
p.fig.suptitle("Altura Significativa de Onda ERA5 x PNBOIA - Boia Santos (2011-2018)", fontsize=25)
p.ax_joint.set_xlabel('Altura Significativa de Onda - PNBOIA (m)', fontsize=20)
p.ax_joint.set_ylabel('Altura Significativa de Onda - ERA5 (m)', fontsize=20)
p.fig.tight_layout()
p.fig.subplots_adjust(top=0.94) # Reduce plot to make room 
ax.text(0.95, 0.01, 'R= {}'.format(str(correlacao)),
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=20)
plt.savefig('C:\IC PYTHON\Plots Definitivo\SANTOS\qqplot_PNBOIA_ERA5_SANTOS_swh.png', fontsize=14, dpi=300)
plt.clf() 



#######################################################           Mwd           #######################################################


#######################################################         Mwp             #######################################################     




#########################################################################################################################
#######################################################     CABO_FRIO  ###################################################
#########################################################################################################################


#######################################################         HS      ##############################################################################################################


##QQPLOTS
#criando linha que corta o eixo para todos os plots
df_CABO_FRIO['linha_corte']=np.nan
rng = np.random.default_rng()
i=0
while i < len(df_CABO_FRIO['linha_corte']):
    df_CABO_FRIO['linha_corte'][i]=rng.integers(0, 360)
    i=i+1
df_CABO_FRIO['linha_corte'][0]=360

df_CABO_FRIO['linha_corte2']=np.nan
df_CABO_FRIO['linha_corte2']=df_CABO_FRIO['linha_corte']







####        Plotando HS
# Passei os filtros para a parte de Aquisição e tratamento dos dados


#Plotando e calculando correlacao
correlacao=df_CABO_FRIO['swh_PNBOIA'].corr(df_CABO_FRIO['swh_ERA5'])
dif=df_CABO_FRIO['swh_PNBOIA']-df_CABO_FRIO['swh_ERA5']
media=dif.mean()

p=sns.jointplot(x=df_CABO_FRIO['swh_PNBOIA'], y=df_CABO_FRIO['swh_ERA5'], data=df_CABO_FRIO, 
                xlim=(0, 6), ylim=(0, 6), kind='reg', color='red', height=20, ratio=7)
sns.lineplot(x="linha_corte2", y="linha_corte", data=df_CABO_FRIO, color='black')
ax = plt.gca()
p.fig.suptitle("Altura Significativa de Onda ERA5 x PNBOIA - Boia Cabo Frio Nova (2016-2018)", fontsize=25)
p.ax_joint.set_xlabel('Altura Significativa de Onda - PNBOIA (m)', fontsize=20)
p.ax_joint.set_ylabel('Altura Significativa de Onda - ERA5 (m)', fontsize=20)
p.fig.tight_layout()
p.fig.subplots_adjust(top=0.94) # Reduce plot to make room 
ax.text(0.95, 0.01, 'R= {}'.format(str(correlacao)),
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=20)
plt.savefig('C:\IC PYTHON\Plots Definitivo\CABO FRIO\qqplot_PNBOIA_ERA5_CABO_FRIO_swh.png', fontsize=14, dpi=300)
plt.clf() 



#######################################################           Mwd           #######################################################


#######################################################         Mwp             #######################################################     




#########################################################################################################################
#######################################################     VITORIA  ###################################################
#########################################################################################################################


#######################################################         HS      ##############################################################################################################



##QQPLOTS
#criando linha que corta o eixo para todos os plots
df_VITORIA['linha_corte']=np.nan
rng = np.random.default_rng()
i=0
while i < len(df_VITORIA['linha_corte']):
    df_VITORIA['linha_corte'][i]=rng.integers(0, 360)
    i=i+1
df_VITORIA['linha_corte'][0]=360

df_VITORIA['linha_corte2']=np.nan
df_VITORIA['linha_corte2']=df_VITORIA['linha_corte']





####        Plotando HS
# Passei os filtros para a parte de Aquisição e tratamento dos dados


#Plotando e calculando correlacao
correlacao=df_VITORIA['swh_PNBOIA'].corr(df_VITORIA['swh_ERA5'])
dif=df_VITORIA['swh_PNBOIA']-df_VITORIA['swh_ERA5']
media=dif.mean()

p=sns.jointplot(x=df_VITORIA['swh_PNBOIA'], y=df_VITORIA['swh_ERA5'], data=df_VITORIA, 
                xlim=(0, 6), ylim=(0, 6), kind='reg', color='red', height=20, ratio=7)
sns.lineplot(x="linha_corte2", y="linha_corte", data=df_VITORIA, color='black')
ax = plt.gca()
p.fig.suptitle("Altura Significativa de Onda ERA5 x PNBOIA - Boia Vitória (2015-2017)", fontsize=25)
p.ax_joint.set_xlabel('Altura Significativa de Onda - PNBOIA (m)', fontsize=20)
p.ax_joint.set_ylabel('Altura Significativa de Onda - ERA5 (m)', fontsize=20)
p.fig.tight_layout()
p.fig.subplots_adjust(top=0.94) # Reduce plot to make room 
ax.text(0.95, 0.01, 'R= {}'.format(str(correlacao)),
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=20)
plt.savefig('C:\IC PYTHON\Plots Definitivo\VITORIA\qqplot_PNBOIA_ERA5_VITORIA_swh.png', fontsize=14, dpi=300)
plt.clf() 






#######################################################           Mwd           #######################################################


#######################################################         Mwp             #######################################################     




#########################################################################################################################
#######################################################     PORTO_SEGURO  ###################################################
#########################################################################################################################


#######################################################         HS      ##############################################################################################################



##QQPLOTS
#criando linha que corta o eixo para todos os plots
df_PORTO_SEGURO['linha_corte']=np.nan
rng = np.random.default_rng()
i=0
while i < len(df_PORTO_SEGURO['linha_corte']):
    df_PORTO_SEGURO['linha_corte'][i]=rng.integers(0, 360)
    i=i+1
df_PORTO_SEGURO['linha_corte'][0]=360

df_PORTO_SEGURO['linha_corte2']=np.nan
df_PORTO_SEGURO['linha_corte2']=df_PORTO_SEGURO['linha_corte']





####        Plotando HS
# Passei os filtros para a parte de Aquisição e tratamento dos dados


#Plotando e calculando correlacao
correlacao=df_PORTO_SEGURO['swh_PNBOIA'].corr(df_PORTO_SEGURO['swh_ERA5'])
dif=df_PORTO_SEGURO['swh_PNBOIA']-df_PORTO_SEGURO['swh_ERA5']
media=dif.mean()

p=sns.jointplot(x=df_PORTO_SEGURO['swh_PNBOIA'], y=df_PORTO_SEGURO['swh_ERA5'], data=df_PORTO_SEGURO, 
                xlim=(0, 6), ylim=(0, 6), kind='reg', color='red', height=20, ratio=7)
sns.lineplot(x="linha_corte2", y="linha_corte", data=df_PORTO_SEGURO, color='black')
ax = plt.gca()
p.fig.suptitle("Altura Significativa de Onda ERA5 x PNBOIA - Boia Porto Seguro (2012-2016)", fontsize=25)
p.ax_joint.set_xlabel('Altura Significativa de Onda - PNBOIA (m)', fontsize=20)
p.ax_joint.set_ylabel('Altura Significativa de Onda - ERA5 (m)', fontsize=20)
p.fig.tight_layout()
p.fig.subplots_adjust(top=0.94) # Reduce plot to make room 
ax.text(0.95, 0.01, 'R= {}'.format(str(correlacao)),
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=20)
plt.savefig('C:\IC PYTHON\Plots Definitivo\PORTO SEGURO\qqplot_PNBOIA_ERA5_PORTO_SEGURO_swh.png', fontsize=14, dpi=300)
plt.clf() 




#######################################################           Mwd           #######################################################


#######################################################         Mwp             #######################################################     




#########################################################################################################################
#######################################################     RECIFE  ###################################################
#########################################################################################################################

#######################################################         HS      ##############################################################################################################



##QQPLOTS
#criando linha que corta o eixo para todos os plots
df_RECIFE['linha_corte']=np.nan
rng = np.random.default_rng()
i=0
while i < len(df_RECIFE['linha_corte']):
    df_RECIFE['linha_corte'][i]=rng.integers(0, 360)
    i=i+1
df_RECIFE['linha_corte'][0]=360

df_RECIFE['linha_corte2']=np.nan
df_RECIFE['linha_corte2']=df_RECIFE['linha_corte']



####        Plotando HS
# Passei os filtros para a parte de Aquisição e tratamento dos dados


#Plotando e calculando correlacao
correlacao=df_RECIFE['swh_PNBOIA'].corr(df_RECIFE['swh_ERA5'])
dif=df_RECIFE['swh_PNBOIA']-df_RECIFE['swh_ERA5']
media=dif.mean()

p=sns.jointplot(x=df_RECIFE['swh_PNBOIA'], y=df_RECIFE['swh_ERA5'], data=df_RECIFE, 
                xlim=(0, 6), ylim=(0, 6), kind='reg', color='red', height=20, ratio=7)
sns.lineplot(x="linha_corte2", y="linha_corte", data=df_RECIFE, color='black')
ax = plt.gca()
p.fig.suptitle("Altura Significativa de Onda ERA5 x PNBOIA - Boia Recife (2012-2016)", fontsize=25)
p.ax_joint.set_xlabel('Altura Significativa de Onda - PNBOIA (m)', fontsize=20)
p.ax_joint.set_ylabel('Altura Significativa de Onda - ERA5 (m)', fontsize=20)
p.fig.tight_layout()
p.fig.subplots_adjust(top=0.94) # Reduce plot to make room 
ax.text(0.95, 0.01, 'R= {}'.format(str(correlacao)),
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=20)
plt.savefig('C:\IC PYTHON\Plots Definitivo\RECIFE\qqplot_PNBOIA_ERA5_RECIFE_swh.png', fontsize=14, dpi=300)
plt.clf() 




#######################################################           Mwd           #######################################################


#######################################################         Mwp             #######################################################     



#########################################################################################################################
#######################################################     FORTALEZA  ###################################################
#########################################################################################################################

#######################################################         HS      ##############################################################################################################



##QQPLOTS
#criando linha que corta o eixo para todos os plots
df_FORTALEZA['linha_corte']=np.nan
rng = np.random.default_rng()
i=0
while i < len(df_FORTALEZA['linha_corte']):
    df_FORTALEZA['linha_corte'][i]=rng.integers(0, 360)
    i=i+1
df_FORTALEZA['linha_corte'][0]=360

df_FORTALEZA['linha_corte2']=np.nan
df_FORTALEZA['linha_corte2']=df_FORTALEZA['linha_corte']






####        Plotando HS
# Passei os filtros para a parte de Aquisição e tratamento dos dados


#Plotando e calculando correlacao
correlacao=df_FORTALEZA['swh_PNBOIA'].corr(df_FORTALEZA['swh_ERA5'])
dif=df_FORTALEZA['swh_PNBOIA']-df_FORTALEZA['swh_ERA5']
media=dif.mean()

p=sns.jointplot(x=df_FORTALEZA['swh_PNBOIA'], y=df_FORTALEZA['swh_ERA5'], data=df_FORTALEZA, 
                xlim=(0, 6), ylim=(0, 6), kind='reg', color='red', height=20, ratio=7)
sns.lineplot(x="linha_corte2", y="linha_corte", data=df_FORTALEZA, color='black')
ax = plt.gca()
p.fig.suptitle("Altura Significativa de Onda ERA5 x PNBOIA - Boia Fortaleza (2016-2018)", fontsize=25)
p.ax_joint.set_xlabel('Altura Significativa de Onda - PNBOIA (m)', fontsize=20)
p.ax_joint.set_ylabel('Altura Significativa de Onda - ERA5 (m)', fontsize=20)
p.fig.tight_layout()
p.fig.subplots_adjust(top=0.94) # Reduce plot to make room 
ax.text(0.95, 0.01, 'R= {}'.format(str(correlacao)),
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=20)
plt.savefig('C:\IC PYTHON\Plots Definitivo\FORTALEZA\qqplot_PNBOIA_ERA5_FORTALEZA_swh.png', fontsize=14, dpi=300)
plt.clf() 





#######################################################           Mwd           #######################################################


#######################################################         Mwp             #######################################################     






#########################################################################################################################
#########################################################################################################################
#########################################################################################################################
#########################################################################################################################
#########################################################################################################################






'''
####plotando mwd

##removendo os flags do vento
#tirando os nans
x=df_RIO_GRANDE['mwd_PNBOIA']>=0.0
df_RIO_GRANDE=df_RIO_GRANDE[x]

#Plotando os 2 ventos e calculando correlacao
correlacao=df_RIO_GRANDE['mwd_PNBOIA'].corr(df_RIO_GRANDE['mwd_ERA5'])
dif=df_RIO_GRANDE['mwd_PNBOIA']-df_RIO_GRANDE['mwd_ERA5']
media=dif.mean()


#Não faz sentido plotar a direção do vento em um QQP

p=sns.jointplot(x=df_RIO_GRANDE['mwd_PNBOIA'], y=df_RIO_GRANDE['mwd_ERA5'], data=df_RIO_GRANDE, 
                xlim=(0, 360), ylim=(0, 360), kind='reg', color='gray', height=11)
sns.lineplot(x="linha_corte2", y="linha_corte", data=df_RIO_GRANDE, color='black')
ax = plt.gca()
p.fig.suptitle("Direção média de Onda - Ponto RIO_GRANDE (2016-2018)")
p.ax_joint.set_xlabel('Direção Média de onda - PNBOIA (m)')
p.ax_joint.set_ylabel('Direção Média de onda - ERA5 (m)')
p.fig.tight_layout()
p.fig.subplots_adjust(top=0.94) # Reduce plot to make room 
ax.text(0.95, 0.01, 'R= {}'.format(str(correlacao)),
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=10)
plt.savefig(path+'\qqplot_PNBOIA_ERA5_RIO_GRANDE_mwd.png', fontsize=10, dpi=300)
plt.clf() 
'''
'''
####plotando pp1d

##removendo os flags do vento
#tirando os nans
x=df_RIO_GRANDE['pp1d_PNBOIA']>=0.0
df_RIO_GRANDE=df_RIO_GRANDE[x]

#Plotando e calculando correlacao
correlacao=df_RIO_GRANDE['pp1d_PNBOIA'].corr(df_RIO_GRANDE['pp1d_ERA5'])
dif=df_RIO_GRANDE['pp1d_PNBOIA']-df_RIO_GRANDE['pp1d_ERA5']
media=dif.mean()

p=sns.jointplot(x=df_RIO_GRANDE['pp1d_PNBOIA'], y=df_RIO_GRANDE['pp1d_ERA5'], data=df_RIO_GRANDE, 
                xlim=(4, 22), ylim=(4, 22), kind='reg', color='gray', height=11)
sns.lineplot(x="linha_corte2", y="linha_corte", data=df_RIO_GRANDE, color='black')
ax = plt.gca()
p.fig.suptitle("Período de pico - Ponto RIO_GRANDE (2009-2019)")
p.ax_joint.set_xlabel('Período de pico de onda - PNBOIA (s)')
p.ax_joint.set_ylabel('Período de pico de onda - ERA5 (s)')
p.fig.tight_layout()
p.fig.subplots_adjust(top=0.94) # Reduce plot to make room 
ax.text(0.95, 0.01, 'R= {}'.format(str(correlacao)),
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=10)
plt.savefig(path+'\qqplot_PNBOIA_ERA5_RIO_GRANDE_pp1d.png', fontsize=10, dpi=300)
plt.clf() 
'''





#########################################################################################################################
###########################################################################################################################
###############################################   ÍNDICES   ###############################################################
#############################################################################################################################
#########################################################################################################################



#########################################################################################################################
##############################################    RIO_GRANDE     ####################################################
#########################################################################################################################


##### PLOTANDO TODOS OS INDICES


##SWH

o1  = df_RIO_GRANDE['swh_PNBOIA'] #Dados observasionais
s1 = df_RIO_GRANDE['swh_ERA5'] #Dados modelados


# Plotting RMSE and NRMSE
#rms = mean_squared_error(y_actual, y_predicted, squared=False)

RMSE_swh = mean_squared_error(o1, s1, squared=False)

NRMSE_swh = (RMSE_swh / o1.mean()) 

# Plotando Coeficiente de correlação
correlacao_swh = o1.corr(s1)

# Plotando bias (tendência)
bias_swh = s1.mean() - o1.mean()

# Plotando Scatter Index
scatter_index_swh = np.sqrt(np.sum( ((s1-s1.mean()) - (o1-o1.mean()))**2)/np.sum(o1**2))

# Plotando HH index
HH_swh = np.sqrt(np.sum((s1 - o1)**2)/np.sum(s1*o1))

# Plotando Nash-Sutcliffe efficiency (NSE)
NSE_swh = sm.nse(s1, o1)




print(bias_swh)
#print(NRMSE_swh)
print(RMSE_swh)
print(correlacao_swh)
print(scatter_index_swh)
print(HH_swh)
print(NSE_swh)


#########################################################################################################################
##############################################    ITAJAI     ####################################################
#########################################################################################################################


##### PLOTANDO TODOS OS INDICES



##SWH

o1  = df_ITAJAI['swh_PNBOIA'] #Dados observasionais
s1 = df_ITAJAI['swh_ERA5'] #Dados modelados


# Plotting RMSE and NRMSE
#rms = mean_squared_error(y_actual, y_predicted, squared=False)

RMSE_swh = mean_squared_error(o1, s1, squared=False)

NRMSE_swh = (RMSE_swh / o1.mean()) 

# Plotando Coeficiente de correlação
correlacao_swh = o1.corr(s1)

# Plotando bias (tendência)
bias_swh = s1.mean() - o1.mean()

# Plotando Scatter Index
scatter_index_swh = np.sqrt(np.sum( ((s1-s1.mean()) - (o1-o1.mean()))**2)/np.sum(o1**2))

# Plotando HH index
HH_swh = np.sqrt(np.sum((s1 - o1)**2)/np.sum(s1*o1))

# Plotando Nash-Sutcliffe efficiency (NSE)
NSE_swh = sm.nse(s1, o1)





print(bias_swh)
#print(NRMSE_swh)
print(RMSE_swh)
print(correlacao_swh)
print(scatter_index_swh)
print(HH_swh)
print(NSE_swh)







#########################################################################################################################
##############################################    SANTOS     ####################################################
#########################################################################################################################


##### PLOTANDO TODOS OS INDICES


##SWH

o1  = df_SANTOS['swh_PNBOIA'] #Dados observasionais
s1 = df_SANTOS['swh_ERA5'] #Dados modelados


# Plotting RMSE and NRMSE
#rms = mean_squared_error(y_actual, y_predicted, squared=False)

RMSE_swh = mean_squared_error(o1, s1, squared=False)

NRMSE_swh = (RMSE_swh / o1.mean()) 

# Plotando Coeficiente de correlação
correlacao_swh = o1.corr(s1)

# Plotando bias (tendência)
bias_swh = s1.mean() - o1.mean()

# Plotando Scatter Index
scatter_index_swh = np.sqrt(np.sum( ((s1-s1.mean()) - (o1-o1.mean()))**2)/np.sum(o1**2))

# Plotando HH index
HH_swh = np.sqrt(np.sum((s1 - o1)**2)/np.sum(s1*o1))

# Plotando Nash-Sutcliffe efficiency (NSE)
NSE_swh = sm.nse(s1, o1)


print(bias_swh)
#print(NRMSE_swh)
print(RMSE_swh)
print(correlacao_swh)
print(scatter_index_swh)
print(HH_swh)
print(NSE_swh)






#########################################################################################################################
##############################################    CABO_FRIO     ####################################################
#########################################################################################################################


##### PLOTANDO TODOS OS INDICES

##SWH

o1  = df_CABO_FRIO['swh_PNBOIA'] #Dados observasionais
s1 = df_CABO_FRIO['swh_ERA5'] #Dados modelados


# Plotting RMSE and NRMSE
#rms = mean_squared_error(y_actual, y_predicted, squared=False)

RMSE_swh = mean_squared_error(o1, s1, squared=False)

NRMSE_swh = (RMSE_swh / o1.mean()) 

# Plotando Coeficiente de correlação
correlacao_swh = o1.corr(s1)

# Plotando bias (tendência)
bias_swh = s1.mean() - o1.mean()

# Plotando Scatter Index
scatter_index_swh = np.sqrt(np.sum( ((s1-s1.mean()) - (o1-o1.mean()))**2)/np.sum(o1**2))

# Plotando HH index
HH_swh = np.sqrt(np.sum((s1 - o1)**2)/np.sum(s1*o1))

# Plotando Nash-Sutcliffe efficiency (NSE)
NSE_swh = sm.nse(s1, o1)





print(bias_swh)
#print(NRMSE_swh)
print(RMSE_swh)
print(correlacao_swh)
print(scatter_index_swh)
print(HH_swh)
print(NSE_swh)



#########################################################################################################################
##############################################    VITORIA     ####################################################
#########################################################################################################################


##### PLOTANDO TODOS OS INDICES

##SWH

o1  = df_VITORIA['swh_PNBOIA'] #Dados observasionais
s1 = df_VITORIA['swh_ERA5'] #Dados modelados


# Plotting RMSE and NRMSE
#rms = mean_squared_error(y_actual, y_predicted, squared=False)

RMSE_swh = mean_squared_error(o1, s1, squared=False)

NRMSE_swh = (RMSE_swh / o1.mean()) 

# Plotando Coeficiente de correlação
correlacao_swh = o1.corr(s1)

# Plotando bias (tendência)
bias_swh = s1.mean() - o1.mean()

# Plotando Scatter Index
scatter_index_swh = np.sqrt(np.sum( ((s1-s1.mean()) - (o1-o1.mean()))**2)/np.sum(o1**2))

# Plotando HH index
HH_swh = np.sqrt(np.sum((s1 - o1)**2)/np.sum(s1*o1))

# Plotando Nash-Sutcliffe efficiency (NSE)
NSE_swh = sm.nse(s1, o1)




print(bias_swh)
#print(NRMSE_swh)
print(RMSE_swh)
print(correlacao_swh)
print(scatter_index_swh)
print(HH_swh)
print(NSE_swh)








#########################################################################################################################
##############################################    PORTO_SEGURO     ####################################################
#########################################################################################################################


##### PLOTANDO TODOS OS INDICES

##SWH

o1  = df_PORTO_SEGURO['swh_PNBOIA'] #Dados observasionais
s1 = df_PORTO_SEGURO['swh_ERA5'] #Dados modelados


# Plotting RMSE and NRMSE
#rms = mean_squared_error(y_actual, y_predicted, squared=False)

RMSE_swh = mean_squared_error(o1, s1, squared=False)

NRMSE_swh = (RMSE_swh / o1.mean()) 

# Plotando Coeficiente de correlação
correlacao_swh = o1.corr(s1)

# Plotando bias (tendência)
bias_swh = s1.mean() - o1.mean()

# Plotando Scatter Index
scatter_index_swh = np.sqrt(np.sum( ((s1-s1.mean()) - (o1-o1.mean()))**2)/np.sum(o1**2))

# Plotando HH index
HH_swh = np.sqrt(np.sum((s1 - o1)**2)/np.sum(s1*o1))

# Plotando Nash-Sutcliffe efficiency (NSE)
NSE_swh = sm.nse(s1, o1)



print(bias_swh)
#print(NRMSE_swh)
print(RMSE_swh)
print(correlacao_swh)
print(scatter_index_swh)
print(HH_swh)
print(NSE_swh)







#########################################################################################################################
##############################################    RECIFE     ####################################################
#########################################################################################################################


##### PLOTANDO TODOS OS INDICES

##SWH

o1  = df_RECIFE['swh_PNBOIA'] #Dados observasionais
s1 = df_RECIFE['swh_ERA5'] #Dados modelados


# Plotting RMSE and NRMSE
#rms = mean_squared_error(y_actual, y_predicted, squared=False)

RMSE_swh = mean_squared_error(o1, s1, squared=False)

NRMSE_swh = (RMSE_swh / o1.mean()) 

# Plotando Coeficiente de correlação
correlacao_swh = o1.corr(s1)

# Plotando bias (tendência)
bias_swh = s1.mean() - o1.mean()

# Plotando Scatter Index
scatter_index_swh = np.sqrt(np.sum( ((s1-s1.mean()) - (o1-o1.mean()))**2)/np.sum(o1**2))

# Plotando HH index
HH_swh = np.sqrt(np.sum((s1 - o1)**2)/np.sum(s1*o1))

# Plotando Nash-Sutcliffe efficiency (NSE)
NSE_swh = sm.nse(s1, o1)




print(bias_swh)
#print(NRMSE_swh)
print(RMSE_swh)
print(correlacao_swh)
print(scatter_index_swh)
print(HH_swh)
print(NSE_swh)







#########################################################################################################################
##############################################    FORTALEZA     ####################################################
#########################################################################################################################


##### PLOTANDO TODOS OS INDICES

##SWH

o1  = df_FORTALEZA['swh_PNBOIA'] #Dados observasionais
s1 = df_FORTALEZA['swh_ERA5'] #Dados modelados


# Plotting RMSE and NRMSE
#rms = mean_squared_error(y_actual, y_predicted, squared=False)

RMSE_swh = mean_squared_error(o1, s1, squared=False)

NRMSE_swh = (RMSE_swh / o1.mean()) 

# Plotando Coeficiente de correlação
correlacao_swh = o1.corr(s1)

# Plotando bias (tendência)
bias_swh = s1.mean() - o1.mean()

# Plotando Scatter Index
scatter_index_swh = np.sqrt(np.sum( ((s1-s1.mean()) - (o1-o1.mean()))**2)/np.sum(o1**2))

# Plotando HH index
HH_swh = np.sqrt(np.sum((s1 - o1)**2)/np.sum(s1*o1))

# Plotando Nash-Sutcliffe efficiency (NSE)
NSE_swh = sm.nse(s1, o1)


print(bias_swh)
#print(NRMSE_swh)
print(RMSE_swh)
print(correlacao_swh)
print(scatter_index_swh)
print(HH_swh)
print(NSE_swh)









#######################################################################################################################################
################################################################  CIRCULARES  ############################################
#######################################################################################################################################





#########################################################################################################################
###############################################         RIO_GRANDE         ###########################################################
#########################################################################################################################


########## DROPAR ALGUMA VARIÁVEL ################
# Exemplo: df_CABO_FRIO.drop(columns=['mwd', 'pp1d', 'hmax', 'swh', 'mwp'], inplace=True)


x=df_RIO_GRANDE['mwd_PNBOIA']>=0.0
df_RIO_GRANDE=df_RIO_GRANDE[x]


##### Coeficiente de Correlação Circular, ou Coeficiente Circular de Pearson

df_RIO_GRANDE_O = df_RIO_GRANDE['mwd_PNBOIA']
df_RIO_GRANDE_S = df_RIO_GRANDE['mwd_ERA5']


array_RIO_GRANDE_O = df_RIO_GRANDE_O.to_numpy()
array_RIO_GRANDE_S = df_RIO_GRANDE_S.to_numpy()


array_RIO_GRANDE_O = np.radians(array_RIO_GRANDE_O)
array_RIO_GRANDE_S = np.radians(array_RIO_GRANDE_S)


alpha = np.array([array_RIO_GRANDE_O])*u.deg
beta = np.array([array_RIO_GRANDE_S])*u.deg


circcorrcoef(alpha, beta)






#########################################################################################################################
###############################################         ITAJAI         ###########################################################
#########################################################################################################################


########## DROPAR ALGUMA VARIÁVEL ################
# Exemplo: df_CABO_FRIO.drop(columns=['mwd', 'pp1d', 'hmax', 'swh', 'mwp'], inplace=True)


x=df_ITAJAI['mwd_PNBOIA']>=0.0
df_ITAJAI=df_ITAJAI[x]


##### Coeficiente de Correlação Circular, ou Coeficiente Circular de Pearson

df_ITAJAI_O = df_ITAJAI['mwd_PNBOIA']
df_ITAJAI_S = df_ITAJAI['mwd_ERA5']


array_ITAJAI_O = df_ITAJAI_O.to_numpy()
array_ITAJAI_S = df_ITAJAI_S.to_numpy()


array_ITAJAI_O = np.radians(array_ITAJAI_O)
array_ITAJAI_S = np.radians(array_ITAJAI_S)


alpha = np.array([array_ITAJAI_O])*u.deg
beta = np.array([array_ITAJAI_S])*u.deg


circcorrcoef(alpha, beta)









#########################################################################################################################
###############################################         SANTOS         ###########################################################
#########################################################################################################################


########## DROPAR ALGUMA VARIÁVEL ################
# Exemplo: df_CABO_FRIO.drop(columns=['mwd', 'pp1d', 'hmax', 'swh', 'mwp'], inplace=True)


x=df_SANTOS['mwd_PNBOIA']>=0.0
df_SANTOS=df_SANTOS[x]


##### Coeficiente de Correlação Circular, ou Coeficiente Circular de Pearson

df_SANTOS_O = df_SANTOS['mwd_PNBOIA']
df_SANTOS_S = df_SANTOS['mwd_ERA5']


array_SANTOS_O = df_SANTOS_O.to_numpy()
array_SANTOS_S = df_SANTOS_S.to_numpy()


array_SANTOS_O = np.radians(array_SANTOS_O)
array_SANTOS_S = np.radians(array_SANTOS_S)


alpha = np.array([array_SANTOS_O])*u.deg
beta = np.array([array_SANTOS_S])*u.deg


circcorrcoef(alpha, beta)








#########################################################################################################################
###############################################         CABO_FRIO         ###########################################################
#########################################################################################################################


########## DROPAR ALGUMA VARIÁVEL ################
# Exemplo: df_CABO_FRIO.drop(columns=['mwd', 'pp1d', 'hmax', 'swh', 'mwp'], inplace=True)


x=df_CABO_FRIO['mwd_PNBOIA']>=0.0
df_CABO_FRIO=df_CABO_FRIO[x]


##### Coeficiente de Correlação Circular, ou Coeficiente Circular de Pearson

df_CABO_FRIO_O = df_CABO_FRIO['mwd_PNBOIA']
df_CABO_FRIO_S = df_CABO_FRIO['mwd_ERA5']


array_CABO_FRIO_O = df_CABO_FRIO_O.to_numpy()
array_CABO_FRIO_S = df_CABO_FRIO_S.to_numpy()


array_CABO_FRIO_O = np.radians(array_CABO_FRIO_O)
array_CABO_FRIO_S = np.radians(array_CABO_FRIO_S)


alpha = np.array([array_CABO_FRIO_O])*u.deg
beta = np.array([array_CABO_FRIO_S])*u.deg


circcorrcoef(alpha, beta)







#########################################################################################################################
###############################################         VITORIA         ###########################################################
#########################################################################################################################


########## DROPAR ALGUMA VARIÁVEL ################
# Exemplo: df_CABO_FRIO.drop(columns=['mwd', 'pp1d', 'hmax', 'swh', 'mwp'], inplace=True)


x=df_VITORIA['mwd_PNBOIA']>=0.0
df_VITORIA=df_VITORIA[x]


##### Coeficiente de Correlação Circular, ou Coeficiente Circular de Pearson

df_VITORIA_O = df_VITORIA['mwd_PNBOIA']
df_VITORIA_S = df_VITORIA['mwd_ERA5']


array_VITORIA_O = df_VITORIA_O.to_numpy()
array_VITORIA_S = df_VITORIA_S.to_numpy()


array_VITORIA_O = np.radians(array_VITORIA_O)
array_VITORIA_S = np.radians(array_VITORIA_S)


alpha = np.array([array_VITORIA_O])*u.deg
beta = np.array([array_VITORIA_S])*u.deg


circcorrcoef(alpha, beta)






#########################################################################################################################
###############################################         PORTO_SEGURO         ###########################################################
#########################################################################################################################


########## DROPAR ALGUMA VARIÁVEL ################
# Exemplo: df_CABO_FRIO.drop(columns=['mwd', 'pp1d', 'hmax', 'swh', 'mwp'], inplace=True)


x=df_PORTO_SEGURO['mwd_PNBOIA']>=0.0
df_PORTO_SEGURO=df_PORTO_SEGURO[x]


##### Coeficiente de Correlação Circular, ou Coeficiente Circular de Pearson

df_PORTO_SEGURO_O = df_PORTO_SEGURO['mwd_PNBOIA']
df_PORTO_SEGURO_S = df_PORTO_SEGURO['mwd_ERA5']


array_PORTO_SEGURO_O = df_PORTO_SEGURO_O.to_numpy()
array_PORTO_SEGURO_S = df_PORTO_SEGURO_S.to_numpy()


array_PORTO_SEGURO_O = np.radians(array_PORTO_SEGURO_O)
array_PORTO_SEGURO_S = np.radians(array_PORTO_SEGURO_S)


alpha = np.array([array_PORTO_SEGURO_O])*u.deg
beta = np.array([array_PORTO_SEGURO_S])*u.deg


circcorrcoef(alpha, beta)









#########################################################################################################################
###############################################         RECIFE         ###########################################################
#########################################################################################################################


########## DROPAR ALGUMA VARIÁVEL ################
# Exemplo: df_CABO_FRIO.drop(columns=['mwd', 'pp1d', 'hmax', 'swh', 'mwp'], inplace=True)


x=df_RECIFE['mwd_PNBOIA']>=0.0
df_RECIFE=df_RECIFE[x]


##### Coeficiente de Correlação Circular, ou Coeficiente Circular de Pearson

df_RECIFE_O = df_RECIFE['mwd_PNBOIA']
df_RECIFE_S = df_RECIFE['mwd_ERA5']


array_RECIFE_O = df_RECIFE_O.to_numpy()
array_RECIFE_S = df_RECIFE_S.to_numpy()


array_RECIFE_O = np.radians(array_RECIFE_O)
array_RECIFE_S = np.radians(array_RECIFE_S)


alpha = np.array([array_RECIFE_O])*u.deg
beta = np.array([array_RECIFE_S])*u.deg


circcorrcoef(alpha, beta)







#########################################################################################################################
###############################################         FORTALEZA         ###########################################################
#########################################################################################################################


########## DROPAR ALGUMA VARIÁVEL ################
# Exemplo: df_CABO_FRIO.drop(columns=['mwd', 'pp1d', 'hmax', 'swh', 'mwp'], inplace=True)


x=df_FORTALEZA['mwd_PNBOIA']>=0.0
df_FORTALEZA=df_FORTALEZA[x]


##### Coeficiente de Correlação Circular, ou Coeficiente Circular de Pearson

df_FORTALEZA_O = df_FORTALEZA['mwd_PNBOIA']
df_FORTALEZA_S = df_FORTALEZA['mwd_ERA5']


array_FORTALEZA_O = df_FORTALEZA_O.to_numpy()
array_FORTALEZA_S = df_FORTALEZA_S.to_numpy()


array_FORTALEZA_O = np.radians(array_FORTALEZA_O)
array_FORTALEZA_S = np.radians(array_FORTALEZA_S)


alpha = np.array([array_FORTALEZA_O])*u.deg
beta = np.array([array_FORTALEZA_S])*u.deg


circcorrcoef(alpha, beta)






#######################################################################################################################
#######################################################################################################################
###########################################   WAVE ROSE  ##############################################################
#######################################################################################################################
#######################################################################################################################

'''
#####################################  PNBOIA
# rosa dos ventos onda
ax = WindroseAxes.from_ax()
ax.bar(df_RIO_GRANDE['mwd_PNBOIA'], df_RIO_GRANDE['swh_PNBOIA'], normed=True, opening=0.12, cmap=cm.rainbow, lw=1, bins=np.arange(1,13,1))
ax.set_title('Wave rose - 2009 a 2019 - PNBOIA (Rio Grande)', fontsize=14)
ax.set_legend(loc=3,decimal_places=1)
#logo = plt.imread('ladsin_2.png')
#ax.figure.figimage(logo, xo = 60, yo = 70)
plt.savefig('C:\\IC PYTHON\\OSM 2022\\wavesrose_RIO_GRANDE_PNBOIA.png', fontsize=15, dpi=300)



#######################################  ERA5
# rosa dos ventos
ax = WindroseAxes.from_ax()
ax.bar(df_RIO_GRANDE['mwd_ERA5'], df_RIO_GRANDE['swh_ERA5'], normed=True, opening=0.73, cmap=cm.rainbow, lw=1, bins=np.arange(1,8,1))
ax.set_title('Wave rose - 2009 a 2019 - ERA5 (Rio Grande)', fontsize=14)
ax.set_legend(loc=3,decimal_places=1)
#logo = plt.imread('ladsin_2.png')
#ax.figure.figimage(logo, xo = 60, yo = 70)
plt.savefig('C:\\IC PYTHON\\OSM 2022\\wavesrose_RIO_GRANDE_ERA5.png', fontsize=15, dpi=300)
'''




#########################################################################################################################
#####################################################       Rio Grande      ##############################################################################
#########################################################################################################################




#####################################  PNBOIA


ax = WindroseAxes.from_ax()
ax.bar(df_RIO_GRANDE['mwd_PNBOIA'], df_RIO_GRANDE['swh_PNBOIA'], normed=True, opening=0.7, edgecolor='black', cmap=cm.rainbow, lw=1, bins=np.arange(1,7,1))
ax.set_title('Rosa de Ondas - 2009 a 2019 - PNBOIA (Rio Grande)', fontsize=15)
ax.set_legend(loc=3, decimal_places=1)
ax.set_xticklabels(['E', 'NE', 'N', 'NW',  'W', 'SW', 'S', 'SE'])
#logo = plt.imread('ladsin_2.png')
#ax.figure.figimage(logo, xo = 60, yo = 70)
plt.savefig('C:\IC PYTHON\Plots Definitivo\RIO GRANDE\wavesrose_RIO_GRANDE_PNBOIA.png') #coloca 2 digitos
plt.clf() #fecha o arquivo para nao plotar por cima



#######################################  ERA5


ax = WindroseAxes.from_ax()
ax.bar(df_RIO_GRANDE['mwd_ERA5'], df_RIO_GRANDE['swh_ERA5'], normed=True, opening=0.7, edgecolor='black', cmap=cm.rainbow, lw=1, bins=np.arange(1,7,1))
ax.set_title('Rosa de Ondas - 2009 a 2019 - ERA 5 (Rio Grande)', fontsize=15)
ax.set_legend(loc=3, decimal_places=1)
ax.set_xticklabels(['E', 'NE', 'N', 'NW',  'W', 'SW', 'S', 'SE'])
#logo = plt.imread('ladsin_2.png')
#ax.figure.figimage(logo, xo = 60, yo = 70)
plt.savefig('C:\IC PYTHON\Plots Definitivo\RIO GRANDE\wavesrose_RIO_GRANDE_ERA5.png') #coloca 2 digitos
plt.clf() #fecha o arquivo para nao plotar por cima



#########################################################################################################################
#####################################################       ITAJAÍ      ##############################################################################
#########################################################################################################################





#####################################  PNBOIA


ax = WindroseAxes.from_ax()
ax.bar(df_ITAJAI['mwd_PNBOIA'], df_ITAJAI['swh_PNBOIA'], normed=True, opening=0.7, edgecolor='black', cmap=cm.rainbow, lw=1, bins=np.arange(1,7,1))
ax.set_title('Rosa de Ondas - 2009 a 2019 - PNBOIA (Itajaí)', fontsize=15)
ax.set_legend(loc=3, decimal_places=1)
ax.set_xticklabels(['E', 'NE', 'N', 'NW',  'W', 'SW', 'S', 'SE'])
#logo = plt.imread('ladsin_2.png')
#ax.figure.figimage(logo, xo = 60, yo = 70)
plt.savefig('C:\IC PYTHON\Plots Definitivo\ITAJAI\wavesrose_ITAJAI_PNBOIA.png') #coloca 2 digitos
plt.clf() #fecha o arquivo para nao plotar por cima



#######################################  ERA5

 
ax = WindroseAxes.from_ax()
ax.bar(df_ITAJAI['mwd_ERA5'], df_ITAJAI['swh_ERA5'], normed=True, opening=0.7, edgecolor='black', cmap=cm.rainbow, lw=1, bins=np.arange(1,7,1))
ax.set_title('Rosa de Ondas - 2009 a 2019 - ERA 5 (Itajaí)', fontsize=15)
ax.set_legend(loc=3, decimal_places=1)
ax.set_xticklabels(['E', 'NE', 'N', 'NW',  'W', 'SW', 'S', 'SE'])
#logo = plt.imread('ladsin_2.png')
#ax.figure.figimage(logo, xo = 60, yo = 70)
plt.savefig('C:\IC PYTHON\Plots Definitivo\ITAJAI\wavesrose_ITAJAI_ERA5.png') #coloca 2 digitos
plt.clf() #fecha o arquivo para nao plotar por cima




#########################################################################################################################
#####################################################       SANTOS      ##############################################################################
#########################################################################################################################


#####################################  PNBOIA


ax = WindroseAxes.from_ax()
ax.bar(df_SANTOS['mwd_PNBOIA'], df_SANTOS['swh_PNBOIA'], normed=True, opening=0.7, edgecolor='black', cmap=cm.rainbow, lw=1, bins=np.arange(1,7,1))
ax.set_title('Rosa de Ondas - 2011 a 2018 - PNBOIA (Santos)', fontsize=15)
ax.set_legend(loc=3, decimal_places=1)
ax.set_xticklabels(['E', 'NE', 'N', 'NW',  'W', 'SW', 'S', 'SE'])
#logo = plt.imread('ladsin_2.png')
#ax.figure.figimage(logo, xo = 60, yo = 70)
plt.savefig('C:\IC PYTHON\Plots Definitivo\SANTOS\wavesrose_SANTOS_PNBOIA.png') #coloca 2 digitos
plt.clf() #fecha o arquivo para nao plotar por cima



#######################################  ERA5


ax = WindroseAxes.from_ax()
ax.bar(df_SANTOS['mwd_ERA5'], df_SANTOS['swh_ERA5'], normed=True, opening=0.7, edgecolor='black', cmap=cm.rainbow, lw=1, bins=np.arange(1,7,1))
ax.set_title('Rosa de Ondas - 2011 a 2018 - ERA 5 (Santos)', fontsize=15)
ax.set_legend(loc=3, decimal_places=1)
ax.set_xticklabels(['E', 'NE', 'N', 'NW',  'W', 'SW', 'S', 'SE'])
#logo = plt.imread('ladsin_2.png')
#ax.figure.figimage(logo, xo = 60, yo = 70)
plt.savefig('C:\IC PYTHON\Plots Definitivo\SANTOS\wavesrose_SANTOS_ERA5.png') #coloca 2 digitos
plt.clf() #fecha o arquivo para nao plotar por cima




#########################################################################################################################
###################################################       CABO_FRIO      ##############################################################################
#########################################################################################################################




#####################################  PNBOIA


ax = WindroseAxes.from_ax()
ax.bar(df_CABO_FRIO['mwd_PNBOIA'], df_CABO_FRIO['swh_PNBOIA'], normed=True, opening=0.7, edgecolor='black', cmap=cm.rainbow, lw=1, bins=np.arange(1,7,1))
ax.set_title('Rosa de Ondas - 2016 a 2018 - PNBOIA (Cabo Frio)', fontsize=15)
ax.set_legend(loc=3, decimal_places=1)
ax.set_xticklabels(['E', 'NE', 'N', 'NW',  'W', 'SW', 'S', 'SE'])
#logo = plt.imread('ladsin_2.png')
#ax.figure.figimage(logo, xo = 60, yo = 70)
plt.savefig('C:\IC PYTHON\Plots Definitivo\CABO FRIO\wavesrose_CABO_FRIO_PNBOIA.png') #coloca 2 digitos
plt.clf() #fecha o arquivo para nao plotar por cima



#######################################  ERA5


ax = WindroseAxes.from_ax()
ax.bar(df_CABO_FRIO['mwd_ERA5'], df_CABO_FRIO['swh_ERA5'], normed=True, opening=0.7, edgecolor='black', cmap=cm.rainbow, lw=1, bins=np.arange(1,7,1))
ax.set_title('Rosa de Ondas - 2016 a 2018 - ERA 5 (Cabo Frio)', fontsize=15)
ax.set_legend(loc=3, decimal_places=1)
ax.set_xticklabels(['E', 'NE', 'N', 'NW',  'W', 'SW', 'S', 'SE'])
#logo = plt.imread('ladsin_2.png')
#ax.figure.figimage(logo, xo = 60, yo = 70)
plt.savefig('C:\IC PYTHON\Plots Definitivo\CABO FRIO\wavesrose_CABO_FRIO_ERA5.png') #coloca 2 digitos
plt.clf() #fecha o arquivo para nao plotar por cima





#########################################################################################################################
#####################################################       VITÓRIA      ##############################################################################
#########################################################################################################################



#####################################  PNBOIA


ax = WindroseAxes.from_ax()
ax.bar(df_VITORIA['mwd_PNBOIA'], df_VITORIA['swh_PNBOIA'], normed=True, opening=0.7, edgecolor='black', cmap=cm.rainbow, lw=1, bins=np.arange(1,7,1))
ax.set_title('Rosa de Ondas - 2015 a 2017 - PNBOIA (Vitória)', fontsize=15)
ax.set_legend(loc=3, decimal_places=1)
ax.set_xticklabels(['E', 'NE', 'N', 'NW',  'W', 'SW', 'S', 'SE'])
#logo = plt.imread('ladsin_2.png')
#ax.figure.figimage(logo, xo = 60, yo = 70)
plt.savefig('C:\IC PYTHON\Plots Definitivo\VITORIA\wavesrose_VITORIA_PNBOIA.png') #coloca 2 digitos
plt.clf() #fecha o arquivo para nao plotar por cima



#######################################  ERA5

 
ax = WindroseAxes.from_ax()
ax.bar(df_VITORIA['mwd_ERA5'], df_VITORIA['swh_ERA5'], normed=True, opening=0.7, edgecolor='black', cmap=cm.rainbow, lw=1, bins=np.arange(1,7,1))
ax.set_title('Rosa de Ondas - 2015 a 2017 - ERA 5 (Vitória)', fontsize=15)
ax.set_legend(loc=3, decimal_places=1)
ax.set_xticklabels(['E', 'NE', 'N', 'NW',  'W', 'SW', 'S', 'SE'])
#logo = plt.imread('ladsin_2.png')
#ax.figure.figimage(logo, xo = 60, yo = 70)
plt.savefig('C:\IC PYTHON\Plots Definitivo\VITORIA\wavesrose_VITORIA_ERA5.png') #coloca 2 digitos
plt.clf() #fecha o arquivo para nao plotar por cima






#########################################################################################################################
#####################################################       Porto Seguro      ##############################################################################
#########################################################################################################################




#####################################  PNBOIA


ax = WindroseAxes.from_ax()
ax.bar(df_PORTO_SEGURO['mwd_PNBOIA'], df_PORTO_SEGURO['swh_PNBOIA'], normed=True, opening=0.7, edgecolor='black', cmap=cm.rainbow, lw=1, bins=np.arange(1,7,1))
ax.set_title('Rosa de Ondas - 2012 a 2016 - PNBOIA (Porto Seguro)', fontsize=15)
ax.set_legend(loc=3, decimal_places=1)
ax.set_xticklabels(['E', 'NE', 'N', 'NW',  'W', 'SW', 'S', 'SE'])
#logo = plt.imread('ladsin_2.png')
#ax.figure.figimage(logo, xo = 60, yo = 70)
plt.savefig('C:\IC PYTHON\Plots Definitivo\PORTO SEGURO\wavesrose_PORTO_SEGURO_PNBOIA.png') #coloca 2 digitos
plt.clf() #fecha o arquivo para nao plotar por cima



#######################################  ERA5

 
ax = WindroseAxes.from_ax()
ax.bar(df_PORTO_SEGURO['mwd_ERA5'], df_PORTO_SEGURO['swh_ERA5'], normed=True, opening=0.7, edgecolor='black', cmap=cm.rainbow, lw=1, bins=np.arange(1,7,1))
ax.set_title('Rosa de Ondas - 2012 a 2016 - ERA 5 (Porto Seguro)', fontsize=15)
ax.set_legend(loc=3, decimal_places=1)
ax.set_xticklabels(['E', 'NE', 'N', 'NW',  'W', 'SW', 'S', 'SE'])
#logo = plt.imread('ladsin_2.png')
#ax.figure.figimage(logo, xo = 60, yo = 70)
plt.savefig('C:\IC PYTHON\Plots Definitivo\PORTO SEGURO\wavesrose_PORTO_SEGURO_ERA5.png') #coloca 2 digitos
plt.clf() #fecha o arquivo para nao plotar por cima







#########################################################################################################################
#####################################################       Recife      ##############################################################################
#########################################################################################################################



#####################################  PNBOIA


ax = WindroseAxes.from_ax()
ax.bar(df_RECIFE['mwd_PNBOIA'], df_RECIFE['swh_PNBOIA'], normed=True, opening=0.7, edgecolor='black', cmap=cm.rainbow, lw=1, bins=np.arange(1,7,1))
ax.set_title('Rosa de Ondas - 2012 a 2016 - PNBOIA (Recife)', fontsize=15)
ax.set_legend(loc=3, decimal_places=1)
ax.set_xticklabels(['E', 'NE', 'N', 'NW',  'W', 'SW', 'S', 'SE'])
#logo = plt.imread('ladsin_2.png')
#ax.figure.figimage(logo, xo = 60, yo = 70)
plt.savefig('C:\IC PYTHON\Plots Definitivo\RECIFE\wavesrose_RECIFE_PNBOIA.png') #coloca 2 digitos
plt.clf() #fecha o arquivo para nao plotar por cima



#######################################  ERA5


ax = WindroseAxes.from_ax()
ax.bar(df_RECIFE['mwd_ERA5'], df_RECIFE['swh_ERA5'], normed=True, opening=0.7, edgecolor='black', cmap=cm.rainbow, lw=1, bins=np.arange(1,7,1))
ax.set_title('Rosa de Ondas - 2012 a 2016 - ERA 5 (Recife)', fontsize=15)
ax.set_legend(loc=3, decimal_places=1)
ax.set_xticklabels(['E', 'NE', 'N', 'NW',  'W', 'SW', 'S', 'SE'])
#logo = plt.imread('ladsin_2.png')
#ax.figure.figimage(logo, xo = 60, yo = 70)
plt.savefig('C:\IC PYTHON\Plots Definitivo\RECIFE\wavesrose_RECIFE_ERA5.png') #coloca 2 digitos
plt.clf() #fecha o arquivo para nao plotar por cima





#########################################################################################################################
#####################################################       Fortaleza      ###################################################################
#########################################################################################################################



#####################################  PNBOIA

 
ax = WindroseAxes.from_ax()
ax.bar(df_FORTALEZA['mwd_PNBOIA'], df_FORTALEZA['swh_PNBOIA'], normed=True, opening=0.7, edgecolor='black', cmap=cm.rainbow, lw=1, bins=np.arange(1,7,1))
ax.set_title('Rosa de Ondas - 2016 a 2018 - PNBOIA (Fortaleza)', fontsize=15)
ax.set_legend(loc=3, decimal_places=1)
ax.set_xticklabels(['E', 'NE', 'N', 'NW',  'W', 'SW', 'S', 'SE'])
#logo = plt.imread('ladsin_2.png')
#ax.figure.figimage(logo, xo = 60, yo = 70)
plt.savefig('C:\IC PYTHON\Plots Definitivo\FORTALEZA\wavesrose_FORTALEZA_PNBOIA.png') #coloca 2 digitos
plt.clf() #fecha o arquivo para nao plotar por cima



#######################################  ERA5


ax = WindroseAxes.from_ax()
ax.bar(df_FORTALEZA['mwd_ERA5'], df_FORTALEZA['swh_ERA5'], normed=True, opening=0.7, edgecolor='black', cmap=cm.rainbow, lw=1, bins=np.arange(1,7,1))
ax.set_title('Rosa de Ondas - 2016 a 2018 - ERA 5 (Fortaleza)', fontsize=15)
ax.set_legend(loc=3, decimal_places=1)
ax.set_xticklabels(['E', 'NE', 'N', 'NW',  'W', 'SW', 'S', 'SE'])
#logo = plt.imread('ladsin_2.png')
#ax.figure.figimage(logo, xo = 60, yo = 70)
plt.savefig('C:\IC PYTHON\Plots Definitivo\FORTALEZA\wavesrose_FORTALEZA_ERA5.png') #coloca 2 digitos
plt.clf() #fecha o arquivo para nao plotar por cima





#######################################################################################################################
#######################################################################################################################
###########################################   WAVE ROSE EXTREMOS   ##############################################################
#######################################################################################################################
#######################################################################################################################

'''
# rosa de ondas
ax = WindroseAxes.from_ax()
ax.bar(df_RIO_GRANDE['mwd_PNBOIA'], df_RIO_GRANDE['swh_PNBOIA'], normed=True, opening=0.7, edgecolor='black', cmap=cm.rainbow, lw=1, bins=np.arange(4,9,1))
ax.set_title('Rosa de Ondas - 2009 a 2019 - Eventos Extremos - PNBOIA (Rio Grande)', fontsize=15)
ax.set_legend(loc=3, decimal_places=1)
ax.set_xticklabels(['E', 'NE', 'N', 'NW',  'W', 'SW', 'S', 'SE'])
#logo = plt.imread('ladsin_2.png')
#ax.figure.figimage(logo, xo = 60, yo = 70)
plt.savefig('C:\IC PYTHON\Plots Definitivo\RIO GRANDE\wavesrose_extremos_RIO_GRANDE_PNBOIA.png', dpi=300) #coloca 2 digitos
plt.clf() #fecha o arquivo para nao plotar por cima
'''