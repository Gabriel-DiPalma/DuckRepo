# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:56:35 2020

@author: uia80364
"""

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime as dt

conn = sqlite3.connect(r'C:\Users\uia80364\Documents\Work\Devs\DOPAC\Concat\FilaR_Saida.db')
query = "SELECT * FROM FilaR_Saida" 

df = pd.read_sql_query(query,conn)

df.drop(columns=['index'], inplace = True)
df.drop(columns=['Taxa'], inplace = True)
df['mediaFimP'] = df['mediaFimP'].astype(float)
df['mediaFimT'] = df['mediaFimT'].astype(float)
df = df[df['TempoCiclo'] < 600]
df = df[df['TempoCiclo'] > 360]
df = df[df['q1'] < 500]
df = df[df['q2'] < 500]
#df = df[df['Q'] < 3]
df['TimeStamp'] = pd.to_datetime(df['TimeStamp']) 
df['Data'] = df['TimeStamp'].dt.strftime('%d-%m-%Y')
df['Key'] = df['Data'].map(str) + '-' + df['Prensa'].map(str)

#pd.plotting.scatter_matrix(df, figsize=(8, 8))
#plt.show()
#plt.savefig("teste_scatter.pdf")