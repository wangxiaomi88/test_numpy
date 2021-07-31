import numpy as np

a=np.arange(1,19).reshape(3,6)
print(a)

print("后两列数据")
print(a[-2:,:])

print("间隔分割")
print(a[:, ::2])

print("逆序切片")
print(a[2:0:-1, -1:-3:-1])

print("练习题")
print(a[:4:2, :])
print(a[:, :3])

print("二维索引掩码")
# mask1=[0,0,1,1]
# print(a[mask1])

m1=[0,0,0]
m2=[1,1,1]
print(a[m1,m2])



print("三维数据")
a=a.reshape(2,3,3)
print(a)

print("练习题")
print(a[:, :2, :2])

