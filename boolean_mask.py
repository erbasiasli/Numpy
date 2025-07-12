import numpy as np

dizi=np.array([10,20,30,40,50,68,98,74,25,11,33])
#boolean_mask=dizi>50
#print(boolean_mask)

#print("boolean maskeyi kullanarak dizideki elemanalrı seçme")

#secilmis=dizi[boolean_mask]
#print("50den büyük olan elemanlar:",secilmis)

boolean_mask= (dizi>30) &(dizi<70)
print("30 ile 70 arasındaki elemanlar:",dizi[boolean_mask])

