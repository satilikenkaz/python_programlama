import pandas as pd

veri = pd.read_csv("iris.data")

print(veri.head())

print(veri.columns)

print(veri[3:5])

print(veri.sort_values(by="sepal length"))
