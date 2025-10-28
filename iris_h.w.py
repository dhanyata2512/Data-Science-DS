import pandas as pd

iris_df=pd.read_csv(r"C:\Users\Bhulku\Desktop\jetlearn\Data Science DS\iris.csv")

print(iris_df.head(15))

print(iris_df["petal_length"].mean())
print(iris_df["petal_width"].mean())
print(iris_df["sepal_length"].mean())
print(iris_df["sepal_width"].mean())

print(iris_df["petal_length"].min())
print(iris_df["petal_width"].min())
print(iris_df["sepal_length"].min())
print(iris_df["sepal_width"].min())

print(iris_df["petal_length"].max())
print(iris_df["petal_width"].max())
print(iris_df["sepal_length"].max())
print(iris_df["sepal_width"].max())

print(iris_df["species"].value_counts())


