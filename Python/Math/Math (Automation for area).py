#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

# fungsi tampilkan menu
def tampilkan_menu():
    print("Menu:")
    print("1 - Luas Persegipanjang")
    print("2 - Luas Segitiga")
    print("3 - Luas Lingkaran")
    print("4 - Luas Trapesium")
    print("5 - Keluar")

    
def pilih_menu():
    while (True):
       tampilkan_menu()
       pilihan = input("Ketik pilihan Anda")
    
       if (pilihan == "1" or pilihan == "2" or pilihan == "3" or pilihan == "4" or pilihan == "5"):
          return int(pilihan)
       else:       
          print("Pilihan Anda tidak ada dalam menu")  

        
def luas_persegipanjang(panjang,lebar):
    luas = panjang*lebar
    return luas
    
def luas_segitiga(alas,tinggi):
    luas = alas*tinggi / 2
    return luas

    
def luas_lingkaran(jari2):
    luas = math.pi*jari2**2
    return luas
    
def luas_trapesium(a,b,t):
    luas = (a + b)/2 * t
    return luas


pilih = pilih_menu()
if pilih == 1:
    print("Anda memilih menu Luas Persegi Panjang")
    panjang = float(input("Masukkan Panjang:"))
    lebar = float(input("Masukkan Lebar:"))
    luas = luas_persegipanjang(panjang,lebar)
    print("Luas Persegi Panjang adalah:", luas, "m2")
    

elif pilih == 2:
    print("Anda memilih menu Luas Segitiga")
    alas = float(input("Masukkan Alas:"))
    tinggi = float(input("Masukkan Tinggi:"))
    luas = luas_segitiga(alas,tinggi)
    print("Luas Segitiga adalah:", luas, "m2")

elif pilih == 3:
    print("Anda memilih menu Luas Lingkaran")
    jari2 = float(input("Masukkan Jari-jari:"))
    luas = luas_lingkaran(jari2)
    print("Luas Lingkaran adalah:", luas, "m2")
    

elif pilih == 4:
    print("Anda memilih menu Luas Trapesium")
    a = float(input("Masukkan nilai a:"))
    b = float(input("Masukkan nilai b:"))
    t = float(input("Masukkan Tinggi:"))
    luas = luas_trapesium(a,b,t)
    print("Luas Trapesium adalah:", luas, "m2")

else:
    print("Anda memilih Keluar")


# In[ ]:




