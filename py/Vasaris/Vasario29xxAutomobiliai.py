import requests
from bs4 import BeautifulSoup
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('automobiliai.csv')
# print(df)

brangiausias_marke_pagal_kaina = df.groupby('Markė')['Kaina'].max().sort_values(ascending=False).head(1)
# print(brangiausias_marke_pagal_kaina)

vidutine_kaina_pagal_marke = df.groupby('Markė')['Kaina'].mean().sort_values(ascending=False).round(2)
# print(vidutine_kaina_pagal_marke)

kuriais_metais_dazniausiai_pagaminta = df['Metai'].mode()[0]
# print(kuriais_metais_dazniausiai_pagaminta)

kainos_deapazonas_pagal_marke = df.groupby('Markė')['Kaina'].agg(['min', 'max'])
# print(kainos_deapazonas_pagal_marke)

automobilias_pagal_metus = df['Metai'].value_counts().sort_index()
# print(automobilias_pagal_metus)

brangiausiu_modeliu_5 = df.sort_values(by=['Kaina'], ascending=False).head(5)[['Markė', 'Modelis', 'Kaina']]
brangiausiu_modeliu_5 = df.sort_values(by=['Kaina'], ascending=False).head(5)[['Markė', 'Modelis', 'Kaina']].reset_index(drop=True)
# reset_index(drop=True) - ismeta indeksus atejusius is lenteles, reset_index() - tik sukuria nauja indeksavima
# print(brangiausiu_modeliu_5)


automobiliu_skaicius_pagal_markes = df['Markė'].value_counts()
# print(automobiliu_skaicius_pagal_markes)

vidutine_kaina_pagal_metus = df.groupby('Metai')['Kaina'].mean().sort_values(ascending=False).round(2)
# print(vidutine_kaina_pagal_metus)

metu_kainos_koreliacija = df[['Metai', 'Kaina']].corr()
print(metu_kainos_koreliacija) #teigiama koreliacija iki 1, neigiama iki -1