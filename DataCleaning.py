
import numpy as np
import pandas as pd
df = pd.read_csv('/SVM_ENG/智慧旅游-旅馆信息数据集1.csv')

a= np.array(df)
c=[]
[rows,cols]=a.shape
for i in range(rows):
    for j in range(cols):
        x=str(a[i][j])
        y=x.encode("UTF-8")
        if(len(x)!=len(y)):
            c.append(i)
            break
a=np.delete(a,c,axis=0)
pd_data=pd.DataFrame(a,columns=range(cols))
pd_data.to_csv('/SVM_ENG/智慧旅游-旅馆信息数据集(修改).csv')



