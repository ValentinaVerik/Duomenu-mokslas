import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_columns', 10) #apraso, kiek konsoleje matosi stulpeliu, eiluciu, plocio
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 500)
"""
apie Pandas
"""
# data = {
#     'Vardas': ['Jonas', 'Petras', 'Ona', 'ieva', 'Julia'],
#     'Amzius': [28, 34, 19, 42, 27],
#     'Miestas': ['Vilnius', 'Kaunas', 'Panevezys', 'Klaipeda', 'Klaipeda']
# }
#
# df = pd.DataFrame(data)
#
# # print(df)
# # print(df['Amzius'])
# # print(df[['Vardas', 'Amzius']])

"""
filtravimas
"""
# vyresni_nei_30 = df[df['Amzius']>30] #nurodome df su [], tada viduje i naujus ['Vardas', 'Amzius'] idedame su kuo dirbame, paskui nurodoma kas atliekama
# # print(vyresni_nei_30)
#
# df['Vyresni nei 30'] = df['Amzius'] > 30 #numatome nauja stulpeli
# # print(df)
"""
rusiavimas
"""
# df_sorted = df.sort_values(by='Amzius', ascending=False) # jei parasysime True, tai surikiuos nuo maziausio(de foult),
# # jei norim tik nuo mazeusio, rasyti salygos 'ascending=True'nebutina
# # print(df_sorted)
# df_sorted = df.sort_values(by=['Miestas', 'Amzius']) #reikia skliausteliu dar vienu[], nes yra dvi reiksmes, kadangi by priima tik viena reiksme
# # print(df_sorted)
#
"""
grupavimas
"""
# grouped_df = df.groupby('Miestas')['Amzius'].mean() #mean - vidurkis
# # print(grouped_df)


"""
Apie renginius
"""
# data  = {
#     'Renginio data': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01'],
#     'Miestas': ['Vilnius', 'Alytus', 'Kaunas', 'Alytus'],
#     'Dalyviai': [300, 150, 250, 100]
# }
#
# df = pd.DataFrame(data)
# print(df)
#
"""
reikia papildomu stulpeliu
"""
#
def renginio_dydis(dydis):
    if dydis < 123:
        return "mazas"
    elif 125 <= dydis <= 200:
        return 'vidutinis'
    else:
        return "didelis"

df['Renginio dydis'] = df['Dalyviai'].apply(renginio_dydis) # apply - kad pritaikyti def funkcija
print(df)

"""
apskaiciuoti bendr1 kiekvieno miesto dalyviu skaiciu
"""
#
# bendras_dalyviu_skaicius_mieste = df.groupby('Miestas')['Dalyviai'].sum() #pirma sugrupuojame pagal miesta
# print(bendras_dalyviu_skaicius_mieste)

"""
Kompiuterijos žodynai internete (naujausios versijos):
http://www.ims.mii.lt/EK%C5%BD/enciklo.html – Enciklopedinis kompiuterijos žodynas
http://www.ims.mii.lt/ALK%C5%BD/angl.html – Anglų–lietuvių kompiuterijos žodynasAngliškas sort gali turėti dvi skirtingas reikšmes:
   1. rikiuoti;
   2. rūšiuoti.rūšiuoti
    Komanda, kuria objektai suskirstomi į kelias grupes – surūšiuojami.
    Pavyzdžiui, gauti laiškai skirstomi į kelis aplankus pagal tematiką. Jeigu objektai išdėstomi į eilę, tai tada sakoma, kad jie rikiuojami.
    Atkreipiame dėmesį, kad anglų kalboje neskiriamos rikiavimo ir rūšiavimo sąvokos. Tai reikia turėti omenyje verčiant programas.rikiuoti
    Komanda rikiavimui atlikti.
    Pavyzdžiai: rikiuoti atvirkščiai, rikiuoti didėjančiai, rikiuoti mažėjančiai, rikiuoti pagal datas ir laikus, rikiuoti pagal siuntėjus, rikiuoti pagal temas, rikiuoti stulpelius.--------------- (edited) 
11:20
grupuoti
    Komanda keliems objektams susieti į vieną.
    Pavyzdžiui, kelioms geometrinėms figūroms į vieną brėžinį.
    Priešinga komanda – išgrupuoti.
    Angliškai: group.
"""

