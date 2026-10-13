cena = int(input('Podaj cenę produktu: '))
rabat = int(input('Podaj rabat (%): '))

kwota_rabatu = cena * (rabat / 100)
cena_po_rabacie = cena - kwota_rabatu

print(f'Cena początkowa: {cena} zł')
print(f'Kwota rabatu: {kwota_rabatu} zł')
print(f'Cena po rabacie: {cena_po_rabacie} zł')

if rabat >= 20:
    print('Duża promocja!')