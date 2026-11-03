pomiary = []

ile = int(input('Podaj liczbe pomiarow: '))

for i in range(1, ile + 1):
    pomiar = int(input(f'{i}. Pomiar: '))
    pomiary.append(pomiar)

pomiary_alarmowe = [z for z in pomiary if z > 50]
pomiary_x2 = [z*2 for z in pomiary]

print(f'Pomiary alarmowe: {pomiary_alarmowe}')
print(f'Pomiary pomnozone przez 2 : {pomiary_x2}')
print(f'Czy wystąpił alarm? {'Tak' if any(x > 50 for x in pomiary) else 'Nie'}')
print(f'Czy wszystkie pomiary są prawidłowe? {'Tak' if all(x <= 50 for x in pomiary) else 'Nie'}')