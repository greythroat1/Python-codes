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


# In[56]:


import math
def horizontal(RMSEX, RMSEY):
    RMSE_vertikal = []
    for i in range(len(RMSEX)):
        D2 = math.sqrt(RMSEX[i]**2 + RMSEY[i]**2)
        RMSE_vertikal.append(D2)
        #print("RMSE Vertikal data:", i+1, "=", D2, "Meter")

    for i in range(len(RMSE_vertikal)):
        CE90 = 1.5175*RMSE_vertikal[i]
        print("Ketelitian Horizontal CE90 data:", i+1, "=", round(CE90, 2), "meter")

def vertikal(RMSEZ):
    for i in range(len(RMSEZ)):
        LE90 = 1.6499*RMSEZ[i]
        print("Ketelitian Vertikal LE90 data:", i+1, "=", round(LE90,2), "meter")


# In[57]:


#Ketelitian tanpa GCP
RMSEX = [0.17, 0.11]
RMSEY = [0.22, 0.17]
RMSEZ = [0.75, 0.24]

horizontal(RMSEX, RMSEY)
vertikal(RMSEZ)


# In[7]:


#Ketelitian 5 GCP
RMSEX = [0.04, 0.03]
RMSEY = [0.04, 0.03]
RMSEZ = [0.09, 0.10]

horizontal(RMSEX, RMSEY)
vertikal(RMSEZ)


# In[6]:


#Ketelitian 8 GCP
RMSEX = [0.03, 0.05]
RMSEY = [0.06, 0.03]
RMSEZ = [0.19, 0.29]

horizontal(RMSEX, RMSEY)
vertikal(RMSEZ)


# In[45]:


def ketelitian(bil_skala, interval_kontur):
    for i in range(len(bil_skala)):
        horizontal_1 = 0.2*bil_skala[i]/1000
        horizontal_2 = 0.3*bil_skala[i]/1000
        horizontal_3 = 0.5*bil_skala[i]/1000
        print("Ketelitian Horizontal CE90 Acuan KELAS 1 data:", i+1, "=", horizontal_1, "meter")
        print("Ketelitian Horizontal CE90 Acuan KELAS 2 data:", i+1, "=", horizontal_2, "meter")
        print("Ketelitian Horizontal CE90 Acuan KELAS 3 data:", i+1, "=", horizontal_3, "meter")

    print("------------------------------------")
    
    for i in range(len(interval_kontur)):
        vertikal_1 = 0.5*interval_kontur[i]
        vertikal_2 = 1.5*vertikal_1
        vertikal_3 = 2.5*vertikal_1
        print("Ketelitian Vertikal LE90 Acuan KELAS 1 data:", i+1, "=", vertikal_1, "meter")
        print("Ketelitian Vertikal LE90 Acuan KELAS 2 data:", i+1, "=", vertikal_2, "meter")
        print("Ketelitian Vertikal LE90 Acuan KELAS 3 data:", i+1, "=", vertikal_3, "meter")

bil_skala = [2500, 1500]
interval_kontur = [1, 0.6]

ketelitian(bil_skala, interval_kontur)


# In[43]:


#Volume Hasil Peledakan dengan Metode Teoritis (Geomteri Peledakan)
B = [3, 3]
S = [3.75, 5]
BH = [4, 5]
n = [222, 137]

Density = 1.9

Volume_loss_DT = [2479.77, 3709.28]

Volume_m3 = []
Volume_ton = []
Volume_ton_teoritis = []
Volume_m3_teoritis = []

for i in range(len(B)):
    V_m3 = B[i]*S[i]*BH[i]*n[i]
    print("Volume Teoritis (dalam m3) pada Data", i+1, ":", V_m3, "m3")
    Volume_m3.append(V_m3)

for i in range(len(B)):
    V_ton = Volume_m3[i]*Density
    print("Volume Teoritis (dalam ton) pada Data", i+1, ":", V_ton, "Ton")
    Volume_ton.append(V_ton)

