marka = 'Peugeot    '
ilosc_drzwi = 5
pojemnosc = 1.3
marka_up = marka.upper()
marka_low = marka.lower()
marka_swap = marka.swapcase()
marka_rstrip = marka.rstrip()
print("Samochod " + marka_swap + " ma " + str(ilosc_drzwi) + " drzwi")
print("Samochod " + marka_rstrip + " ma " + str(ilosc_drzwi) + " drzwi")
print("Samochod " + marka + " ma " + str(ilosc_drzwi) + " drzwi")
print(marka_up)
print("Pojemnosc po zmianach: " + str(pojemnosc * 2))
print(marka_low)
