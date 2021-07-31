import numpy as np

# a=np.array([[123],[3,4,5],[6,7,8]])
a=np.array([1,2,3,4,5,6])
print(a,type(a))

for i in a:
    print(i)

print(a[0],a[1:3])

print(a*2)
print(a+a)
print(a>2)
print(a*a)

b=np.array([1,2,3,4,5])

try:
    print(a*b)
except Exception as e:
    print(e)
