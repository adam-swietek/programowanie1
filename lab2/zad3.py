napoje = ["Woda", "Sok", "Cola"]
ceny = [3, 5, 6]

razem = list(zip(napoje, ceny))

for i, elem in enumerate(razem, start=1):
    print(f'{i}. {elem[0]} - {elem[1]} zl')

print('0. Zakoncz')

do_zaplaty = 0

while True:
    opcja = int(input('Wybierz opcje: '))

    if opcja == 0:
        print(f'Lacznie do zaplaty: {do_zaplaty}')
        break
    elif opcja < 0 or opcja > 3:
        print('Nieprawidlowy numer opcji')
    else:
        print(f'Wybrano: {razem[opcja - 1][0]}, cena: {razem[opcja - 1][1]} zl.')
        do_zaplaty += razem[opcja-1][1]