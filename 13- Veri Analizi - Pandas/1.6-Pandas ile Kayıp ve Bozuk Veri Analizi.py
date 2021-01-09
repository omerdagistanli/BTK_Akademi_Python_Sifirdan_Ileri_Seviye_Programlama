import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index=["a","c","e","f","h"], columns=["Kolon1","Kolon2","Kolon3"])

df = df.reindex(["a","b","c","d","e","f","g","h"])

yeniKolon = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["Kolon4"] = yeniKolon

result = df
# result = df.drop("Kolon1", axis= 1)
# result = df.drop(["Kolon1","Kolon2"], axis=1)
# result = df.drop(["a","b"], axis=0)
#
# result = df.isnull()            # NaN olan veriler True olur
# result = df.notnull()           # NaN olan veriler False olur
#
# result = df.isnull().sum()
result = df[df["Kolon1"].isnull()]["Kolon1"]        # NaN olan satırları getirir. Diğer kolonlarda bağlı olduğu için onlarda gözükür.
                                                    # bu yüzden Kolon1 diye hangi kolonun gelmesini istediğimi belirttim.

result = df.dropna()                             # default axis = 0 => herhangi bir satırda NaN varsa o satır silinir.
result = df.dropna(axis = 1)                     # sütunda NaN varsa o sütun silinir

result = df.dropna(how="all")                    # tüm satırlar NaN sa silinir
result = df.dropna(subset=["Kolon1","Kolon3"])  # seçili kolonlarda NaN varsa o satırlar silinir
print(result)