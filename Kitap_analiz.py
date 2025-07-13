import numpy as np

kitap_fiyatlari=np.array([25,45,20,35,50,40,30])

satis_adetleri=np.array([100,150,200,120,130,80,110])

kategoriler=np.array(["Roman","Bilim","Çocuk","Tarih","Roman","Bilim","Çocuk"])

toplam_gelir=kitap_fiyatlari*satis_adetleri
print("Toplam Gelir:",kategoriler,'\n',toplam_gelir)

#ortalama_fiyat=np.mean(kitap_fiyatlari)
#max_fiyat=np.max(kitap_fiyatlari)
#min_fiyat=np.min(kitap_fiyatlari)

#print("Ortalama fiyat:",ortalama_fiyat)
#print("Max fiyat:",max_fiyat)
#print("Min fiyat:",min_fiyat)

romanlar=kitap_fiyatlari[kategoriler=="Roman"]
print('Roman kategorisi içerisindeki kitapların fiyatları:',romanlar)

roman_satislari=satis_adetleri[kategoriler=="Roman"]
print("Roman satış:",roman_satislari)

Roman_Toplam_Satis=np.sum(romanlar*roman_satislari)
print(Roman_Toplam_Satis)


veri=np.array([kitap_fiyatlari,satis_adetleri])
veri_reshaped=np.reshape(veri,(2,7))

print(veri_reshaped)

