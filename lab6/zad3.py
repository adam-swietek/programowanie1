import pandas as pd
import matplotlib.pyplot as plt

magazyny = pd.read_csv('magazyny.csv')
klienci = pd.read_csv('klienci.csv')

magazyny = magazyny[['wojewodztwo', 'produkty']]
klienci = klienci[['wojewodztwo', 'zamowienia']]

magazyny_grupowane = magazyny.groupby('wojewodztwo')['produkty'].sum()
klienci_grupowane = klienci.groupby('wojewodztwo')['zamowienia'].sum()

zlacz = pd.merge(magazyny_grupowane, klienci_grupowane, on='wojewodztwo')

zlacz['roznica'] = zlacz['produkty'] - zlacz['zamowienia']

zlacz = zlacz.reset_index()

zlacz = zlacz.sort_values('roznica')

print(zlacz)

# wykres slupkowy dla kazdego wojewodztwa
ax = zlacz[['wojewodztwo', 'produkty', 'zamowienia']].plot(x='wojewodztwo', y=['produkty', 'zamowienia'], kind='bar')
plt.legend(['Produkty', 'Zamowienia'])
plt.show()

# wykres slupkowy poziomy

ax = zlacz[['wojewodztwo', 'produkty', 'zamowienia']].plot(x='wojewodztwo', y=['produkty', 'zamowienia'], kind='barh')
plt.show()

print(f'Najmniejsza roznica: {zlacz.iloc[0]["wojewodztwo"]}')
print(f'W ilu wojewodztwach liczba produktow < liczba zamowien: {len(zlacz[zlacz["roznica"] < 0])}')