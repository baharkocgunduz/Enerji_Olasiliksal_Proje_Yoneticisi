
liste = [
    {"id" : "hedef1", "mesafe " : 10, "deger" : 2, "basari_olasiligi" : 0.5,"skor" :""},
    {"id" : "hedef2", "mesafe " : 20, "deger" : 3, "basari_olasiligi" : 1.0,"skor" :""},
    {"id" : "hedef2", "mesafe " : 30, "deger" : 1, "basari_olasiligi" : 1.5, "skor" :""}
]

toplam_enerji = 100
enerji_katsayisi = 1.0

def skor(liste, toplam_enerji, enerji_katsayisi):
    for i in liste:
        i["skor"] = (i["basari_olasiligi"]* i["deger"]) / i["mesafe "]
    
    liste_skor = sorted(liste, key=lambda x: x["skor"], reverse=True)

    secilen = []
    kalan_enerji = toplam_enerji

    for i in liste_skor:
        gereken_enerji = i["mesafe "] * enerji_katsayisi
        if kalan_enerji >= gereken_enerji:
                secilen.append(i["id"])
                kalan_enerji -= gereken_enerji
    return secilen, kalan_enerji
            

secilen, kalan_enerji = skor(liste,toplam_enerji,enerji_katsayisi)

print ("Secilen hedefler sirasiyla: ", secilen)
print("Kalan enerji miktari: ", kalan_enerji)