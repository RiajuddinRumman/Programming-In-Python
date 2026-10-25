import pandas as pd

data = {
    "Name" : ["Alex", "Baena", "Cristiano", "Donaruma", "Elanga", "Fred"],
    "Age" : [22, 27, 41, 30, 25, 31],
    "Nationality" : ["Spain", "Spain", "Portugal", "Italy", "England", "Brazil"],
    "Position" : ["LW", "LM", "ST", "GK", "RW", "RM"]
}

df = pd.DataFrame(data)

print(df.head(), df.tail())
print(df.describe())
print(df.columns)
print(df.dtypes)