import numpy as np

a=np.array([[1,2,3],[4,5,6]])
b=np.arange(0,10,2.2)

c=np.zeros([3,5])
d=np.ones(10,dtype="float32")
d2=np.ones(10,dtype="int32")

e=np.zeros_like(a)
f=np.ones_like(b)

print(a)
print(b)
print(c)
print(d)
print(d2)
print(e)
print(f)

print(np.ones(5)/5)

#ndarray属性访问及操作
print(b.shape,d.dtype,c.size,len(c))

c.shape=(5,3)
print(c)
print("行访问：",c[0])
print("列访问：",c[: ,0])

# d4=d
# d4.dtype="int32"
# print(d4)

d3=d.astype("int64")
print(d3)

