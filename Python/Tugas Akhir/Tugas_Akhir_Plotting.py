#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style


# In[4]:


# creating the dataset (DATA 1)
data = {'Teoritis':16501.23, 
        'Terrestrial Mapping':16405.45, 
        'Aerial Mapping\n(Tanpa GCP)':13518.12, 
        'Aerial Mapping\n(5 GCP)':14699.39, 
        'Aerial Mapping\n(8 GCP)':15403.59}

methods = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (12, 8))
 
# creating the bar plot
plt.bar(methods, values, color=['slategrey', 'firebrick', 'mediumseagreen', 'tan', 'royalblue'],
        width = 0.5)
 
#plt.style.use("bmh")
#plt.style.use('seaborn-v0_8-whitegrid')
plt.style.use('seaborn-v0_8')
plt.xlabel("Metode", fontsize=22)
plt.xticks(rotation=30)
plt.ylabel("Tonase (Ton)", fontsize=22)
plt.ylim(12000,17000)
plt.yticks(np.arange(12000,17500,500))
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.title("Volume Hasil Peledakan pada Data 1", fontsize=22)
plt.show()


# In[5]:


# creating the dataset (DATA 2)

data_2 = {'Teoritis':15813.22, 
        'Terrestrial Mapping':14906.75, 
        'Aerial Mapping\n(Tanpa GCP)':13188.76, 
        'Aerial Mapping\n(5 GCP)':14297.63, 
        'Aerial Mapping\n(8 GCP)':14353.72}

methods = list(data_2.keys())
values_2 = list(data_2.values())
  
fig = plt.figure(figsize = (12, 8))
 
# creating the bar plot
plt.bar(methods, values_2, color=['slategrey', 'firebrick', 'mediumseagreen', 'tan', 'royalblue'],
        width = 0.5)
 

#plt.style.use("bmh")
#plt.style.use('seaborn-v0_8-whitegrid')
plt.style.use('seaborn-v0_8')
plt.xlabel("Metode", fontsize=22)
plt.xticks(rotation=30)
plt.ylabel("Tonase (Ton)", fontsize=22)
plt.ylim(12000,17000)
plt.yticks(np.arange(12000,17500,500))
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.title("Volume Hasil Peledakan pada Data 2", fontsize=22)
plt.show()


# In[38]:


# Tingkat perbedaan (DATA 1)
data = {'Terrestrial Mapping':0.58, 
        'Aerial Mapping\n(Tanpa GCP)':18.08, 
        'Aerial Mapping\n(5 GCP)':10.92, 
        'Aerial Mapping\n(8 GCP)':6.65}

methods = list(data.keys())
values = list(data.values())

plt.figure(figsize = (12, 8))
plt.barh(methods, values, color=['firebrick', 'mediumseagreen', 'tan', 'royalblue'],
         height = 0.4)

plt.style.use('seaborn-v0_8')
plt.ylabel("Metode", fontsize=22)
#plt.yticks(rotation="vertical")
plt.gca().invert_yaxis()
plt.xlabel("Perbedaan (%)", fontsize=22)
plt.xlim(0,100)
plt.xticks(np.arange(0,110,10))
plt.rc('ytick', labelsize=18)
plt.rc('xtick', labelsize=18)
plt.title("Tingkat Perbedaan Masing-masing Metode\nterhadap Metode Teoritis pada Data 1\n(*Semakin kecil, semakin mendekati nilai Teoritis)",
          fontsize=22)
plt.show()


# In[39]:


# Tingkat perbedaan (DATA 2)
data = {'Terrestrial Mapping':5.73, 
        'Aerial Mapping\n(Tanpa GCP)':16.6, 
        'Aerial Mapping\n(5 GCP)':9.58, 
        'Aerial Mapping\n(8 GCP)':9.22}

methods = list(data.keys())
values = list(data.values())

