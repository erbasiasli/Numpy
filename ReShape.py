import numpy as np

#dizi=np.array([1,2,3,4,5,6])
#yeni_dizi=dizi.reshape(2,3)
#print(yeni_dizi)

#matris=np.array([[1,2],[3,4],[5,6]])
#tek_boyut=matris.reshape(-1)#tek boyuta getirir.
#print(tek_boyut)


dizi=np.array([1,2,3,4,5,6,7,8,9,10,11,12])

yeni_dizi=dizi.reshape(3,-1)#-1 satır sayısını biz belirledik sütun sayısını o belirlemesi için

otomatik_dizi=-1
yeni_dizi2=dizi.reshape(3,otomatik_dizi)
print(yeni_dizi2)