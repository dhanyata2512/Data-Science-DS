import pandas as pd

#dictionary to Data Frame
dictionary={"name":["Dhanyata","Aditi","Amy"],"age":[13,34,14],"year":[9,13,10]}
df=pd.DataFrame(dictionary,index=["S1","S2","S3"])
print(df)
print(type(df))

#List to a Data Frame
list=[["Dhanyata",13,9],["Aditi",34,13],["Amy",14,10]]
df2=pd.DataFrame(list,columns=["Name","Age","Year"])
print(df2)

#fetch complete info
df.info()