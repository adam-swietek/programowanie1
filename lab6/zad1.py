import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('magazyny.csv', encoding='utf-8-sig')
print(df.head())

df = df[['magazyn', 'miasto', 'wojewodztwo', 'produkty']]

ile = 0

for i in df['magazyn']:
    ile += 1

print(f'\nLiczba magazynów: {ile}\n')

df = df.sort_values('produkty', ascending=False)

print(df[['magazyn', 'miasto', 'produkty']].head())

print(f'\nŁączna liczba produktów: {df["produkty"].sum()}\n')

df_wykres = df[['magazyn', 'produkty']].head(10)

plt.barh(df_wykres['magazyn'], df_wykres['produkty'])
plt.gca().invert_yaxis()
plt.xlabel('Liczba produktów')
plt.ylabel('Magazyn')
plt.show()

print(f'Najwiecej produktów znajduje się w magazynie:\n {df.iloc[0]['magazyn']} {df.iloc[0]['miasto']} {df.iloc[0]['produkty']}')
print(f'Roznica miedzy pierwszym a piątym magazynem wynosi: {df.iloc[0]['produkty'] - df.iloc[4]['produkty']}')