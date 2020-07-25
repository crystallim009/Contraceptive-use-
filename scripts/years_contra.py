
import pandas as pd
import numpy as np

df = pd.read_csv("contra.csv")

df = df.replace('..', np.nan)                          # change to null 

df = df.drop(['Survey start year'], axis=1)

df[df.columns[4:]] = df[df.columns[4:]].astype(float)
df = df.round(1)                                       # change columns to one decimal place

df.to_csv(r"C:\Users\thous\OneDrive\Desktop\projects\contra\years_contra.csv", encoding='utf-8', index=False)
