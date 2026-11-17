import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('klienci.csv', encoding='utf-8-sig')
print(df.head())

print(f'Liczba klientów: {len(df)}\n')

df = df[['klient', 'miasto', 'wojewodztwo', 'zamowienia']]

df = df.sort_values('zamowienia', ascending=False)

print('TOP 5 Klientów:')
print(df.head()[['klient', 'miasto', 'zamowienia']])

print(f'Łączna liczba zamówionych sztuk: {df['zamowienia'].sum()}\n')

df['udzial_procent'] = round((df['zamowienia'] / df['zamowienia'].sum()) * 100, 2)

print('TOP 5 Klientów:')
print(df.head()[['klient', 'miasto', 'zamowienia', 'udzial_procent']])

df_wykres = df[['klient', 'zamowienia']].head(10)

plt.bar(df_wykres['klient'], df_wykres['zamowienia'])
plt.xlabel('klient')
plt.ylabel('Liczba zamówień')
plt.show()

# Narysować prosty wykres kołowy z dwoma częściami: TOP 10 klientów oraz wszyscy pozostali.
# Udziały na wykresie powinny łącznie wynosić 100%.

top10 = df['zamowienia'].head(10).sum()
pozostali = df['zamowienia'].iloc[10:].sum()

plt.pie([top10, pozostali], labels = ['TOP 10', 'Pozostali'], autopct='%1.1f%%')
plt.title('Udział zamówień TOP 10 klientów vs pozostali')
plt.show()

# Pytania

print(f'Klient który zamówił najwięcej sztuk: {df.iloc[0]['klient']}')
print(f'Procent wszystkich zamówień złożonych przez TOP 10 klientów: {round(df['udzial_procent'].head(10).sum(), 0)}%')