import numpy as np

#dizi= np.array([1,2,3,4,5])
#print(dizi)

#dizi=np.arange(0,10,2)
#print(dizi)
#range(0,10,2)

dizi=np.linspace(0,1,5)
print(dizi)

boyut=dizi.ndim
veri_turu=dizi.dtype
print("Dizinin boyutu:",boyut)
print("veri tipi:",veri_turu)