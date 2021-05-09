samochody = ['syrena', 'poloneza', 'audi', 'bmw']
print(samochody[2])
print(len(samochody))

for x in samochody:
 print(x)

for idx in range(len(samochody)) :
 #print(str(idx) + " : " + samochody[idx])
 print("{0} : {1}".format(idx, samochody[idx]))
