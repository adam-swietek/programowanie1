ksiazki = []
dostepnosc = []

while True:
    print('========== BIBLIOTEKA ==========\n1. Dodaj ksiazke\n2. Wyswietl wszystkie ksiazki\n3. Wypozycz ksiazke\n4. Zwroc ksiazke\n5. Usun ksiazke\n0. Zakoncz\n===============================')

    wybor = int(input('Wybierz opcje: '))

    if wybor == 0:
        break
    elif wybor == 1:
        tytul = input('Tytul: ')
        autor = input('Autor: ')
        ksiazki.append({tytul: autor})
        dostepnosc.append(True)
    elif wybor == 2:
        idx = 0
        for ksiazka in ksiazki:
            print(f'{idx+1}. {list(ksiazka.items())[0][0]} {list(ksiazka.items())[0][1]} status: {'Dostępna' if dostepnosc[idx] else 'Niedostępna'}')
            idx += 1
    elif wybor == 3:
        numer = int(input('Wybierz numer: '))

        if dostepnosc[numer - 1]:
            dostepnosc[numer - 1] = False
            print(f'Wypożyczono: {list(ksiazki[numer-1].keys())[0]}')
        else:
            print('Ksiazka jest juz wypozyczona')
    elif wybor == 4:
        numer = int(input('Wybierz numer: '))
        if not dostepnosc[numer - 1]:
            dostepnosc[numer - 1] = True
            print(f'Zwrócono: {list(ksiazki[numer - 1].keys())[0]}')
        else:
            print('Książka nie jest wypożyczona')
    elif wybor == 5:
        numer = int(input('Wybierz numer: '))
        if ksiazki[numer - 1]:
            ksiazki.pop(numer - 1)
            dostepnosc.pop(numer - 1)
            print('Książka usunięta')
        else:
            print('Ksiazka nie istnieje')
    else:
        print('Nieznana opcja menu')
