# split single cells of multiple values into individual columns

import pandas as pd

df = pd.read_csv("contra1_.csv")

df[['Female sterilisation', 'Male sterilisation', 'Pill', 'Injectable', 'Implant', 'IUD', 'Male condom', 'Rhythm', 'Withdrawal']] = df['Contraceptive'].str.split(" ", expand=True)

df = df.drop(['Contraceptive'], axis=1)

df.to_csv(r"C:\Users\thous\OneDrive\Desktop\projects\contra\world_contra.csv", encoding='utf-8', index=False)
