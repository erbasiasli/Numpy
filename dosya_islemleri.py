import numpy as np

data=np.loadtxt('data.txt',delimiter=None)
#print(data)

row_sums=np.sum(data,axis=1)
#print("her sqatırın toplamı",row_sums)

#np.savetxt('output.txt',row_sums,fmt='%d')

output_data=np.column_stack((data,row_sums))

np.savetxt('output_with_sums.txt',output_data,fmt='%d',delimiter=' ')
print("kayıt işlemi tamamlandı.")



