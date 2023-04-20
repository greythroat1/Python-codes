#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import matplotlib.pyplot as plt

#PT MEGA CITRA UTAMA

#Datum Clarke 1866
a1 = 6_378_206.4
b1 = 6_356_583.8

#Datum GRS-80 (1979)
a2 = 6_378_137
b2 = 6_356_752.3141


B = [110.295, 110.365, 110.365, 110.295]
L = [-0.140, -0.140, -0.256, -0.256]
h = [8, 32, 40, 92]
n = len(B)

a_x1 = []
b_y1 = []
c_x2 = []
d_y2 = []

BG_X = []
BG_Y = []

rms = []

luas1_sementara = []
luas2_sementara = []


for i in range (n):
    #mengkonversikan nilai Bujur dan Lintang kedalam derajat
    konversi1 = math.radians(B[i])
    konversi2 = math.radians(L[i])
    sin_lamda = math.sin(konversi1)
    cos_lamda = math.cos(konversi1)
    sin_phi = math.sin(konversi2)
    cos_phi= math.cos(konversi2)
    
    #mencari nilai koordinat kartesian
    e1 = math.sqrt(1 - (b1**2 / a1**2))
    N1 = (a1 / math.sqrt(1 - (e1**2 * (sin_phi**2))))
    X1 = ((N1 + h[i]) * cos_phi * cos_lamda)
    Y1 = ((N1 + h[i]) * cos_phi * sin_lamda)

    e2 = math.sqrt(1 - (b2**2 / a2**2))
    N2 = (a2 / math.sqrt(1 - (e2**2 * (sin_phi**2))))
    X2 = ((N2 + h[i]) * cos_phi * cos_lamda)
    Y2 = ((N2 + h[i]) * cos_phi * sin_lamda)
    
    a_x1.append(X1)
    b_y1.append(Y1)
    c_x2.append(X2)
    d_y2.append(Y2)
    
    #mencari nilai pergeseran
    Besar_Geser_X = (X2-X1)
    Besar_Geser_Y = (Y2-Y1)
    BG_X.append(Besar_Geser_X)
    BG_Y.append(Besar_Geser_Y)
    
    #mencari nilai RMSE
    x_2 = (X2-X1)**2
    y_2 = (Y2-Y1)**2
    error = (x_2+y_2)
    rms.append(error) 
    
    print('Koordinat titik X',i+1, '(Datum Clarke 1866) :', X1, 'm')
    print('Koordinat titik Y',i+1, '(Datum Clarke 1866) :', Y1, 'm')
    print('Koordinat titik X',i+1, '(Datum GRS-80 [1979]) :', X2, 'm')
    print('Koordinat titik Y',i+1, '(Datum GRS-80 [1979]) :', Y2, 'm')
    print('Besar pergeseran titik X',i+1, ':', Besar_Geser_X, 'm')
    print('Besar pergeseran titik Y',i+1, ':', Besar_Geser_Y, 'm')
    print('---')

#mencari nilai pergeseran (lanjutan)    
Besar_Geser_Rata2_X = sum(BG_X)/len(BG_X)
Besar_Geser_Rata2_Y = sum(BG_Y)/len(BG_Y)
Besar_Geser_Rata2 = (Besar_Geser_Rata2_X + Besar_Geser_Rata2_Y) / 2

#mencari nilai RMSE (lanjutan)
error_total = sum(rms)
RMSE = math.sqrt(error_total / len(rms))

#mencari luas WIUP pada kedua datum
titik_akhir1 = (a_x1[3]*b_y1[0]) - (b_y1[3]*a_x1[0])
titik_akhir2 = (c_x2[3]*d_y2[0]) - (d_y2[3]*c_x2[0])
for j in range (len(a_x1)):
    if j < 3:
        area1 = ((a_x1[j]*b_y1[j+1]) - (b_y1[j]*a_x1[j+1]))
        area2 = ((c_x2[j]*d_y2[j+1]) - (d_y2[j]*c_x2[j+1]))
        luas1_sementara.append(area1)
        luas2_sementara.append(area2)
    
    else:
        print()
        
luas1 = abs((sum(luas1_sementara)+titik_akhir1) / 2)
luas2 = abs((sum(luas2_sementara)+titik_akhir2) / 2)