plt.figure(figsize = (12, 8))
plt.barh(methods, values, color=['firebrick', 'mediumseagreen', 'tan', 'royalblue'],
         height = 0.4)

plt.style.use('seaborn-v0_8')
plt.ylabel("Metode", fontsize=22)
#plt.yticks(rotation="vertical")
plt.gca().invert_yaxis()
plt.xlabel("Perbedaan (%)", fontsize=22)
plt.xlim(0,100)
plt.xticks(np.arange(0,110,10))
plt.rc('ytick', labelsize=18)
plt.rc('xtick', labelsize=18)
plt.title("Tingkat Perbedaan Masing-masing Metode\nterhadap Metode Teoritis pada Data 2\n(*Semakin kecil, semakin mendekati nilai Teoritis)",
          fontsize=22)
plt.show()


# In[43]:


# Durasi Data 1

methods = ["Terrestrial Mapping", "Aerial Mapping\n(Tanpa GCP)", "Aerial Mapping\n(Menggunakan GCP)"]
obtain_data = [300, 7, 7]
process_data = [9, 78, 108]
legend = ["Pengambilan Data", "Pengolahan Data"]

plt.figure(figsize = (12, 8))

plt.bar(methods, obtain_data, width=0.4, color="lightcoral")
plt.bar(methods, process_data, bottom=obtain_data, width=0.4, color="cornflowerblue") 
plt.xlabel("\nMetode", fontsize=22)
plt.ylabel("Waktu (menit)", fontsize=22)
plt.ylim(0,350)
plt.yticks(np.arange(0,400,50))
plt.rc('ytick', labelsize=18)
plt.rc('xtick', labelsize=18)
plt.title("Durasi Pengambilan dan Pengolahan Data Masing-masing Metode\npada Data 1",
          fontsize=22)
plt.legend(legend, loc='upper right', fontsize=15)
plt.show()


# In[45]:


# Durasi Data 2

methods = ["Terrestrial Mapping", "Aerial Mapping\n(Tanpa GCP)", "Aerial Mapping\n(Menggunakan GCP)"]
obtain_data = [180, 2, 2]
process_data = [11, 33, 63]
legend = ["Pengambilan Data", "Pengolahan Data"]

plt.figure(figsize = (12, 8))

plt.bar(methods, obtain_data, width=0.4, color="lightcoral")
plt.bar(methods, process_data, bottom=obtain_data, width=0.4, color="cornflowerblue") 
plt.xlabel("\nMetode", fontsize=22)
plt.ylabel("Waktu (menit)", fontsize=22)
plt.ylim(0,250)
plt.yticks(np.arange(0,300,50))
plt.rc('ytick', labelsize=18)
plt.rc('xtick', labelsize=18)
plt.title("Durasi Pengambilan dan Pengolahan Data Masing-masing Metode\npada Data 2",
          fontsize=22)
plt.legend(legend, loc='upper right', fontsize=14)
plt.show()


# In[47]:


# Rata-rata durasi dari kedua metode
data_1 = {'Terrestrial Mapping':250, 
        'Aerial Mapping\n(Tanpa GCP)':60, 
        'Aerial Mapping\n(Menggunakan GCP)':90}

methods = list(data_1.keys())
values_1 = list(data_1.values())


# creating the bar plot
plt.figure(figsize = (12, 8))
plt.bar(methods, values_1, color=['firebrick', 'mediumseagreen', 'rebeccapurple'],
        width = 0.4)


#plt.style.use("bmh")
#plt.style.use('seaborn-v0_8-whitegrid')
plt.style.use('seaborn-v0_8')
plt.xlabel("\nMetode", fontsize=22)
#plt.xticks(rotation=30)
plt.ylabel("Waktu (menit)", fontsize=22)
plt.ylim(0,250)
plt.yticks(np.arange(0,300,25))
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.title("Rata-rata Durasi Waktu Memperoleh Data", fontsize=22)
plt.show()

