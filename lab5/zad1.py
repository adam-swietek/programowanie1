import numpy as np

pomiary = []

ile = int(input('Podaj liczbe pomiarow: '))

for i in range(ile):
    pomiar = float(input(f'Pomiar {i+1}: '))
    pomiary.append(pomiar)

pomiary = np.array(pomiary)

print(f'Pomiary: {pomiary}')
print(f'Srednia: {np.mean(pomiary)} C')
print(f'Minimum: {np.min(pomiary)} C')
print(f'Maksimum: {np.max(pomiary)} C')
print(f'Rozstęp: {np.max(pomiary) - np.min(pomiary)} C')