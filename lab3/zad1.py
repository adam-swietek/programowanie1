kontakty = {}

while True :

    print('========== KSIAZKA KONTAKTOW ==========\n1. Dodaj kontakt\n2. Wyswietl wszystkie kontakty\n3. Wyszukaj kontakt\n4. Edytuj kontakt\n5. Usun kontakt\n0. Zakoncz\n=======================================')

    wybor = int(input('Wybierz opcje: '))
    if wybor == 0:
        break
    elif wybor == 1:
        imie = input('Imie: ')
        nazwisko = input('Nazwisko: ')
        telefon = input('Telefon: ')
        if telefon not in kontakty:
            kontakty[telefon] = [imie, nazwisko]
            print('Kontakt dodany')
        else:
            print('Kontakt już istnieje')
    elif wybor == 2:
        if kontakty:
            for key, value in kontakty.items():
                print(f'{value[0]} {value[1]} tel. {key}')
        else:
            print('Brak kontaktów')
    elif wybor == 3:
        szukaj = input('Podaj numer telefonu: ')
        if szukaj in kontakty:
            print(f'{kontakty[szukaj][0]} {kontakty[szukaj][1]}')
        else:
            print('Kontakt nie istnieje')
    elif wybor == 4:
        podmien = input('Podaj numer telefonu kontaktu: ')
        if podmien in kontakty:
            imie = input('Nowe imie: ')
            nazwisko = input('Nowe nazwisko: ')
            kontakty[podmien] = [imie, nazwisko]
            print('Kontakt zmodyfikowany')
        else:
            print('Kontakt nie istnieje')
    elif wybor == 5:
        usun = input('Podaj numer telefonu do usuniecia: ')
        if usun in kontakty:
            kontakty.pop(usun)
            print('Kontakt usuniety')
        else:
            print('Kontakt nie istnieje')