print('Besar pergeseran rata-rata titik X :', Besar_Geser_Rata2_X, 'm')
print('Besar pergeseran rata-rata titik Y :', Besar_Geser_Rata2_Y, 'm')
print('Besar pergeseran rata-rata total :', Besar_Geser_Rata2, 'm')
print()
print('RMSE :', RMSE)
print()
print('Luas WIUP pada Datum Clarke 1866 :', luas1, 'm2')
print('Luas WIUP pada Datum GRS-80 [1979] :', luas2, 'm2')
print()

#mem-plotkan batas-batas WIUP
plt.style.use('seaborn')
plt.figure(figsize=(13,9))
plt.scatter(a_x1, b_y1, color = 'lime', s = 18, label = 'Datum Clarke 1866')
plt.scatter(c_x2, d_y2, color = 'firebrick', s = 18, label = 'Datum GRS-80 [1979]')
plt.title('Perbandingan Batas-Batas WIUP PT MEGA CITRA UTAMA pada Kedua Datum')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best')
plt.show()


# In[2]:


import math
import matplotlib.pyplot as plt
#PT BARATA GUNA PERKASA

#Datum Clarke 1866
a1 = 6_378_206.4
b1 = 6_356_583.8

#Datum GRS-80 (1979)
a2 = 6_378_137
b2 = 6_356_752.3141

B = [110.246, 110.273, 110.273, 110.246]
L = [-0.867, -0.867, -0.927, -0.927]
h = [173, 71, 75, 38]
n = len(B)

a_x1 = []
b_y1 = []
c_x2 = []
d_y2 = []

BG_X = []
BG_Y = []

rms = []

luas1_sementara = []
luas2_sementara = []


for i in range (n):
    #mengkonversikan nilai Bujur dan Lintang kedalam derajat
    konversi1 = math.radians(B[i])
    konversi2 = math.radians(L[i])
    sin_lamda = math.sin(konversi1)
    cos_lamda = math.cos(konversi1)
    sin_phi = math.sin(konversi2)
    cos_phi= math.cos(konversi2)
    
    #mencari nilai koordinat kartesian
    e1 = math.sqrt(1 - (b1**2 / a1**2))
    N1 = (a1 / math.sqrt(1 - (e1**2 * (sin_phi**2))))
    X1 = ((N1 + h[i]) * cos_phi * cos_lamda)
    Y1 = ((N1 + h[i]) * cos_phi * sin_lamda)

    e2 = math.sqrt(1 - (b2**2 / a2**2))
    N2 = (a2 / math.sqrt(1 - (e2**2 * (sin_phi**2))))
    X2 = ((N2 + h[i]) * cos_phi * cos_lamda)
    Y2 = ((N2 + h[i]) * cos_phi * sin_lamda)
    
    a_x1.append(X1)
    b_y1.append(Y1)
    c_x2.append(X2)
    d_y2.append(Y2)
    
    #mencari nilai pergeseran
    Besar_Geser_X = (X2-X1)
    Besar_Geser_Y = (Y2-Y1)
    BG_X.append(Besar_Geser_X)
    BG_Y.append(Besar_Geser_Y)
    
    #mencari nilai RMSE
    x_2 = (X2-X1)**2
    y_2 = (Y2-Y1)**2
    error = (x_2+y_2)
    rms.append(error) 
    
    print('Koordinat titik X',i+1, '(Datum Clarke 1866) :', X1, 'm')
    print('Koordinat titik Y',i+1, '(Datum Clarke 1866) :', Y1, 'm')
    print('Koordinat titik X',i+1, '(Datum GRS-80 [1979]) :', X2, 'm')
    print('Koordinat titik Y',i+1, '(Datum GRS-80 [1979]) :', Y2, 'm')
    print('Besar pergeseran titik X',i+1, ':', Besar_Geser_X, 'm')
    print('Besar pergeseran titik Y',i+1, ':', Besar_Geser_Y, 'm')
    print('---')

#mencari nilai pergeseran (lanjutan)    
Besar_Geser_Rata2_X = sum(BG_X)/len(BG_X)
Besar_Geser_Rata2_Y = sum(BG_Y)/len(BG_Y)
Besar_Geser_Rata2 = (Besar_Geser_Rata2_X + Besar_Geser_Rata2_Y) / 2

