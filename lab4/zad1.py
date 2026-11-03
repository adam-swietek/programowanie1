pomiary = []

ile = int(input('Ile pomiarów chcesz wprowadzić? '))

for i in range(1, ile+1):
    pom = int(input(f'Pomiar {i}. '))
    pomiary.append(pom)

print(f'Pierwszy pomiar: {pomiary[0]}')
print(f'Ostatni pomiar: {pomiary[-1]}')

if len(pomiary) >= 3:
    print(f'Pierwsze trzy: {pomiary[:3]}')
else:
    print(f'Pierwsze trzy: {pomiary}')

print(f'Co drugi pomiar: {pomiary[::2]}')
print(f'Odwrocona lista: {pomiary[::-1]}')

pomiary_kopia = pomiary.copy()

pomiary_kopia[0] = 0

print(f'Oryginal: {pomiary}')
print(f'Kopia po zmianie: {pomiary_kopia}')