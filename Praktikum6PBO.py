# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:00:44 2024

@author: ocanh
"""

import math

class BangunRuang:
    def __init__(self):
        pass
    
    def hitung_luas(self):
        pass
    
    def hitung_volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        super().__init__()
        self.sisi = sisi
    
    def hitung_luas(self):
        return 6 * self.sisi ** 2
    
    def hitung_volume(self):
        return self.sisi ** 3

class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        super().__init__()
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    
    def hitung_luas(self):
        return 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)
    
    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

class Bola(BangunRuang):
    def __init__(self, jari_jari):
        super().__init__()
        self.jari_jari = jari_jari
    
    def hitung_luas(self):
        return 4 * math.pi * self.jari_jari ** 2
    
    def hitung_volume(self):
        return (4/3) * math.pi * self.jari_jari ** 3

class Silinder(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        super().__init__()
        self.jari_jari = jari_jari
        self.tinggi = tinggi
    
    def hitung_luas(self):
        return 2 * math.pi * self.jari_jari * (self.jari_jari + self.tinggi)
    
    def hitung_volume(self):
        return math.pi * self.jari_jari ** 2 * self.tinggi

class PrismaSegitiga(BangunRuang):
    def __init__(self, alas, tinggi_alas, tinggi_prisma):
        super().__init__()
        self.alas = alas
        self.tinggi_alas = tinggi_alas
        self.tinggi_prisma = tinggi_prisma
    
    def hitung_luas(self):
        return self.alas * self.tinggi_alas + 3 * self.alas * self.tinggi_prisma
    
    def hitung_volume(self):
        return (1/2) * self.alas * self.tinggi_alas * self.tinggi_prisma

def main():
    # Meminta pengguna untuk memasukkan Nama dan NIM sekali saja
    nama = input("Nama: ")
    nim = input("NIM : ")

    print("--- Soal ---")  # Tambahkan prompt untuk "Soal"
    sisi_kubus = float(input("Masukkan panjang sisi kubus: "))
    kubus = Kubus(sisi_kubus)
    luas_kubus = kubus.hitung_luas()
    volume_kubus = kubus.hitung_volume()

    panjang_balok = float(input("Masukkan panjang balok: "))
    lebar_balok = float(input("Masukkan lebar balok: "))
    tinggi_balok = float(input("Masukkan tinggi balok: "))
    balok = Balok(panjang_balok, lebar_balok, tinggi_balok)
    luas_balok = balok.hitung_luas()
    volume_balok = balok.hitung_volume()

    jari_jari_bola = float(input("Masukkan jari-jari bola: "))
    bola = Bola(jari_jari_bola)
    luas_bola = bola.hitung_luas()
    volume_bola = bola.hitung_volume()

    jari_jari_silinder = float(input("Masukkan jari-jari silinder: "))
    tinggi_silinder = float(input("Masukkan tinggi silinder: "))
    silinder = Silinder(jari_jari_silinder, tinggi_silinder)
    luas_silinder = silinder.hitung_luas()
    volume_silinder = silinder.hitung_volume()

    alas_prisma = float(input("Masukkan alas prisma segitiga: "))
    tinggi_alas_prisma = float(input("Masukkan tinggi alas prisma segitiga: "))
    tinggi_prisma = float(input("Masukkan tinggi prisma segitiga: "))
    prisma_segitiga = PrismaSegitiga(alas_prisma, tinggi_alas_prisma, tinggi_prisma)
    luas_prisma = prisma_segitiga.hitung_luas()
    volume_prisma = prisma_segitiga.hitung_volume()

    print("--- Hasil jawaban ---")  # Tambahkan prompt untuk "Hasil jawaban"
    print("Luas kubus :", luas_kubus)
    print("Volume Kubus :", volume_kubus)
    print("Luas balok :", luas_balok)
    print("Volume balok :", volume_balok)
    print("Luas bola :", luas_bola)
    print("Volume Bola :", volume_bola)
    print("Luas silinder :", luas_silinder)
    print("Volume silinder :", volume_silinder)
    print("Luas prisma segitiga :", luas_prisma)
    print("Volume Prisma segitiga :", volume_prisma)

if __name__ == "__main__":
    main()
