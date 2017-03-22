import pandas as pd

df = pd.read_csv("otodom_gdansk.csv")


pokoje = df['liczba pokoi'].str.len() < 15
df = df[pokoje]
pietro = df['piętro'].str.len() < 15
df = df[pietro]
rynek = df['rynek'].str.len() < 10
df = df[rynek]
cena = df['cena (zł)'].str.len() < 11
df = df[cena]
pow = df['powierzchnia'].str.len() < 11
df = df[pow]

df['cena (zł)'] = df['cena (zł)'].str.replace(' ', '')
df['cena (zł)'] = df['cena (zł)'].str.replace(',', '.')
df['cena (zł)'] = df['cena (zł)'].astype(float)

df['powierzchnia'] = df['powierzchnia'].str.replace(' ', '')
df['powierzchnia'] = df['powierzchnia'].str.replace(',', '.')
df['powierzchnia'] = df['powierzchnia'].astype(float)

df2 = df

df = pd.read_csv("otodom_gdansk_part2.csv")

pokoje = df['liczba pokoi'].str.len() < 15
df = df[pokoje]
pietro = df['piętro'].str.len() < 15
df = df[pietro]
rynek = df['rynek'].str.len() < 10
df = df[rynek]
cena = df['cena (zł)'].str.len() < 11
df = df[cena]
pow = df['powierzchnia'].str.len() < 11
df = df[pow]

df['cena (zł)'] = df['cena (zł)'].str.replace(' ', '')
df['cena (zł)'] = df['cena (zł)'].str.replace(',', '.')
df['cena (zł)'] = df['cena (zł)'].astype(float)

df['powierzchnia'] = df['powierzchnia'].str.replace(' ', '')
df['powierzchnia'] = df['powierzchnia'].str.replace(',', '.')
df['powierzchnia'] = df['powierzchnia'].astype(float)

c = pd.concat([df2,df])

c.to_csv("gdansk.csv")