#mencari nilai RMSE (lanjutan)
error_total = sum(rms)
RMSE = math.sqrt(error_total / len(rms))

#mencari luas WIUP pada kedua datum
titik_akhir1 = (a_x1[3]*b_y1[0]) - (b_y1[3]*a_x1[0])
titik_akhir2 = (c_x2[3]*d_y2[0]) - (d_y2[3]*c_x2[0])
for j in range (len(a_x1)):
    if j < 3:
        area1 = ((a_x1[j]*b_y1[j+1]) - (b_y1[j]*a_x1[j+1]))
        area2 = ((c_x2[j]*d_y2[j+1]) - (d_y2[j]*c_x2[j+1]))
        luas1_sementara.append(area1)
        luas2_sementara.append(area2)
    
    else:
        print()
        
luas1 = abs((sum(luas1_sementara)+titik_akhir1) / 2)
luas2 = abs((sum(luas2_sementara)+titik_akhir2) / 2)


print('Besar pergeseran rata-rata titik X :', Besar_Geser_Rata2_X, 'm')
print('Besar pergeseran rata-rata titik Y :', Besar_Geser_Rata2_Y, 'm')
print('Besar pergeseran rata-rata total :', Besar_Geser_Rata2, 'm')
print()
print('RMSE :', RMSE)
print()
print('Luas WIUP pada Datum Clarke 1866 :', luas1, 'm2')
print('Luas WIUP pada Datum GRS-80 [1979] :', luas2, 'm2')
print()

#mem-plotkan batas-batas WIUP
plt.style.use('seaborn')
plt.figure(figsize=(12,8))
plt.scatter(a_x1, b_y1, color = 'lime', s = 20, label = 'Datum Clarke 1866')
plt.scatter(c_x2, d_y2, color = 'red', s = 20, label = 'Datum GRS-80 [1979]')
plt.title('Perbandingan Batas-Batas WIUP PT BARATA GUNA PERKASA pada Kedua Datum')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best')
plt.show()


# In[3]:


import math
import matplotlib.pyplot as plt
#PT MODERN CAHAYA MAKMUR

#Datum Clarke 1866
a1 = 6_378_206.4
b1 = 6_356_583.8

#Datum GRS-80 (1979)
a2 = 6_378_137
b2 = 6_356_752.3141


B = [121.681, 121.721, 121.721, 121.741, 121.741, 121.681]
L = [-2.966, -2.966, -3.013, -3.013, -3.050, -3.050]
h = [819, 788, 640, 592, 608, 623]
n = len(B)

a_x1 = []
b_y1 = []
c_x2 = []
d_y2 = []

BG_X = []
BG_Y = []

rms = []

luas1_sementara = []
luas2_sementara = []


for i in range (n):
    #mengkonversikan nilai Bujur dan Lintang kedalam derajat
    konversi1 = math.radians(B[i])
    konversi2 = math.radians(L[i])
    sin_lamda = math.sin(konversi1)
    cos_lamda = math.cos(konversi1)
    sin_phi = math.sin(konversi2)
    cos_phi= math.cos(konversi2)
    
    #mencari nilai koordinat kartesian
    e1 = math.sqrt(1 - (b1**2 / a1**2))
    N1 = (a1 / math.sqrt(1 - (e1**2 * (sin_phi**2))))
    X1 = ((N1 + h[i]) * cos_phi * cos_lamda)
    Y1 = ((N1 + h[i]) * cos_phi * sin_lamda)

    e2 = math.sqrt(1 - (b2**2 / a2**2))
    N2 = (a2 / math.sqrt(1 - (e2**2 * (sin_phi**2))))
    X2 = ((N2 + h[i]) * cos_phi * cos_lamda)
    Y2 = ((N2 + h[i]) * cos_phi * sin_lamda)
    
    a_x1.append(X1)
    b_y1.append(Y1)
    c_x2.append(X2)
    d_y2.append(Y2)
    
    #mencari nilai pergeseran
    Besar_Geser_X = (X2-X1)
    Besar_Geser_Y = (Y2-Y1)
    BG_X.append(Besar_Geser_X)
    BG_Y.append(Besar_Geser_Y)
    
    #mencari nilai RMSE
    x_2 = (X2-X1)**2
    y_2 = (Y2-Y1)**2
    error = (x_2+y_2)
    rms.append(error) 
    
    print('Koordinat titik X',i+1, '(Datum Clarke 1866) :', X1, 'm')
    print('Koordinat titik Y',i+1, '(Datum Clarke 1866) :', Y1, 'm')
    print('Koordinat titik X',i+1, '(Datum GRS-80 [1979]) :', X2, 'm')
    print('Koordinat titik Y',i+1, '(Datum GRS-80 [1979]) :', Y2, 'm')
    print('Besar pergeseran titik X',i+1, ':', Besar_Geser_X, 'm')
    print('Besar pergeseran titik Y',i+1, ':', Besar_Geser_Y, 'm')
    print('---')

