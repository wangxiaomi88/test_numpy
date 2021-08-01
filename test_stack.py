import numpy as np

a=np.arange(1,7).reshape(2,3)
b=np.arange(7,13).reshape(2,3)
print(a)
print(b)

print(np.vstack((a,b)))
print(np.hstack((a,b)))
print(np.dstack((a,b)))

print("拆分矩阵")
c=np.vstack((a,b))
a,b=np.vsplit(c,2)
print(a,b)

c=np.hstack((a,b))
a,b,d=np.hsplit(c,3)
print(a,b,d)

print("三维拆分")
c=np.dstack((a,b))
a,b=np.dsplit(c,2)
print(c)
print(a,b)

a=a.reshape(2,2)
b=b.reshape(2,2)
print(np.concatenate((a,b),axis=0))
print(np.concatenate((a,b),axis=1))

p,q=np.split(a,2,axis=0)
print(p,q)


a=np.arange(1,9)
b=np.arange(9,17)
c=np.row_stack((a,b))
print(c)
d=np.column_stack((a,b))
print(d)

print(d.T) #d的转置







