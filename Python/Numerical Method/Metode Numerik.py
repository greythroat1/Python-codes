#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
import time
from IPython.display import clear_output
import matplotlib.pyplot as plt
import pandas as pd


# In[3]:


#Membuat fungsi dari garis (dengan n = 2)
def fungsi_fx(x):
    fx = 2*(x)+12
    return fx

#Golden Search Section
r = (math.sqrt(5)-1) / 2
xl = 4
xu = 10

def golden_search_min(xl,xu,e):
    it = 0
    while e >= 0.05:
        d = r*(xu-xl)
        x1 = xl+d
        x2 = xu-d
        fx1 = fungsi_fx(x1)
        fx2 = fungsi_fx(x2)
        clear_output(wait=True)
        
        if fx2>fx1:
            xl = x2
            xu = xu
            x2 = x1
            x1 = xl + (r*(xu-xl))
            xopt = x1
        
        else:
            xl = xl
            xu = x1
            x1 = x2
            x2 = xu - (r*(xu-xl))
            xopt = x2
        it+=1
        print('Iterasi:', it)
        print('xl:', xl)
        print('xu:', xu)
        print('fx optimum:', fungsi_fx(xopt))
        
        e = ((1-r)*(abs((xu-xl) / xopt))) * 100
        print('Error:', e, '%')
        
        #Mencari jarak antara dua titik koordinat (dengan n = 2)
        titik_x1 = 4
        titik_y1 = 22
        d_jarak = math.sqrt((titik_x1-xopt)**2 + (titik_y1-fungsi_fx(xopt))**2)
        print('Jarak antara dua titik koordinat:', d_jarak, 'satuan unit')
        
        time.sleep(3)

golden_search_min(4,10,1)


# In[7]:


import matplotlib.pyplot as plt
import pandas as pd

#Memasukkan data kedalam python
df = pd.read_csv('D:\Tugas Metode Numerik/truck_7.txt', sep = ';')

t = df['time(s)'].tolist()
v = df['velocity(m/s)'].tolist()

#Menghitung jarak yang ditempuh
def trapezoid(x,y,h):
    L = (h/2)*((y[0]+2*(sum(y[1:-1]))+y[-1]))
    return L

S = trapezoid(t,v,2)
print('Jarak yang ditempuh:', S, 'm')

#Mem-plotkan hasil
plt.figure(figsize=(12,8))
plt.plot(t,v,'c')
plt.plot(t,v,'r.')
plt.xlabel('time(s)')
plt.ylabel('speed(m/s)')
plt.show()


# In[ ]:




