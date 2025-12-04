from json import load
import math

toplam_enerji = 100
enerji_katsayisi = 1.0 
x0, y0, z0 = 0, 0, 0 

with open("liste.json", "r") as f:
    dosya = load(f)
    liste = dosya["hedefler"]
    f.close()     

with open("basari_kriterleri.json", "r") as f:
     dosya = load(f)
     kriterler = dosya["kriterler"]
     f.close()

def mesafe_hesaplama(x0, y0 , z0):
    for i in liste:
        x = i["konum_x"]
        y = i["konum_y"]
        z = i["konum_z"]
        mesafe = math.sqrt((x - x0)**2 + (y - y0)**2 + (z - z0)**2) 
        i["mesafe"] = float(format(mesafe, ".2f"))

def g_alan(kriterler, x, y):
    noise = 0
    for i in kriterler:
        if i["id"] == "sensor_hatasi":
            gurultu_alanlari = i["gurultu_alanlari"]
    for i in gurultu_alanlari:
        if i["x_min"] < x < i["x_max"] and i["y_min"] < y < i["y_max"]:
            noise = i["deger"]
    return noise


def ruzgar_etkisi(kriterler):
    ruzgar_degeri = 0
    ruzgar_onem = 0.8
    ruzgar_normali = 0
    for i in kriterler:
        if i["id"] == "ruzgar":
            ruzgar_normali = ((i["hiz"]-1)/(10-1))
    ruzgar_degeri = 1-(ruzgar_onem*ruzgar_normali)
    return ruzgar_degeri

def gurultu_etkisi(kriterler, x, y):
    gurultu_degeri = 0
    sensor = 0.3
    noise = g_alan(kriterler, x, y)
    gurultu_degeri = (1-noise)*sensor
    return gurultu_degeri

def basari_olasiligi(liste):
    for i in liste:
        mesafe_degeri = 0
        hiz = 0.05
        mesafe_hesaplama(x0, y0, z0)
        mesafe = i["mesafe"]
        mesafe_degeri = 1 / (1 + (mesafe*hiz))
        gx = i["konum_x"]
        gy = i["konum_y"]
        gurultu_degeri = gurultu_etkisi(kriterler, gx, gy)
        ruzgar_degeri = ruzgar_etkisi(kriterler)
        basari = mesafe_degeri*gurultu_degeri*ruzgar_degeri
        i["basari_olasiligi"] = basari


def skor(liste, toplam_enerji, enerji_katsayisi):
    global x0, y0, z0

    for i in liste:
        i["skor"] = (i["basari_olasiligi"]* i["deger"]) / i["mesafe"]

    liste_skor = sorted(liste, key=lambda x: x["skor"], reverse=True)

    secilen = []
    kalan_enerji = toplam_enerji

    for i in liste_skor:
        gereken_enerji = i["mesafe"] * enerji_katsayisi
        if kalan_enerji >= gereken_enerji:
                secilen.append(i["id"])
                x0 = i["konum_x"]
                y0 = i["konum_y"]
                z0 = i["konum_z"]
                mesafe_hesaplama(x0, y0, z0)
                kalan_enerji -= gereken_enerji
    return secilen, kalan_enerji

basari_olasiligi(liste)
secilen, kalan_enerji = skor(liste, toplam_enerji, enerji_katsayisi)
print("Secilen hedefler sirasiyla: ", secilen)
print("Kalan enerji miktari: ", format(kalan_enerji, ".2f"))
