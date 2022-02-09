import pandas as pd
from pandas_datareader import data as pdr
import datetime as date
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp 

###########################################
# declarando fechas

enddate = date.datetime(2021,9,16)
startdate = date.datetime(2000,1,1)
###########################################


###########################################
# obteniendo los datos de Yahoo

ipc = pdr.get_data_yahoo('TV', start = startdate, end = enddate)['Close']
##########################################



##########################################
# Graficando los datos de Yahoo
plt.style.use('dark_background')
plt.title('Precios del IPC')
plt.ylabel("Precio")
plt.xlabel("Año")
ipc.plot()
plt.show()
##########################################

last_year = np.log(ipc[-252:])
sigma = last_year.pct_change().std()*(252**0.5)
mu = (last_year[-1:].values / last_year[:1].values) - 1

window = 70
T = 1.0
last_price = ipc[-1:]

sp.random.seed(123)
paths = 10
dt =T/window
S = np.zeros([window], dtype=float)
x = range(0, int(window), 1)

df = pd.DataFrame()
# Figure setup
fig=plt.figure()
axis=fig.add_subplot(111)
for j in range(0, paths):
    S[0]= last_price
    for i in x[:-1]:
        e=sp.random.normal()
        S[i+1]=S[i]+S[i]*(mu-0.5*pow(sigma,2))*dt+sigma*S[i]*sp.sqrt(dt)*e
    df[j] = S   
    plt.plot(x, S,lw=2)
    
plt.title('Caminos con Movimiento Browniano')
axis.set_xlabel('Tiempo (dias)')
axis.set_ylabel('Precio')
axis.grid(True)
plt.style.use('dark_background')
plt.show()

df2 = pd.concat([ipc,df], axis = 0)
df2 = df2.reset_index()
df2 = df2.drop(['index'], axis = 1)
df2.head()

plt.style.use('dark_background')
df3 = df2[-255:]
fig2 = plt.figure(figsize = (16,8))
axis2 = fig2.add_subplot(111)
plt.plot(df3)
plt.title('Simulación de Precio del IPC con Movimiento Browniano')
axis2.set_xlabel('Tiempo (Ultimo año y 3 meses de predicción)')
axis2.set_ylabel('Precio')
axis2.grid(True)
plt.tick_params(
    axis='x',          
    which='both',      
    bottom=False,      
    top=False,         
    labelbottom=False) 
plt.show()