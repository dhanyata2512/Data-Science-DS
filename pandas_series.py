import pandas as pd

#converting list/array to series
list=[2,3,7,6,3,6,12,13,14]
s=pd.Series(list)#,index=["a","b","c","d","e","f","g"])
print(s)
#print(s["e"])
print(type(s))

#statistical operation
print(s.mean())
print(s.sum())
print(s.count())
print(s.min())
print(s.max())
print(s.median())
print(s.mode())

#sorting
print(s.sort_values())
print(s.sort_values(ascending=False))

#count unique values
print(s.value_counts())