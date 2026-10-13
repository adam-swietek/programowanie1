kwota_odkladana = int(input('Ile odkładasz tygodniowo? '))
okres_oszczedzania = int(input('Przez ile tygodni? '))

oszczednosci = 0

for i in range(1, okres_oszczedzania+1):
    oszczednosci += kwota_odkladana
    print(f'Tydzień {i}: {oszczednosci} zł')

print(f'Łączne oszczędności: {oszczednosci}')