#mencari nilai pergeseran (lanjutan)    
Besar_Geser_Rata2_X = sum(BG_X)/len(BG_X)
Besar_Geser_Rata2_Y = sum(BG_Y)/len(BG_Y)
Besar_Geser_Rata2 = (Besar_Geser_Rata2_X + Besar_Geser_Rata2_Y) / 2

#mencari nilai RMSE (lanjutan)
error_total = sum(rms)
RMSE = math.sqrt(error_total / len(rms))

#mencari luas WIUP pada kedua datum
titik_akhir1 = (a_x1[5]*b_y1[0]) - (b_y1[5]*a_x1[0])
titik_akhir2 = (c_x2[5]*d_y2[0]) - (d_y2[5]*c_x2[0])
for j in range (len(a_x1)):
    if j < 5:
        area1 = ((a_x1[j]*b_y1[j+1]) - (b_y1[j]*a_x1[j+1]))
        area2 = ((c_x2[j]*d_y2[j+1]) - (d_y2[j]*c_x2[j+1]))
        luas1_sementara.append(area1)
        luas2_sementara.append(area2)
    
    else:
        print()
        
luas1 = abs((sum(luas1_sementara)+titik_akhir1) / 2)
luas2 = abs((sum(luas2_sementara)+titik_akhir2) / 2)


print('Besar pergeseran rata-rata titik X :', Besar_Geser_Rata2_X, 'm')
print('Besar pergeseran rata-rata titik Y :', Besar_Geser_Rata2_Y, 'm')
print('Besar pergeseran rata-rata total :', Besar_Geser_Rata2, 'm')
print()
print('RMSE :', RMSE)
print()
print('Luas WIUP pada Datum Clarke 1866 :', luas1, 'm2')
print('Luas WIUP pada Datum GRS-80 [1979] :', luas2, 'm2')
print()

#mem-plotkan batas-batas WIUP
plt.style.use('seaborn')
plt.figure(figsize=(12,8))
plt.scatter(a_x1, b_y1, color = 'lime', s = 20, label = 'Datum Clarke 1866')
plt.scatter(c_x2, d_y2, color = 'crimson', s = 20, label = 'Datum GRS-80 [1979]')
plt.title('Perbandingan Batas-Batas WIUP PT MODERN CAHAYA MAKMUR pada Kedua Datum')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best')
plt.show()


# In[4]:


import math
import matplotlib.pyplot as plt
#PT SELATAN ARC MINERALS

#Datum Clarke 1866
a1 = 6_378_206.4
b1 = 6_356_583.8

#Datum GRS-80 (1979)
a2 = 6_378_137
b2 = 6_356_752.3141


B = [117.408, 117.475, 117.475, 117.408, 117.408, 117.417, 117.417, 117.408]
L = [-8.892, -8.892, -9.017, -9.017, -8.975, -8.975, -8.925, -8.925]
h = [566, 740, 140, 675, 575, 475, 579, 797]
n = len(B)

a_x1 = []
b_y1 = []
c_x2 = []
d_y2 = []

BG_X = []
BG_Y = []

rms = []

luas1_sementara = []
luas2_sementara = []


