import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('magazyny.csv')

print(df.columns)

df = df[['magazyn', 'miasto', 'wojewodztwo', 'produkty']]

woj = input('Podaj wojewodztwo: ').lower()
min_produktow = int(input('Minimum produktow: '))

df = df[(df['wojewodztwo'] == woj) & (df['produkty'] >= min_produktow)]

if df.empty:
    print('Brak magazynów spełniających kryteria')
else:
    df = df.sort_values('produkty', ascending=False)

    print('Znalezione magazyny:')
    print(df[['magazyn', 'miasto', 'produkty']])

    print(f'Liczba znalezionych magazynów: {len(df)}\n')
    print(f'Liczba produktów w znalezionych magazynach: {df["produkty"].sum()}\n')

    #wykres poziomy

    plt.barh(df['magazyn'], df['produkty'])
    plt.gca().invert_yaxis()
    plt.title('Top 5 magazynów z znalezionych')
    plt.xlabel('Liczba produktów')
    plt.ylabel('Magazyn')
    plt.show()

    print(f'Najwiecej produktów znajduje się w magazynie: {df.iloc[0]["magazyn"]}')
