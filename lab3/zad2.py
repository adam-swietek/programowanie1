while True:
    print('========== KALKULATOR ==========\n1. Dodawanie\n2. Odejmowanie\n3. Mnozenie\n4. Dzielenie\n5. Potegowanie\n6. Srednia z podanych liczb\n0. Zakoncz\n================================')

    wybor = int(input('Wybierz opcje: '))
    if wybor == 0:
        break
    elif wybor == 1:
        try:
            liczba1 = int(input('Liczba 1: '))
            liczba2 = int(input('Liczba 2: '))
            print(f'Wynik: {liczba1} + {liczba2} = {liczba1 + liczba2}')
        except ValueError:
            print('Podane liczby to nie wartosci liczbowe')
    elif wybor == 2:
        try:
            liczba1 = int(input('Liczba 1: '))
            liczba2 = int(input('Liczba 2: '))
            print(f'Wynik: {liczba1} - {liczba2} = {liczba1 - liczba2}')
        except ValueError:
            print('Podane liczby to nie wartosci liczbowe')
    elif wybor == 3:
        try:
            liczba1 = int(input('Liczba 1: '))
            liczba2 = int(input('Liczba 2: '))
            print(f'Wynik: {liczba1} * {liczba2} = {liczba1 * liczba2}')
        except ValueError:
            print('Podane liczby to nie wartosci liczbowe')
    elif wybor == 4:
        try:
            liczba1 = int(input('Liczba 1: '))
            liczba2 = int(input('Liczba 2: '))
            if liczba2 != 0:
                print(f'Wynik: {liczba1} / {liczba2} = {liczba1 / liczba2}')
            else:
                print('Nie można dzielić przez zero')
        except ValueError:
            print('Podane liczby to nie wartosci liczbowe')
    elif wybor == 5:
        try:
            liczba1 = int(input('Liczba 1: '))
            liczba2 = int(input('Liczba 2: '))
            print(f'Wynik: {liczba1} ** {liczba2} = {liczba1 ** liczba2}')
        except ValueError:
            print('Podane liczby to nie wartosci liczbowe')
    elif wybor == 6:
        suma = 0
        try:
            ile = int(input('Ile liczb? '))
            if ile > 0:
                for i in range(1, ile+1):
                    try:
                        liczba = int(input(f'Liczba {i}: '))
                        suma += liczba
                    except ValueError:
                        print('Podana liczba to nie wartość liczbowa')
                        break
                print(f'Srednia: {suma/ile}')
            else:
                print('Zła liczba elementów')
        except ValueError:
            print('Podana wartość to nie liczba')
    else:
        print('Nieznana opcja menu')
