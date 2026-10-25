import numpy as np
import pandas as pd

child1 = {
    "name" : "Emil",
    "year" : 2004,
}

child2 = {
    "name" : "Tobias",
    "year" : 2007
}

child3 = {
    "name" : "Linus",
    "year" : 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(myfamily.get("child1"))




data = {
    "Student" : ["Martinez", "Alvarez", "John", "Chris", "Shakib", "Sarah"],
    "Department" : ["CSE", "CSE", "EEE", "CSE", "EEE", "CSE"],
    "Age" : [21, 22, 20, 21, 23, 22],
    "Attendance" : [85, 90, 96, 98, 97, 92],
    "Marks" : [88, 85, 90, 92, 90, 91]
}

df = pd.DataFrame(data)

print(1,df)
print(2, df.head(2), df.tail(2)) ##function for printing first and last two values
print(df.sample(2)) ##print random rows
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.describe()) ##statistical summary
print(df.info())
print(df.sort_values("Marks"))



print(df["Marks"].mean())
print(df["Marks"].median())
print(df["Marks"].max())
print(df["Marks"].min())
print(df["Marks"].sum())
print(df["Marks"].std())


##print(df.isNull().sum())
##print(df.duplicated().sum())

df = df.drop_duplicates()
df = df.rename(columns = {
    "Student" : "Name",
    "Department" : "Dept"
})

#df = pd.read_csv("SL Flood Risk.csv")