"""
Sukurkite dataframe su stulpeliais [Šalis, Gyventojų skaičius mln, BVP, mlrd. USD]

Pridėkite naują stulpelį BVP vienam gyventojui, USD, kuris apskaičiuojamas padalinant BVP iš gyventojų skaičiaus ir padauginant iš milijono.
Raskite ir atspausdinkite šalį su didžiausiu BVP vienam gyventojui.
Pridėkite naują stulpelį Ekonomikos kategorija, kuris kategorizuoja šalis pagal jų BVP:
        * Jei BVP mažesnis nei 100 mlrd. USD, Ekonomikos kategorija yra 'Maža ekonomika'.
        * Jei BVP yra tarp 100 mlrd. USD ir 1000 mlrd. USD, Ekonomikos kategorija yra 'Vidutinė ekonomika'.
        * Jei BVP didesnis nei 1000 mlrd. USD, Ekonomikos kategorija yra 'Didelė ekonomika'.
Grupuokite duomenis pagal Ekonomikos kategorija ir apskaičiuokite vidutinį BVP vienam gyventojui kiekvienoje kategorijoje.
"""
#
# data = {
#     'Salis': ['Lietuva', 'Italija', 'Portugalija', 'Ispanija', 'Vokietija'],
#     'Gyventoju skaicius mln.': [3, 10, 12, 15, 20],
#     'BVP, mlrd, USD': [86, 100, 200, 150, 250]
# }
# df= pd.DataFrame(data)
# df['BVP vienam gyventojui, USD'] = (df['BVP, mlrd, USD'] * 1e9) / (df['Gyventoju skaicius mln.'] * 1e6)
# # print(df)
#
# didziausias_bvp_vienam_gyventojui = df[df['BVP vienam gyventojui, USD'] == df['BVP vienam gyventojui, USD'].max()]['Salis']
# # print(f'Didziausias BVP vienam gyventojui yra: {didziausias_bvp_vienam_gyventojui.iloc[0]}')   #iloc integer location
#
# def kategorijos(bvp):
#     if bvp < 100:
#         return 'Maza ekonomika'
#     elif 100 < bvp < 1000:
#         return 'Vidutine ekonomika'
#     else:
#         return 'Didele ekonomika'
#
# df['Ekonomikos kategorija'] = df['BVP, mlrd, USD'].apply(kategorijos)
# # print(df)
#
# vidutinis_bvp_vienam_gyventojui = df.groupby('Ekonomikos kategorija')['BVP vienam gyventojui, USD'].mean().reset_index()
# print(vidutinis_bvp_vienam_gyventojui)
#
#
# plt.figure(figsize=(10, 6))
# plt.bar(vidutinis_bvp_vienam_gyventojui['Ekonomikos kategorija'],
#          vidutinis_bvp_vienam_gyventojui['BVP vienam gyventojui, USD'], color='skyblue')
#
# plt.title('Vidutinis BVP vienam gyventojui pagal ekonomikos kategorija')
# plt.xlabel('Ekonomikos kategorija', fontsize=20)
# plt.ylabel('BVP vienam gyventojui, USD')
# # plt.xticks(rotation=45)
# plt.show()

"""
Sukurkite duomenų rinkinį, kuriame saugoma informacija apie įvairių knygų pardavimus per metus. Duomenys apima knygos pavadinimą, autorių, pardavimų skaičių ir išleidimo metus.
    * Raskite, kiek vidutiniškai buvo parduota knygų kiekvieno autoriaus.
    * Sukurkite naują stulpelį 'Amžius', kuriame būtų nurodyta, kiek metų knygai nuo jos išleidimo iki 2024 metų.
    * Apskaičiuokite, kuri knyga buvo parduota geriausiai kiekvieno autoriaus atžvilgiu. (Praleiskite)
    * Grupuokite duomenis pagal išleidimo metus ir apskaičiuokite, kiek knygų buvo išleista kiekvienais metais.
    
"""
#
# data = {
#     'Knygos pavadinimas': ['Apie geles', 'Lietuvos istorija', 'Egipto faraonai', 'Kleopatra', 'Lietuvos miskai'],
#     'Knygos autorius': ['Antanas Antanaitis', 'Antanas Antanaitis', 'Jhonas Jecksonas', 'Mary Keri', 'Antanas Antanaitis'],
#     'Pardavimu skaicius': [700, 1500, 600, 530, 1000],
#     'Isleidimo metai': [2009, 1990, 1975, 1975, 2013]
# }
# df = pd.DataFrame(data)
#
# vidutiniskai_parduota_knygu_autoriui = df.groupby('Knygos autorius')['Pardavimu skaicius'].mean().reset_index()
# # print(vidutiniskai_parduota_knygu_autoriui)
#
# df['Amzius'] = (2024 - df['Isleidimo metai'])
# # print(df)
#
# max_pardavimai = df.groupby('Knygos autorius')['Pardavimu skaicius'].transform('max') == df['Pardavimu skaicius']
# geriausiai_parduotos_knygos = df[max_pardavimai]
# print(geriausiai_parduotos_knygos[['Knygos autorius', 'Knygos pavadinimas', 'Pardavimu skaicius']])
# # max_pardavimai = df.groupby('Autorius')['Pardavimai'].transform('max') == df['Pardavimai']
# # geriausiai_parduotos_knygos = df[max_pardavimai]
# # # print(geriausiai_parduotos_knygos[['Autorius', 'Knygos pavadinimas', 'Pardavimai']])
#
# grupuoti_pagal_metus = df.groupby('Isleidimo metai').size()
# # print(grupuoti_pagal_metus)

