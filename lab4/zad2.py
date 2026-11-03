produkty = []
ceny = []

ile = int(input('Liczba produktów: '))

for i in range(1, ile+1):
    produkt = input(f'Produkt {i}: ')
    cena = int(input(f'Cena: '))
    produkty.append(produkt)
    ceny.append(cena)

for idx, produkt in enumerate(produkty, start=1):
    print(f'{idx}. {produkt}')

licznik = 0

print('=== CENNIK ===')
for para in zip(produkty, ceny):
    print(f'{licznik}. {para[0]} - {para[1]}')
    licznik += 1

print(f'Suma cen: {sum(ceny)} zł')
print(f'Najdroższy produkt: {max(zip(produkty, ceny), key=lambda x: x[1])[0]} - {max(zip(produkty, ceny), key=lambda x: x[1])[1]} zł')

