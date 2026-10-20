temperatury = []
powyzej_sredniej = []

for i in range(1, 8):
    pomiar = int(input(f'Dzien {i}: '))
    temperatury.append(pomiar)

srednia = sum(temperatury) / 7
print(f'Srednia: {srednia} C')

print(f'Najwyzsza: {max(temperatury)} C')
print(f'Najnizsza: {min(temperatury)} C')

for i in temperatury:
    if i > srednia:
        powyzej_sredniej.append(i)

print(f'Powyzej sredniej: {powyzej_sredniej}')
print(f'Liczba dni: {len(powyzej_sredniej)}')
