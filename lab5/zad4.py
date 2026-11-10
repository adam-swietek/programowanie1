import pandas as pd
import matplotlib.pyplot as plt

nazwiska = []
punkty = []
oceny = []

ile = int(input('Podaj liczbe studentow: '))

for i in range(ile):
    nazwisko = input(f'Podaj nazwisko studenta {i+1}: ')
    nazwiska.append(nazwisko)
    punkt = int(input(f'Podaj punkty studenta {i+1}: '))
    punkty.append(punkt)

df = pd.DataFrame({
    'Nazwisko': nazwiska,
    'Punkty': punkty
})

for punkt in punkty:
    if punkt >= 0 and punkt < 50:
        oceny.append(2.0)
    elif punkt >= 50 and punkt < 60:
        oceny.append(3.0)
    elif punkt >= 60 and punkt < 70:
        oceny.append(3.5)
    elif punkt >= 70 and punkt < 80:
        oceny.append(4.0)
    elif punkt >= 80 and punkt < 90:
        oceny.append(4.5)
    elif punkt >= 90 and punkt <= 100:
        oceny.append(5.0)

df['Ocena'] = oceny

print(df, '\n')
print(f'Średnia ocen: {df["Ocena"].mean()}')
print(f'Liczba zaliczen: {len(df[df["Ocena"] >= 3.0])}')

print('----Posortowane dane----')

df_sorted = df.sort_values("Punkty", ascending=False)
print(df_sorted, '\n')

plt.bar(df['Nazwisko'], df['Ocena'])
plt.title("Wyniki egzaminu")
plt.xlabel('Student')
plt.ylabel('Ocena')
plt.ylim(0, 5.5)
plt.tight_layout()
plt.show()

plot = df.plot(x='Nazwisko', y='Ocena', kind='bar', legend=False)
plt.show()