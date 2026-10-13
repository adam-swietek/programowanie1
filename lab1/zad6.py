temperatura = int(input('Podaj temperature: '))
ktos_w_domu = input('Czy ktos jest w domu? ')
okno_otwarte = input('Czy okno jest otwarte? ')

stan_ogrzewania = True
powod = ''


if okno_otwarte.lower() == 'tak':
    stan_ogrzewania = False
    powod = 'Okno otwarte'

if stan_ogrzewania and okno_otwarte.lower() == 'nie' and ktos_w_domu.lower() == 'tak' and temperatura >= 20:
    stan_ogrzewania = False
    powod = 'Temperatura powyzej 20 stopni'
elif stan_ogrzewania and okno_otwarte.lower() == 'nie' and ktos_w_domu.lower() == 'tak' and temperatura < 20:
    powod = 'Temperatura ponizej 20 stopni'

if stan_ogrzewania and okno_otwarte.lower() == 'nie' and ktos_w_domu.lower() == 'nie' and temperatura >= 16:
    stan_ogrzewania = True
    powod = 'Temperatura powyzej 16 stopni a nikogo nie ma w domu'
elif stan_ogrzewania and okno_otwarte.lower() == 'nie' and ktos_w_domu.lower() == 'nie' and temperatura < 16:
    powod = 'Temperatura ponizej 16 stopni i nikogo nie ma w domu'

if stan_ogrzewania:
    print('Ogrzewanie: WLACZONE')
else:
    print('Ogrzewanie: WYLACZONE')

print(powod)