import pandas as pd

pd.set_option('future.no_silent_downcasting', True)

iris_df=pd.read_csv(r"C:\Users\Bhulku\Desktop\jetlearn\Data Science DS\iris.csv")

print(iris_df.head(15))
print(iris_df.shape)
print(iris_df.info())
print(iris_df.tail(8))

print(iris_df["species"].value_counts())

print(iris_df[iris_df["species"]=="setosa"])

print(iris_df[iris_df["petal_length"]>iris_df["petal_length"].mean()])

print(iris_df.agg({"petal_length":["mean","min","max"],"petal_width":["mean","min","max"],"sepal_width":["mean","min","max"],"sepal_length":["mean","min","max"]}))

iris_df["specimen"]=iris_df["species"].replace({"setosa":1,"virginica":2,"versicolor":3})
print(iris_df)

print(iris_df.sort_values("petal_length"))
print(iris_df.groupby("species").mean())

iris_df.rename(columns={"sepal_length":"sepal lenght","sepal_width":"sepal width","petal_width":"petal width"},inplace=True)
print(iris_df)

print(iris_df["species"].str.upper())
