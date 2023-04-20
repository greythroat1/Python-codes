#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import numpy as np

v = [5, 175, 0, 130, 275, 137, 300, 4, 137, 0, 9, 0, 0, 9, 55, 115, 5, 0, 5, 0, 2]
#tanggal = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
hari = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
n = len(v)
ch = []

D = 8.5
r = D/2
A = 3.14*r**2

for i in range (n):
    curah_hujan = v[i]/A*10
    ch.append(curah_hujan)
    #print ("Curah Hujan", i+1, ":", curah_hujan)
    
    if curah_hujan < 0.5 :
        print ("Curah Hujan", i+1, ":", curah_hujan, '---> Berawan')
    if 0.5 <= curah_hujan < 20 :
        print ("Curah Hujan", i+1, ":", curah_hujan, '---> Hujan Ringan')
    if 20 <= curah_hujan < 50:
        print ("Curah Hujan", i+1, ":", curah_hujan, '---> Hujan Sedang')
    if curah_hujan >= 50:
        print ("Curah Hujan", i+1, ":", curah_hujan, '---> Hujan Lebat')
        
plt.style.use('bmh')
plt.figure(figsize=(20,6))
plt.plot(hari,ch)
plt.scatter(hari,ch, color='black')
plt.axhline(y=0.5, color='gray', linestyle='-')
plt.axhline(y=20, color='green', linestyle='-')
plt.axhline(y=50, color='yellow', linestyle='-')
plt.xlim([0,21])
plt.ylim([-1,60])
plt.xticks(np.arange(0,22,1))
plt.yticks(np.arange(0,61,10))
plt.title('Curah Hujan Harian')
plt.xlabel('Hari')
plt.ylabel('Curah Hujan (mm)')
plt.show()


# In[4]:


week_1 = [0.8815815573138209, 30.855354505983733, 0, 22.921120490159343, 48.48698565226015, 24.155334670398695, 52.89489343882926]
week_2 = [0.7052652458510568, 24.155334670398695, 0, 1.5868468031648777, 0, 0, 1.5868468031648777]
week_3 = [9.69739713045203, 20.27637581821788, 0.8815815573138209, 0, 0.8815815573138209, 0, 0.3526326229255284]
n = len(week_1)

ch_week_1 = sum(week_1)/n
ch_week_2 = sum(week_2)/n
ch_week_3 = sum(week_3)/n
print ('Curah Hujan Minggu 1 :', ch_week_1)
print ('Curah Hujan Minggu 2 :', ch_week_2)
print ('Curah Hujan Minggu 3 :', ch_week_3)


# In[ ]:




