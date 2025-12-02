from json import load

from Skor import skor

toplam_enerji = 100
enerji_katsayisi = 1.0

with open("liste.json", "r") as f:
    dosya = load(f)
    liste = dosya["hedefler"]
    f.close()
    # henüz dosya kapatılmadı
    # mesafe değişkeni hesaplanacak         

secilen, kalan_enerji = skor(liste, toplam_enerji, enerji_katsayisi)

print("Secilen hedefler sirasiyla: ", secilen)
print("Kalan enerji miktari: ", kalan_enerji)
