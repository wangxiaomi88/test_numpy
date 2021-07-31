import numpy as np

a = np.arange(1, 101)
print(a[a % 3 == 0])

a[a % 3 == 0] = 9
print(a)

names=np.array(["Mi","Apple","Huawei","Oppo","Vivo"])
rank=[0,3,4,2,1]
print(names[rank])


print("二维索引掩码")
a=np.arange(1,19)
a.resize(3,6)
print(a)
m1=[0,1,2,1,0]
m2=[0,1,2,3,4]
print(a[m1,m2])

