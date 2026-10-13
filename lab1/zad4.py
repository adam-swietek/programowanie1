wiek = int(input('Podaj wiek: '))
zgoda = ''
dokument = ''

if wiek >= 13 and wiek < 18:
    zgoda = input('Czy masz zgode opiekuna? ')

if wiek >= 18 or zgoda.lower() == 'tak':
    dokument = input('Czy masz dokument tozsamosci? ')

if (wiek >= 18 and dokument.lower() == 'tak') or (zgoda.lower() == 'tak' and dokument.lower() == 'tak'):
    print('Wypozyczenie mozliwe')
else:
    print('Wypozyczenie niemozliwe')

