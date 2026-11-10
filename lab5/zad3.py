import pandas as pd

produkty = ['Mysz', 'Klawiatura', 'Monitor', 'Podkładka']
ceny = [50, 120, 650, 30]
ilosc = [10, 5, 3, 20]

df = pd.DataFrame({
    'Produkt': produkty,
    'Cena': ceny,
    'Ilość': ilosc
})

df['Wartość'] = df['Cena'] * df['Ilość']

print(df)
print('\n')
print('Produkty powyżej 100 zł:')
print(df[df['Cena'] > 100]['Produkt'])
print('\n')
print(f'Wartość magazynu: {df["Wartość"].sum()}')
print(f'Średnia cena: {df["Cena"].mean()}')