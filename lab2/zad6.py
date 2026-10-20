zadania = []

print('1 - Dodaj zadanie,')
print('2 - Wyswietl zadania,')
print('3 - Usun zadanie,')
print('4 - Wyswietl liczbe zadan,')
print('0 - Zakoncz.')

while True:
    wybor = int(input('Wybierz opcje: '))
    if wybor == 0:
        print('Do widzenia!')
        break
    elif wybor < 0 or wybor > 4:
        print('Nieprawidlowy numer opcji')
    else:
        if wybor == 1:
            zadanie = input('Podaj zadanie: ')
            zadania.append(zadanie)
        elif wybor == 2:
            if zadania:
                for i in range(1, len(zadania)+1):
                    print(f'{i}. {zadania[i-1]}')
            else:
                print('Brak zadan')
        elif wybor == 3:
            if zadania:
                nr_zadania = int(input('Podaj numer zadania: ')) - 1
                if nr_zadania >= 0 and nr_zadania < len(zadania):
                    zadania.pop(nr_zadania)
            else:
                print('Brak zadan')
        elif wybor == 4:
            if zadania:
                print(f'Liczba aktualnych zadan: {len(zadania)}')
            else:
                print('Brak zadan')
    