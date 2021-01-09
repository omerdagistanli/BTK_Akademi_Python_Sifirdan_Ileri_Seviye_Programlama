import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index = ["A","B","C"], columns=["Column1","Column2","Column3"])

# Seriler
result = df.loc["A"]                # A satırına ait kolonlar ekrana yazdırılır A-Column1,Column2,Column3
result = type(df.loc["A"])

# Kullanım şekli
# loc["row", "column"], loc["row"], loc[":", "column"]

result = df.loc["A":"C","Column2"]              # A C arası Column2 değerleri yazılır

# iloc[ index (satırlara göre) ]
result = df.iloc[1]              # B satırına ait Kolonların hepsi yazdırılır

df["Column4"] = pd.Series(randn(3), ["A","B","C"])      # oluşturulan seriyi df ye ekledik

df.drop("Column4", axis=1)       # kolon 5 in yukardan aşağı olduğunu belirttik

print(df)