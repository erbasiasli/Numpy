import numpy as np

dizi1=np.array([1,2,3,5])
dizi2=np.array([3,4,12,5])

toplam=dizi1+dizi2
çıkarma=dizi1-dizi2
çarpma=dizi1*dizi2
bölme=dizi1/dizi2

#print("Toplam",toplam)
#print(çıkarma)
#print(çarpma)
#print(bölme)

toplam=np.sum(dizi1)
print(toplam)

carpim=np.prod(dizi1)
print(carpim)

kare_al=np.sqrt(dizi1)
print(kare_al)

ortalama=np.mean(dizi1)
print(ortalama)

medyan_al=np.median(dizi1)
print(medyan_al)

standart_sapma=np.std(dizi1)
print(standart_sapma)