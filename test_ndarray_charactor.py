import numpy as np

a=np.arange(1,19)
a.shape=(2,9)
print(a)
a.resize(2,3,3)
print(a)

# 视图变维
print("视图变维")
a2=a.reshape(3,6)
a3=a.ravel()
print("新向量：",a2,a3)
a[0][0][0]=999
print("原向量改值后：",a2,a3)


# f复制变维
print("复制变维")
a4 = a.flatten()
print("新向量：",a4)
a[0][0][0]=222
print("原向量改值后：",a4)

print(a4[8::-1])


print(a2[1,:])
print(a2[:,2])

print(a2)
print(a2[1:2,:])
print(a2[:,-1:-3:-1])
print("切片")
print(a2[2:0:-1,-1:-3:-1])

b=np.arange(1,19)
mask=[2,5,6,14]
print(b[mask])
print(b[[2,4,6,9,12]])