#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[2]:


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


# In[3]:


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


# In[4]:


def horizontal(RMSEX, RMSEY):
    RMSE_vertikal = []
    for i in range(len(RMSEX)):
        D2 = math.sqrt(RMSEX[i]**2 + RMSEY[i]**2)
        RMSE_vertikal.append(D2)

    for i in range(len(RMSE_vertikal)):
        CE90 = 1.5175*RMSE_vertikal[i]
        print("Ketelitian Horizontal CE90 data:", i+1, "=", round(CE90, 2), "meter")

def vertikal(RMSEZ):
    for i in range(len(RMSEZ)):
        LE90 = 1.6499*RMSEZ[i]
        print("Ketelitian Vertikal LE90 data:", i+1, "=", round(LE90,2), "meter")


# In[5]:


#Ketelitian tanpa GCP
RMSEX = [0.17, 0.11]
RMSEY = [0.22, 0.17]
RMSEZ = [0.75, 0.24]

print("Hasil Ketelitian Foto Udara Tanpa Menggunakan GCP:")
horizontal(RMSEX, RMSEY)
vertikal(RMSEZ)


# In[6]:


#Ketelitian 5 GCP
RMSEX = [0.04, 0.03]
RMSEY = [0.04, 0.03]
RMSEZ = [0.09, 0.10]

print("Hasil Ketelitian Foto Udara Menggunakan 5 GCP:")
horizontal(RMSEX, RMSEY)
vertikal(RMSEZ)


# In[7]:


#Ketelitian 8 GCP
RMSEX = [0.03, 0.05]
RMSEY = [0.06, 0.03]
RMSEZ = [0.19, 0.29]

print("Hasil Ketelitian Foto Udara Menggunakan 8 GCP:")
horizontal(RMSEX, RMSEY)
vertikal(RMSEZ)


# In[8]:


#Membuat Ketelitian Acuan
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


# In[1]:


import math
math.sqrt(0.17**2 + 0.22**2)


# In[2]:


0.28*1.5175


# In[3]:


1.6499*0.75


# In[6]:


0.5 * 2500 / 1000


# In[7]:


1.5 * 0.5


# In[8]:


23.660-12.797


# In[1]:


import math
XA = 100.4726791944
XB = 100.472991
YA = 0.96766667
YB = 0.96755000

az = math.atan((XB-XA)/(YB-YA))
print(az)


# In[2]:


print(XB-XA)


# In[3]:


print(YB-YA)


# In[1]:


import math
XA = 106991.96
XB = 106979.03
YA = 663893.95
YB = 663902.08

az = math.atan((XB-XA)/(YB-YA))
print(az)


# In[ ]:




