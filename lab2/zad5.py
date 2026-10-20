haslo = "Python123"
proby = 3

while True:
    if proby > 0:
        podaj_haslo = input('Podaj haslo: ')
        if podaj_haslo == haslo:
            print('Logowanie udane')
            break
        else:
            proby -= 1
            print(f'Niepoprawne haslo. Pozostale proby: {proby}')
    else:
        print('Konto zablokowane')
        break