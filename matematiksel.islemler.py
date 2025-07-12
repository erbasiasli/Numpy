import numpy as np

dizi1=np.array([1,2,3,4,5])
dizi2=np.array([3,4,45,23,34])

#toplam=np.add(dizi1,dizi2)
#fark=np.subtract(dizi1,dizi2)
#carp=np.multiply(dizi1,dizi2)
#bol=np.divide(dizi1,dizi2)
#ustunu_al=np.power(dizi1,2)
#karekok=np.sqrt(dizi1)

#mean dizinin ortalamasını alır
#varyans ortalamaya yakınlığı ve uzaklığı hesaplayan birim ort uzaklaştıkça varyans yüksek olur

#varyans=np.var(dizi1)
#print(varyans)

#standart sapma bir yarışta aynı anda bitirme süreleri aynıysa standart sapma düşük ama bazısı çok hızlı bazısı çok yavaş bitirirse standart sapma yüksektir.

sapma=np.std(dizi2)
print(sapma) 

#print(toplam)
#print(fark)
#print(carp)
#print(bol)
#print(ustunu_al)
#print(karekok)