import numpy as np

#1 ile 10 arasında rastgele 5 tam sayı üretme

#rastgele_sayi_üret=np.random.randint(1,10,size=5)
rastgele_sayi_üret=np.random.random(5)
print("Rastgele oluşturulan sayıkar:",rastgele_sayi_üret)

normal_rakam=np.random.normal(0,1,5)

print(normal_rakam)

rastgele_dizi=np.random.rand(3,3)
print(rastgele_dizi)


rastgele_dizi2=np.random.rand(3,3)*10
rastgele_dizi2=rastgele_dizi2.astype(int)
print(rastgele_dizi2)