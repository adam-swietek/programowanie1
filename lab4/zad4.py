warsztat_python = set()
warsztat_ai = set()

while True:
    print('1. Zapisz na python')
    print('2. Zapisz na AI')
    print('3. Wyświetl uczestników')
    print('4. Uczestnicy obu warsztatów')
    print('5. Wszyscy unikalni uczestnicy')
    print('0. Zakończ')

    wybor = int(input('Wybierz opcje: '))

    if  wybor == 0:
        break
    elif wybor == 1:
        imie = input('Imie: ')
        nazwisko = input('Nazwisko: ')
        warsztat_python.add((imie, nazwisko))
    elif wybor == 2:
        imie = input('Imie: ')
        nazwisko = input('Nazwisko: ')
        warsztat_ai.add((imie, nazwisko))
    elif wybor == 3:
        print('Uczestnicy warsztat python:')
        for i in warsztat_python:
            print(i[0], i[1])
        print('Uczestnicy warsztat AI:')
        for i in warsztat_ai:
            print(i[0], i[1])
    elif wybor == 4:
        print('Uczestnicy obu warsztatów:')
        print(warsztat_python & warsztat_ai)
    elif wybor == 5:
        print('Wszyscy unikalni uczestnicy:')
        print(warsztat_python | warsztat_ai)