for i in range (n):
    #mengkonversikan nilai Bujur dan Lintang kedalam derajat
    konversi1 = math.radians(B[i])
    konversi2 = math.radians(L[i])
    sin_lamda = math.sin(konversi1)
    cos_lamda = math.cos(konversi1)
    sin_phi = math.sin(konversi2)
    cos_phi= math.cos(konversi2)
    
    #mencari nilai koordinat kartesian
    e1 = math.sqrt(1 - (b1**2 / a1**2))
    N1 = (a1 / math.sqrt(1 - (e1**2 * (sin_phi**2))))
    X1 = ((N1 + h[i]) * cos_phi * cos_lamda)
    Y1 = ((N1 + h[i]) * cos_phi * sin_lamda)

    e2 = math.sqrt(1 - (b2**2 / a2**2))
    N2 = (a2 / math.sqrt(1 - (e2**2 * (sin_phi**2))))
    X2 = ((N2 + h[i]) * cos_phi * cos_lamda)
    Y2 = ((N2 + h[i]) * cos_phi * sin_lamda)
    
    a_x1.append(X1)
    b_y1.append(Y1)
    c_x2.append(X2)
    d_y2.append(Y2)
    
    #mencari nilai pergeseran
    Besar_Geser_X = (X2-X1)
    Besar_Geser_Y = (Y2-Y1)
    BG_X.append(Besar_Geser_X)
    BG_Y.append(Besar_Geser_Y)
    
    #mencari nilai RMSE
    x_2 = (X2-X1)**2
    y_2 = (Y2-Y1)**2
    error = (x_2+y_2)
    rms.append(error) 
    
    print('Koordinat titik X',i+1, '(Datum Clarke 1866) :', X1, 'm')
    print('Koordinat titik Y',i+1, '(Datum Clarke 1866) :', Y1, 'm')
    print('Koordinat titik X',i+1, '(Datum GRS-80 [1979]) :', X2, 'm')
    print('Koordinat titik Y',i+1, '(Datum GRS-80 [1979]) :', Y2, 'm')
    print('Besar pergeseran titik X',i+1, ':', Besar_Geser_X, 'm')
    print('Besar pergeseran titik Y',i+1, ':', Besar_Geser_Y, 'm')
    print('---')

#mencari nilai pergeseran (lanjutan)    
Besar_Geser_Rata2_X = sum(BG_X)/len(BG_X)
Besar_Geser_Rata2_Y = sum(BG_Y)/len(BG_Y)
Besar_Geser_Rata2 = (Besar_Geser_Rata2_X + Besar_Geser_Rata2_Y) / 2

#mencari nilai RMSE (lanjutan)
error_total = sum(rms)
RMSE = math.sqrt(error_total / len(rms))

#mencari luas WIUP pada kedua datum
titik_akhir1 = (a_x1[7]*b_y1[0]) - (b_y1[7]*a_x1[0])
titik_akhir2 = (c_x2[7]*d_y2[0]) - (d_y2[7]*c_x2[0])
for j in range (len(a_x1)):
    if j < 7:
        area1 = ((a_x1[j]*b_y1[j+1]) - (b_y1[j]*a_x1[j+1]))
        area2 = ((c_x2[j]*d_y2[j+1]) - (d_y2[j]*c_x2[j+1]))
        luas1_sementara.append(area1)
        luas2_sementara.append(area2)
        
    else:
        print()
        
luas1 = abs((sum(luas1_sementara)+titik_akhir1) / 2)
luas2 = abs((sum(luas2_sementara)+titik_akhir2) / 2)


print('Besar pergeseran rata-rata titik X :', Besar_Geser_Rata2_X, 'm')
print('Besar pergeseran rata-rata titik Y :', Besar_Geser_Rata2_Y, 'm')
print('Besar pergeseran rata-rata total :', Besar_Geser_Rata2, 'm')
print()
print('RMSE :', RMSE)
print()
print('Luas WIUP pada Datum Clarke 1866 :', luas1, 'm2')
print('Luas WIUP pada Datum GRS-80 [1979] :', luas2, 'm2')
print()

#mem-plotkan batas-batas WIUP
plt.style.use('seaborn')
plt.figure(figsize=(12,8))
plt.scatter(a_x1, b_y1, color = 'lime', s = 18, label = 'Datum Clarke 1866')
plt.scatter(c_x2, d_y2, color = 'crimson', s = 18, label = 'Datum GRS-80 [1979]')
plt.title('Perbandingan Batas-Batas WIUP PT SELATAN ARC MINERALS pada Kedua Datum')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best')
plt.show()


# In[ ]:




