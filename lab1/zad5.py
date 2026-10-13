czas_parkowania = int(input('Podaj czas parkowania (h): '))
oplata = 0

if czas_parkowania <= 0:
    print('Błędne dane')
else:
    print(f'Czas postoju: {czas_parkowania} godziny')
    if czas_parkowania == 1:
        oplata = 5
    elif czas_parkowania > 1 and czas_parkowania <= 3:
        oplata = 12
    elif czas_parkowania > 3 and czas_parkowania <= 6:
        oplata = 20
    else:
        oplata = 30
    print(f'Opłata za parking: {oplata} zł')
    