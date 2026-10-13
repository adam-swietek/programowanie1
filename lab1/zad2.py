liczba_puntkow = int(input('Podaj liczbę punktów z egzaminu: '))

ocena = 0

poprawne_dane = True

if liczba_puntkow >= 0 and liczba_puntkow < 50:
    ocena = 2.0
elif liczba_puntkow >= 50 and liczba_puntkow < 60:
    ocena = 3.0
elif liczba_puntkow >= 60 and liczba_puntkow < 70:
    ocena = 3.5
elif liczba_puntkow >= 70 and liczba_puntkow < 80:
    ocena = 4.0
elif liczba_puntkow >= 80 and liczba_puntkow < 90:
    ocena = 4.5
elif liczba_puntkow >= 90 and liczba_puntkow <= 100:
    ocena = 5.0
else:
    poprawne_dane = False
    print('Błędne dane!')

if poprawne_dane:
    print(f'Liczba uzyskanych punktów: {liczba_puntkow}')
    print(f'Ocena: {ocena}')
