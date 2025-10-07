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

#descriptive statistics 
print(df.describe())

# read csv file
titanic_df=pd.read_csv(r"C:\Users\Bhulku\Desktop\jetlearn\Data Science DS\titanic.csv")
titanic_df.info()
print(titanic_df)

#fetch records from top
print(titanic_df.head(15))

#fetch records from bottom
print(titanic_df.tail())

#No.rows and columns
print(titanic_df.shape)

#retrive single column
print(titanic_df["Name"])

print(titanic_df["Age"].mean())
print(titanic_df["Fare"].sum())

#retrive multiple column
print(titanic_df[["Name","Age"]])

#filtering
print(titanic_df[titanic_df["Age"]<18])

print(titanic_df[(titanic_df["Age"]<18)&(titanic_df["Pclass"]==1)])# & --> and  ----- use | ---> or

#slicing with index
print(titanic_df.iloc[10:20:2,2:5])
print(titanic_df.iloc[[13,14,5,7,34,67,92],[2,3,5]])
