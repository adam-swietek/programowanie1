dane = []

while True:
    print('''
========= MOJ BUDZET =========
1. Dodaj przychod
2. Dodaj wydatek
3. Wyswietl historie operacji
4. Wyswietl stan konta
5. Podsumowanie finansowe
6. Wyszukaj operacje
7. Usun operacje
0. Zakoncz
==============================''')
    stan_konta = 0
    wybor = int(input('Wybierz opcje: '))

    if wybor == 0:
        break
    elif wybor == 1:
        opis = input('Opis: ')
        kwota = int(input('Kwota: '))
        dane.append({opis: [kwota, 'przychod']})
        print('Dodano przychód')
    elif wybor == 2:
        opis = input('Opis: ')
        kwota = int(input('Kwota: '))
        dane.append({opis: [kwota, 'wydatek']})
        print('Dodano wydatek')
    elif wybor == 3:
        idx = 0
        for i in dane:
            print(f'{idx+1}. {list(i.keys())[0]} {list(i.values())[0][0]} zł {list(i.values())[0][1]}')
            idx += 1
    elif wybor == 4:
        for i in dane:
            if list(i.values())[0][1] == 'przychod':
                stan_konta += int(list(i.values())[0][0])
            else:
                stan_konta -= int(list(i.values())[0][0])
        print(f'Stan konta: {stan_konta} zl')
    elif wybor == 5:
        temp = []
        suma_przychodow = 0
        suma_wydatkow = 0
        for i in dane:
            if list(i.values())[0][1] == 'wydatek':
                temp.append(list(i.values())[0][0])
        najwiekszy_wydatek = max(temp)
        for i in dane:
            if list(i.values())[0][1] == 'przychod':
                suma_przychodow += int(list(i.values())[0][0])
            else:
                suma_wydatkow += int(list(i.values())[0][0])
        for i in dane:
            if list(i.values())[0][1] == 'przychod':
                stan_konta += int(list(i.values())[0][0])
            else:
                stan_konta -= int(list(i.values())[0][0])
        print(f'Suma przychodów: {suma_przychodow} zl')
        print(f'Suma wydatkow: {suma_wydatkow} zl')
        print(f'Bilans: {stan_konta} zl')
        print(f'Najwiekszy wydatek: {najwiekszy_wydatek} zl')
    elif wybor == 6:
        pass
    elif wybor == 7:
        usun = int(input('Podaj numer operacji do usuniecia: '))
        dane.pop(usun - 1)
        print('Operacja usunieta')

