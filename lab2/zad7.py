magazyn = {"Mysz": 5, "Klawiatura": 3, "Monitor": 2}

print('1. Stan magazynu')
print('2. Przyjecie towaru')
print('3. Wydanie towaru.')
print('0. Zakoncz')

while True:
    wybor = int(input('Wybierz opcje: '))
    if wybor == 0:
        print('Do widzenia!')
        break
    elif wybor < 0 or wybor > 3:
        print('Niepoprawny numer opcji')
    else:
        if wybor == 1:
            for produkt, ile in magazyn.items():
                print(f'{produkt}: {ile} szt.')
        elif wybor == 2:
            produkt = input('Podaj nazwe produktu: ')
            sztuki = int(input('Podaj liczbe sztuk: '))
            if produkt in magazyn:
                magazyn[produkt] += sztuki
            else:
                magazyn[produkt] = sztuki
            print('Zaktualizowano stan produktu')
        elif wybor == 3:
            produkt = input('Podaj nazwe produktu: ')
            sztuki = int(input('Podaj liczbe sztuk: '))
            if produkt not in magazyn:
                print('Nie ma takiego produktu')
                continue
            elif sztuki > magazyn[produkt]:
                print('Niewystarczająca ilość na magazynie')
                continue
            else:
                magazyn[produkt] -= sztuki
                print(f'Wydano {sztuki} szt.')