"""
Modesto variantas
"""

# import pandas as pd
# import numpy as np
#
# data = {
#     'Knygos pavadinimas': ['Haris Poteris ir Išminties Akmuo', 'Haris Poteris ir Paslapčių Kambarys', 'Saulėlydis', 'Niekieno vaikai', 'Haris Poteris ir Azkabano kalinys'],
#     'Autorius': ['J.K. Rowling', 'J.K. Rowling', 'Stephenie Meyer', 'Lina Žutautė', 'J.K. Rowling'],
#     'Pardavimai': [120000, 150000, 130000, 50000, 170000],
#     'Išleidimo metai': [1997, 1998, 2005, 2019, 1999]
# }
# df = pd.DataFrame(data)
#
# vidutiniai_pardavimai = df.groupby('Autorius')['Pardavimai'].mean()
# # print(vidutiniai_pardavimai)
#
# df['Amzius'] = 2024 - df['Išleidimo metai']
# # print(df)
# max_pardavimai = df.groupby('Autorius')['Pardavimai'].transform('max') == df['Pardavimai']
# geriausiai_parduotos_knygos = df[max_pardavimai]
# # print(geriausiai_parduotos_knygos[['Autorius', 'Knygos pavadinimas', 'Pardavimai']])
#
# knygos_pagal_metus = df.groupby('Išleidimo metai').size()
# print(knygos_pagal_metus)

"""
Sukurkite mokyklos bibliotekos knygų duomenų rinkinį, kuriame saugoma informacija apie knygas, 
jų žanrus, puslapių skaičių, ir ar knyga yra skolinama. Jūsų užduotis – atlikti duomenų analizę ir vizualizaciją, 
naudojant pandas ir matplotlib. 
    * Sukurkite naują stulpelį Skaitymo trukmė (val), kuris apskaičiuotų, 
    kiek vidutiniškai laiko (valandomis) užtruktų perskaityti knygą, jei žmogus skaitytų 100 puslapių per valandą.
    * Apskaičiuokite, kiek vidutiniškai puslapių turi knyga kiekviename žanre.
    * Filtruokite ir atspausdinkite tik tas knygas, kurios yra skolinamos ir turi daugiau nei 300 puslapių.
    * Naudodami matplotlib, nubrėžkite stulpelinę diagramą, kurioje vaizduojamas knygų skaičius kiekviename žanre. (Nebūtina)
"""
data = {
    'Knygos pavadinimas': ['Apie meile', 'Lietuvos istorija', 'Egipto faraonai', 'Kleopatra', 'Lietuvos miskai'],
    'Zanras': ['romanas', 'istotine', 'istotine', 'romanas', 'publicistika'],
    'Puslapiu skaicius': [300, 600, 600, 530, 400],

}
df = pd.DataFrame(data)

df['Reikia dienu vienai knygai'] = df['Puslapiu skaicius'] / 100
# print(df)

vidutiniskai_psl_pagal_zanra = df.groupby('Zanras')['Puslapiu skaicius'].mean()
# print(f'Vidutiniskai psl pagal zanra: {vidutiniskai_psl_pagal_zanra}')

knygu_skaicius_pagal_zanra = df.groupby('Zanras').size()
# grupuoti_pagal_metus = df.groupby('Isleidimo metai').size()
# print(knygu_skaicius_pagal_zanra)
df['zanras'] = 'Zanras'
df['Knygos pavadinimas'] = 'Knygos pavadinimas'



# def ar_skolinama(knyga):
#     if len(knyga) >= 3:
#         print("Nneskolinama")
#         return
#     if knyga.arSkolinama:
#         print("Knyga jau išduota.")
#         return
#     knyga.arSkolinama = True
#
#     ar_skolinama.append(knyga)
#     print(f"{'Knygos pavadinimas'} skolinama ")
#     return True

#
#
#
plt.figure(figsize=(10, 6))
plt.bar(knygu_skaicius_pagal_zanra['Zanras'], knygu_skaicius_pagal_zanra['Knygos pavadinimas'], color='skyblue')

plt.title('Knygų skaičius kiekviename žanre')
plt.xlabel('Zanras', fontsize=20)
plt.ylabel('Knygu skaicius pagal zanra')
plt.xticks(rotation=45)
plt.show()


# plt.figure(figsize=(10, 6))
# plt.bar(vidutinis_bvp_vienam_gyventojui['Ekonomikos kategorija'],
#          vidutinis_bvp_vienam_gyventojui['BVP vienam gyventojui, USD'], color='skyblue')
#
# plt.title('Vidutinis BVP vienam gyventojui pagal ekonomikos kategorija')
# plt.xlabel('Ekonomikos kategorija', fontsize=20)
# plt.ylabel('BVP vienam gyventojui, USD')
# # plt.xticks(rotation=45)
# plt.show()