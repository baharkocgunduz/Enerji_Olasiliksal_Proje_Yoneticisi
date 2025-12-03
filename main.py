'''
-----
başarı durumunu kontrol edden ayrı bir dosya açılacak
başarı durumu için gerekli olan parametreler belirlenecek
bu parametrelerin okunacağı bir dosya olabilir
sonuçta başarı durumu hesaplama fonk tanımlanacak
hesap yapılacak ve gerekli değer döndürülecek
main.py de import edilecek ve fonksisyon çalıştırılıp sonucu başarı olasılığına yüklenecek


'''
from json import load
import math

toplam_enerji = 100
enerji_katsayisi = 1.0
x0, y0, z0 = 0, 0, 0 # başlangıç konumu

# json dosyası okundu , liste değişkeni liste türünde hedef bilgilerini taşıyor
with open("liste.json", "r") as f:
    dosya = load(f)
    liste = dosya["hedefler"]
    f.close()     

# liste içinde tutulan x,y,z konumları kullanılarak en kısa mesafeyi hesaplayan fonksiyon
# hesaplanan mesafeler liste içinde her hedef dict için ekleniyor
def mesafe_hesaplama():
    for i in liste:
        x = i["konum_x"]
        y = i["konum_y"]
        z = i["konum_z"]
        mesafe = math.sqrt((x - x0)**2 + (y - y0)**2 + (z - z0)**2) # en kısa mesafe hesaplanıyor
        i["mesafe"] = float(format(mesafe, ".2f"))


# hesaplanan skorlar liste içinde her hedef dict için ekleniyor
# liste skor değerlerine göre azalan sırayla sıralanıyor
# kalan enerji güncelleniyor
# seçilen hedefler secilen listesine ekleniyor
# secilen listesi ve son enerji return ediliyor 
def skor(liste, toplam_enerji, enerji_katsayisi):
    for i in liste:
        i["skor"] = (i["basari_olasiligi"]* i["deger"]) / i["mesafe"]

    liste_skor = sorted(liste, key=lambda x: x["skor"], reverse=True)

    secilen = []
    kalan_enerji = toplam_enerji

    for i in liste_skor:
        gereken_enerji = i["mesafe"] * enerji_katsayisi
        if kalan_enerji >= gereken_enerji:
                secilen.append(i["id"])
                kalan_enerji -= gereken_enerji
    return secilen, kalan_enerji


mesafe_hesaplama()
secilen, kalan_enerji = skor(liste, toplam_enerji, enerji_katsayisi)

print("Secilen hedefler sirasiyla: ", secilen)
print("Kalan enerji miktari: ", kalan_enerji)
