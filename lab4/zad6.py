import matplotlib.pyplot as plt

def rysuj_wykres(nazwiska, oceny):
    plt.bar(nazwiska, oceny)
    plt.title("Wyniki egzaminu")
    plt.xlabel("Student")
    plt.ylabel("Ocena")
    plt.ylim(0, 5.5)
    plt.savefig('wykres.png')
    plt.show()

nazwiska = []
punkty = []
oceny = []

ile = int(input('Podaj liczbe studentów: '))

for i in range(1, ile+1):
    nazwisko = input(f'Podaj nazwisko {i} studenta: ')
    punkt = int(input(f'Podaj punkty {i} studenta: '))
    nazwiska.append(nazwisko)
    punkty.append(punkt)
    if punkt >= 0 and punkt < 50:
        oceny.append(2.0)
        print(f'{nazwisko} - 2.0')
    elif punkt >= 50 and punkt < 60:
        oceny.append(3.0)
        print(f'{nazwisko} - 3.0')
    elif punkt >= 60 and punkt < 70:
        oceny.append(3.5)
        print(f'{nazwisko} - 3.5')
    elif punkt >= 70 and punkt < 80:
        oceny.append(4.0)
        print(f'{nazwisko} - 4.0')
    elif punkt >= 80 and punkt < 90:
        oceny.append(4.5)
        print(f'{nazwisko} - 4.5')
    elif punkt >= 90 and punkt <= 100:
        oceny.append(5.0)
        print(f'{nazwisko} - 5.0')

srednia = sum(oceny) / len(oceny)
print(f'Srednia ocen: {srednia}')

zdalo = 0

for i in oceny:
    if i >= 3.0:
        zdalo += 1

print(f'Liczba zaliczen: {zdalo}')
print('Ładowanie wykresu...')
rysuj_wykres(nazwiska, oceny)

