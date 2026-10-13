

def sprawdzenie_oceny(liczba_punktow):
    ocena = 0
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
    return ocena

ile_zaliczylo = 0

liczba_studentow = int(input('Podaj liczbe studentow'))

for i in range(1, liczba_studentow+1):
    nazwisko = input(f'Nazwisko stuenta {i}: ')
    liczba_puntkow = int(input('Punkty: '))
    if liczba_puntkow >= 0 and liczba_puntkow <= 100:
        print(f'{nazwisko} - {liczba_puntkow} - ocena {sprawdzenie_oceny(liczba_puntkow)}')
    else:
        print('Niepoprawne dane')
    if sprawdzenie_oceny(liczba_puntkow) >= 3.0:
        ile_zaliczylo += 1

print(f'Liczba studentow, ktorzy zaliczyli egzamin: {ile_zaliczylo}')

