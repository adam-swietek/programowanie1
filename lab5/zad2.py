import numpy as np

ceny = []

ile = int(input('Podaj liczbe produktów: '))

for i in range(ile):
    cena = int(input(f'Podaj cene produktu {i+1}: '))
    ceny.append(cena)

rabat = int(input('Podaj rabat (%): '))

ceny = np.array(ceny)
ceny_po_rabacie = ceny * (1 - rabat/100)

print(f'Ceny początkowe: {ceny}')
print(f'Ceny po rabacie: {ceny_po_rabacie}')
print(f'Suma przed rabatem: {np.sum(ceny)} zł')
print(f'Suma po rabacie: {np.sum(ceny_po_rabacie)} zł')
print(f'Ceny powyzej 100zł: {ceny_po_rabacie[ceny_po_rabacie > 100]}')
