import numpy as np

def loadcsv(filepath):
    header=[]
    data=[]
    with open(filepath,"r") as f:
        for index, line in enumerate(f.readlines()):
            if index == 0:
                header=line[:-1].split(",")
            else:
                data.append(tuple( line[:-1].split(",") ))

    result=np.array(data,dtype={"names":header,"formats":["f8","f8","f8","f8","f8","f8"]}) #构建一个一维数组，每个元素是一个元组且起好了名字
    return result




if __name__ == '__main__':
    data= loadcsv("data.csv") #index,pack_type,extra_time,extra_flow,use_month,loss
    print(data[0]["extra_time"],data.shape)

    extra_time_col=data["extra_time"]
    print("extra_time min value: ", min(extra_time_col),"extra_time max value: ", max(extra_time_col), "mean: ",sum(extra_time_col)/len(extra_time_col))
    extra_flow_col=data["extra_flow"]
    print("extra_flow min value: ", min(extra_flow_col),"extra_flow max value: ", max(extra_flow_col), "mean: ",sum(extra_flow_col)/len(extra_flow_col))
    use_month_col=data["use_month"]
    print("use_month min value: ", min(use_month_col),"use_month max value: ", max(use_month_col), "mean: ",sum(use_month_col)/len(use_month_col))


    print("有剩余通话时间的人数占比：",data[data["extra_time"]>0].size/data.size)
    print("有剩余流量的人数占比：",data[data["extra_flow"]>0].size/data.size)


kinds=set(data["pack_type"])
for k in kinds:
    print(k,"套餐占比：", data[data["pack_type"]==k].size/data.size  )