print("------------------------------------------------------------")

for i in range(len(Volume_loss_DT)):
    V_ton_final = Volume_ton[i]-Volume_loss_DT[i]
    print("Volume Teoritis Akhir (dalam ton) pada Data", i+1, ":", V_ton_final, "Ton")
    Volume_ton_teoritis.append(V_ton_final)

for i in range(len(Volume_ton_teoritis)):
    V_m3_final = Volume_ton_teoritis[i]/1.9
    print("Volume Teoritis Akhir (dalam m3) pada Data", i+1, ":", round(V_m3_final, 2), "m3")


# In[44]:


#Kesamaan dan Perbedaan Masing-masing Metode terhadap Metode Teoritis pada Kedua Data
Teoritis = Volume_ton_teoritis
Terrestrial_Map = [16405.45, 14906.75]
Aerial_Map_nogcp = [13518.12, 13188.76]
Aerial_Map_5gcp = [14699.39, 14297.63]
Aerial_Map_8gcp = [15403.59, 14353.72]

Kesamaan_Terr = []
Kesamaan_Aer_nogcp = []
Kesamaan_Aer_5gcp = []
Kesamaan_Aer_8gcp = []
#TERR/TEORITIS*100

for i in range(len(Teoritis)):
    Kesamaan_Terrestrial = Terrestrial_Map[i]/Teoritis[i]*100
    Kesamaan_Aerial_nogcp = Aerial_Map_nogcp[i]/Teoritis[i]*100
    Kesamaan_Aerial_5gcp = Aerial_Map_5gcp[i]/Teoritis[i]*100
    Kesamaan_Aerial_8gcp = Aerial_Map_8gcp[i]/Teoritis[i]*100

    Kesamaan_Terr.append(Kesamaan_Terrestrial)
    Kesamaan_Aer_nogcp.append(Kesamaan_Aerial_nogcp)
    Kesamaan_Aer_5gcp.append(Kesamaan_Aerial_5gcp)
    Kesamaan_Aer_8gcp.append(Kesamaan_Aerial_8gcp)
    
    print("Tingkat Kesamaan Metode Terrestrial Mapping Data", i+1, ":", round(Kesamaan_Terrestrial, 2), "%")
    print("Tingkat Kesamaan Metode Aerial Mapping (Tanpa GCP) Data", i+1, ":", round(Kesamaan_Aerial_nogcp, 2), "%")
    print("Tingkat Kesamaan Metode Aerial Mapping (5 GCP) Data", i+1, ":", round(Kesamaan_Aerial_5gcp, 2), "%")
    print("Tingkat Kesamaan Metode Aerial Mapping (8 GCP) Data", i+1, ":", round(Kesamaan_Aerial_8gcp, 2), "%")

print("-----------------------------------------------")

for i in range(len(Teoritis)):
    Perbedaan_Terrestrial = abs(Kesamaan_Terr[i] - 100)
    Perbedaan_Aerial_nogcp = abs(Kesamaan_Aer_nogcp[i] - 100)
    Perbedaan_Aerial_5gcp = abs(Kesamaan_Aer_5gcp[i] - 100)
    Perbedaan_Aerial_8gcp = abs(Kesamaan_Aer_8gcp[i] - 100)
    print("Tingkat Perbedaan Metode Terrestrial Mapping Data", i+1, ":", round(Perbedaan_Terrestrial, 2), "%")
    print("Tingkat Perbedaan Metode Aerial Mapping (Tanpa GCP) Data", i+1, ":", round(Perbedaan_Aerial_nogcp, 2), "%")
    print("Tingkat Perbedaan Metode Aerial Mapping (5 GCP) Data", i+1, ":", round(Perbedaan_Aerial_5gcp, 2), "%")
    print("Tingkat Perbedaan Metode Aerial Mapping (8 GCP) Data", i+1, ":", round(Perbedaan_Aerial_8gcp, 2), "%")


# In[ ]:





# In[ ]:




