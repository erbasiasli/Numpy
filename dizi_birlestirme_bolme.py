import numpy as np

#dizi1=np.array([1,2,3])
#dizi2=np.array([4,5,6])
#tek boyutlu dizi birleştirme
#birlesik_dizi=np.concatenate((dizi1,dizi2))

#print("diziler birleştirildi:",birlesik_dizi)

#iki boyutlu dizi birleştirme
#dizi3=np.array([[1,2,3],[4,5,6]])
#dizi4=np.array([[7,8,9],[10,11,12]])

#birlesik_dizi=np.hstack((dizi3,dizi4))#dikey birleştirme
#birlesik_dizi2=np.vstack((dizi3,dizi4))#yatay birleştirme

#print(birlesik_dizi)
#print(birlesik_dizi2)

#dizi bölme
#dizi=np.array([1,2,3,4,5,6])
#bd=np.split(dizi,3)
#print(bd)

dizi5=np.array([[1,2,3,4],[5,6,7,8]])
bd=np.hsplit(dizi5,2)
bd1=np.vsplit(dizi5,2)

print(bd)
print(bd1)
