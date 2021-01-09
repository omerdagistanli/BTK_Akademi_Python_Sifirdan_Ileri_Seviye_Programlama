import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15, 5)

df = pd.DataFrame(data, columns=["Kolon1","Kolon2","Kolon3","Kolon4","Kolon5"])

result = df
result = df.head()                  # ilk 5 kaydı getirir
result = df.tail()                  # son 5 kayıt getirir
result = df["Kolon2"].head()
result = df["Kolon3"].tail()
result = df[df["Kolon1"] > 60] [["Kolon1","Kolon2"]]
result = df[(df["Kolon3"] < 30) & (df["Kolon2"] < 40)]
print(result)