samolot = {'nazwa': 'boeing',
           'przebieg': 10000,
           'typ': 'pasazerski'}

#magazyn = {'x01': 'mleko', 'x02': 'ser'}
# print(magazyn['x01'])

#print(samolot['xyz'])
print(samolot.get('xyz'))

for key in samolot:
    print("{0}: {1}".format(key, samolot[key]))

print("-----------------------------")
for key, value in samolot.items():
    print(key, value)
print("-----------------------------")
if 'ilosc_pasazerow' not in samolot:
    print('uwaga: nie mam infromacji o pasazerach. PRzyjmuje samolot transportowy!')

print("-----------------------------")
magazyn = [
    {'nazwa': 'mleko',
     'cena': 12},
    {'nazwa': 'czekolada',
     'cena': 12},
    {'nazwa': 'tyskie',
     'cena': 12},
    {'nazwa': 'audi',
     'cena': 12},
]

for pozycja in magazyn:
    print(pozycja['nazwa'])
