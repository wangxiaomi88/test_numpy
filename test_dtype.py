import numpy as np

a=np.array([1,2,3,4],dtype="float32")
print(a,a.dtype)

b=a.astype("int64")
c=b.astype("str")
print(b,b.dtype)
print(c,c.dtype)


data=[
    ("小红",[45,60,84],15),
    ("小",[57,76,89],15),
    ("小拉面兰",[32,68,77],15)
]

# c=np.array(data,dtype="2str,3int32,int32,")
c=np.array(data,dtype="2U,3i4,i4,")
print("行访问",c[0])
print("矩阵规模",c.shape)

d=np.array(data,dtype={"names":["name","scores","age"],"formats":["2str","3int32","int32"]})
print(d[2]["scores"])

e = np.array(data, dtype=[("name","str",2),("scores","int32",3),("age","int32",1)] )
print(e[0]["scores"])
print(e["age"])


dates=np.array(["2011","2011-02","2011-03-02","2011-03-04 10:54:36"])
# ndates=dates.astype("datetime64[D]") #时间精确到天
ndates=dates.astype("M8[D]") #时间精确到天
print(ndates)
print(ndates[-1]-ndates[0])


