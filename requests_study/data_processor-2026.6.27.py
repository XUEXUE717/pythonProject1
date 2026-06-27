import csv
import pandas as pd

read = pd.read_csv('nba.csv',sep=",",header=0,encoding='gbk',names=['Name','Team','Number','Position','Age','Height','Weight','College','Salary'
])
print(type(read))
#print(read["Name"])
data_age = read[read['Age'] > 35]
print(data_age.to_string())
data_age.to_csv("data_gt_35.csv",index=False)
