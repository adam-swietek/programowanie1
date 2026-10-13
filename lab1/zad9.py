poczatek = int(input('Podaj poczatek zakresu: '))
koniec = int(input('Podaj koniec zakresu: '))

ile_parzystych = 0

for i in range(poczatek, koniec+1):
    if i % 2 == 0:
        print(f'{i} - Parzysta')
        ile_parzystych += 1
    else:
        print(f'{i} - Nieparzysta')

print(f'Liczba liczb parzystych: {ile_parzystych}')