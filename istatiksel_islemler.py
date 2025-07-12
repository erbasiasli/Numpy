import numpy as np

dizi=np.array([1,2,3,4,56])
#min=np.min(dizi)
# #maks=np.max(dizi)
#print("-"*45)
#print("Dizi içerisinde en yüksek değere sahip veri:",maks)
#print("Dizideki en düşük değer:",min)
#print("-"*45)

toplam=np.sum(dizi)
kume_toplam=np.cumsum(dizi)
#kümelatif toplam bir öncekiyle toplayıp bie ileriye atar toplamı

print(toplam)
print(kume_toplam)