cena = int(input('Podaj cenę produktu: '))
sztuki = int(input('Podaj liczbę sztuk: '))

koszt_dostawy = 12
wartosc_produktow = cena * sztuki

print(f'Wartość produktów: {wartosc_produktow}zł')

if cena >= 100:
    print('Koszt dostawy: 0zł')
    print(f'Do zapłaty: {wartosc_produktow}')
else:
    print(f'Koszt dostawy: {koszt_dostawy}zł')
    print(f'Do zapłaty: {wartosc_produktow + koszt_dostawy}zł')

