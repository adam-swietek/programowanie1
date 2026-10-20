lista = []
ile = int(input('Ile produktów chcesz dodać? '))

for i in range(1, ile+1):
    dodaj = input(f'Produkt {i}: ')
    lista.append(dodaj)

print(f'Lista: {lista}')
print(f'Liczba produktow: {len(lista)}')
usun = input('Podaj produkt do usuniecia: ')

if usun in lista:
    lista.remove(usun)
    print(f'Nowa lista: {lista}')
else:
    print('Nie ma takiego produktu w liscie')