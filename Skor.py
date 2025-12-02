import main
import math

toplam_enerji = 100
enerji_katsayisi = 1.0
x0 , y0, z0 = 0, 0, 0

def mesafe_hesaplama():
    for i in main.liste:
        x = i["konum_x"]
        y = i["konum_y"]
        z = i["konum_z"]
        mesafe = math.sqrt((x - x0)**2 + (y - y0)**2 + (z - z0)**2) # en kısa mesafe hesaplanıyor
        i["mesafe"] = mesafe

mesafe_hesaplama()

def skor(liste, toplam_enerji, enerji_katsayisi):
    for i in main.liste:
        i["skor"] = (i["basari_olasiligi"]* i["deger"]) / i["mesafe"]

    liste_skor = sorted(main.liste, key=lambda x: x["skor"], reverse=True)

    secilen = []
    kalan_enerji = toplam_enerji

    for i in liste_skor:
        gereken_enerji = i["mesafe"] * enerji_katsayisi
        if kalan_enerji >= gereken_enerji:
                secilen.append(i["id"])
                kalan_enerji -= gereken_enerji
    return secilen, kalan_enerji