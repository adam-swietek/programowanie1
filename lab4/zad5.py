def wyswietl_menu():
    print('========== KALKULATOR ==========\n1. Dodawanie\n2. Odejmowanie\n3. Mnozenie\n4. Dzielenie\n5. Potegowanie\n6. Srednia z podanych liczb\n0. Zakoncz\n================================')

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    return a / b if b != 0 else 'Nie dzielmy przez 0'

def potegowanie(a, b):
    return a ** b

def srednia_z_podanych(liczby):
    return sum(liczby) / len(liczby)

def main():
    wyswietl_menu()

    while True:
        wybor = int(input('Wybor: '))

        if wybor == 0:
            break
        elif wybor == 1:
            l1 = int(input('Liczba 1: '))
            l2 = int(input('Liczba 2: '))
            print(dodawanie(l1, l2))
        elif wybor == 2:
            l1 = int(input('Liczba 1: '))
            l2 = int(input('Liczba 2: '))
            print(odejmowanie(l1, l2))
        elif wybor == 3:
            l1 = int(input('Liczba 1: '))
            l2 = int(input('Liczba 2: '))
            print(mnozenie(l1, l2))
        elif wybor == 4:
            l1 = int(input('Liczba 1: '))
            l2 = int(input('Liczba 2: '))
            print(dzielenie(l1, l2))
        elif wybor == 5:
            l1 = int(input('Liczba: '))
            l2 = int(input('Potęga: '))
            print(potegowanie(l1, l2))
        elif wybor == 6:
            liczby = []
            ile = int(input('Ile liczb do sredniej: '))
            for i in range(1, ile+1):
                liczba = int(input(f'Liczba {i}: '))
                liczby.append(liczba)
            print(srednia_z_podanych(liczby))

if __name__ == '__main__':
    main()