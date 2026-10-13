wysokosc = int(input('Podaj wysokosc choinki: '))

ilosc_gwiazdek = 1

for i in range(1, wysokosc+1):
    print(' '*(wysokosc-i)+('*'*ilosc_gwiazdek)+' '*(wysokosc-i))
    ilosc_gwiazdek += 2