#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
from matplotlib import pyplot as plt
def hitung_nilai(data_nilai):
    total = sum(data_nilai)
    n = len(data_nilai)
    minimum = min(data_nilai)
    maximum = max(data_nilai)
    rata_rata_nilai = total/n
    A = []
    AB = []
    B = []
    BC = []
    C = []
    D = []
    E = []
    di_atas_rata_rata = []
    di_bawah_rata_rata = []
    for i in (data_nilai):
        if i >= 87:
            A.append(i)
        elif i in range (78,87):
            AB.append(i)
        elif i in range (69,78):
            B.append(i)
        elif i in range (60,69):
            BC.append(i)
        elif i in range (51,60):
            C.append(i)
        elif i in range (41,51):
            D.append(i)
        else:
            E.append(i)
        if i > rata_rata_nilai:
            di_atas_rata_rata.append(i)
        else:
            di_bawah_rata_rata.append(i)
    nilai_A = len(A)
    nilai_AB = len(AB)
    nilai_B = len(B)
    nilai_BC = len(BC)
    nilai_C = len(C)
    nilai_D = len(D)
    nilai_E = len(E)
    di_atas = len(di_atas_rata_rata)
    di_bawah = len(di_bawah_rata_rata)
    return(total, minimum, maximum, rata_rata_nilai, nilai_A, nilai_AB, nilai_B, nilai_BC, nilai_C, nilai_D, nilai_E, di_atas, di_bawah)
nilai = [40,55,75,65,71,93,73,88,60,91,95,80,78,84,45,30,55]
hasil = hitung_nilai(nilai)
print("total:", hasil[0])
print("nilai minimum:", hasil[1])
print("nilai maximum:", hasil[2])
print("rata-rata nilai:", hasil[3])
print("jumlah nilai A:", hasil[4])
print("jumlah nilai AB:", hasil[5])
print("jumlah nilai B:", hasil[6])
print("jumlah nilai BC:", hasil[7])
print("jumlah nilai C:", hasil[8])
print("jumlah nilai D:", hasil[9])
print("jumlah nilai E:", hasil[10])
print("jumlah mahasiswa dengan nilai di atas rata-rata:", hasil[11])
print("jumlah mahasiswa dengan nilai di bawah rata-rata:", hasil[12])
x = ("A", "AB", "B", "BC", "C", "D", "E")
y = (hasil[4:11])
plt.bar(x,y)
plt.xlabel("nilai")
plt.ylabel("jumlah")
plt.grid(True)
plt.show()


# In[32]:


import math
from matplotlib import pyplot as plt
phi = math.pi
maxim = 10
L1 = 0.25
L2 = 0.5
g = 10
x = []
y1 = []
y2 = []
for e in range (60):
    perioda1 = 2*phi*math.sqrt(L1/g)
    perioda2 = 2*phi*math.sqrt(L2/g)
    teta1 = maxim*math.cos((2*phi/perioda1)*(e*0.1))
    teta2 = maxim*math.cos((2*phi/perioda2)*(e*0.1))
    x.append(e)
    y1.append(teta1)
    y2.append(teta2)
plt.plot(x,y1, label= "l=0.25")
plt.plot(x,y2, label= "l=0.5")
plt.xlabel("time(s)")
plt.ylabel("theta")
plt.legend(loc="best")
plt.grid(True)
plt.show()


# In[8]:


from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv("D:/Gempa Dunia.csv", index_col=0)
df1=pd.read_csv("D:/Gempa di Indo.csv", index_col=0)
df.head()
df1.head()

print("Jumlah gempa seluruh dunia:" +str(len(df["mag"])), "kejadian")
print("Jumlah gempa di Indonesia:" +str(len(df1["mag"])), "kejadian")
print("Magnitudo minimum:" +str(min(df["mag"])))
print("Magnitudo maximum:" +str(max(df["mag"])))
print("Magnitudo rata-rata:" +str(sum(df["mag"]/len(df["mag"]))))

df.plot.scatter(x="longitude", y="latitude", label="Gempa di Dunia", color="blue")
df1.plot.scatter(x="longitude", y="latitude", label="Gempa di Indonesia", color="red")
plt.title("LOKASI KEJADIAN GEMPA")
plt.xlabel("Bujur")
plt.ylabel("Lintang")
plt.legend(loc="best")
plt.show()


# In[ ]:





# In[ ]:




