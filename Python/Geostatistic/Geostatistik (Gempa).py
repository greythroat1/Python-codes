#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats


# In[4]:


#Memasukkan data kedalam python
df = pd.read_csv('D:/Geostatistik/query_earthquake_Geostat.csv', sep = ',')

mag = df['mag'].tolist()
#print(mag)

plt.style.use('seaborn')
plt.figure(figsize=(12,8))
plt.hist(mag)
#plt.xticks(np.arange(4,6,0.25))
plt.title('Magnitude Gempa')
plt.xlabel('Magnitude Gempa')
plt.ylabel('Frekuensi Gempa')
plt.show()


# In[4]:


df2 = pd.read_csv('D:/Geostatistik/Frekuensi Gempa terhadap patahan per 2 km (Jarak 0-50 km).csv')
#print(df2)

jarak = df2['Jarak'].tolist()
frek = df2['Frekuens'].tolist()

plt.style.use("seaborn")
plt.figure(figsize=(16,8))
plt.scatter(jarak, frek)
plt.xticks(np.arange(0,52,2))
plt.title('Frekuensi Gempa terhadap Patahan per 2 KM (Dengan Jarak 0-50 km)')
plt.xlabel('Jarak dari patahan (km)')
plt.ylabel('Frekuensi Gempa')
plt.show()


# In[5]:


slope, intercept, r, p, stderr = scipy.stats.linregress(jarak, frek)
line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'
print(line)

x = np.array(jarak)
y = np.array(frek)

fig, ax = plt.subplots()
ax.plot(x, y, linewidth=0, marker='s', label='Titik Gempa')
ax.plot(x, intercept + slope * x, label=line)
ax.set_xlabel('Jarak dari patahan')
ax.set_ylabel('Frekuensi Gempa')
ax.legend(facecolor='white')
plt.show()

R_Sq = r**2
print("Nilai R2 adalah:", R_Sq)


# In[18]:


import statistics

mean = statistics.mean(mag)
median = statistics.median(mag)
mode = statistics.mode(mag)
stdev = statistics.stdev(mag)

print("Mean dari magnitude gempa:", mean)
print("Median dari magnitude gempa:", median)
print("Modus dari magnitude gempa:", mode)
print("Standar Deviasi dari magnitude:", stdev)

