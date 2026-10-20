liczba_studentow = int(input('Podaj liczbe studentow: '))
punkty = []
liczba_zaliczen = 0

for i in range(1, liczba_studentow+1):
    punkty_studenta = int(input(f'Punkty studenta {i}: '))
    punkty.append(punkty_studenta)

srednia = sum(punkty) / len(punkty)
print(f'Srednia: {srednia}')

print(f'Najwyzszy wynik: {max(punkty)}')
print(f'Najnizszy wynik: {min(punkty)}')

print(f'Wyniki rosnaco: {sorted(punkty)}')

for i in punkty:
    if i >= 50:
        liczba_zaliczen += 1

print(f'Liczba zaliczen: {liczba_zaliczen}')