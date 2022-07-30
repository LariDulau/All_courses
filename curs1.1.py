'''
in cursul acesta facem variabile, tipuri de variabile, exercitii cu string
'''

print('hei, Lari:)')

marca_masina = 'Volvo'
model_masina = 'XC60'
motor = 2
Motor = 3 # key sensitive M m
site = 'www.emag.ro'
lungime = 10
latime = 5

print(marca_masina)
print(model_masina)
print(motor)
print(Motor)
print(lungime*latime)

# atribuire de valori in aceeasi linie
strada, numar, apartament = 'Somesului', 105, 1
print(numar)

# atribuirea aceleiasi valori la mai multe variabile
lungime = latime = 5
print(lungime)
print(latime)

# tipuri de date
# int = nr intregi
varsta = 10

# float = nr cu virgula
pret = 3.5

# bool(ean) = true/false
e_deschis_la_magazin = True

# string = cuvinte/propozitii
nume = 'Lari'

print(type(pret))
print(type(nume))

# transformare string in int = type casting
varsta2 = '4'
print(type(varsta2))
varsta2 = int(varsta2)
print(type(varsta2))

print('ana are mere')

# print valori de tip diferit!
name = 'Ana'
age = 45
print('Eleva ' + name + ' are varsta de ' + str(age)) # modu 1
print(f'Eleva {name} are varsta de {age}') # modu 2 (better) - recomandat!

# assert = verificari (la final)
assert site == 'www.emag.ro'

# input - introduci in consola numele/numere ceva orice
cursant1 = input('Vreau numele primului cursant')
print(cursant1)
lungime = int(input('lungimea este'))
latime = int(input('latimea este'))
print(f'aria este {lungime*latime}')

# string index: print(nume clasa[index])
compunere = 'Ana are mere'
print(compunere[1])
print(compunere[0:4]) # de unde incepe pana unde se termina-1 (0 pana la 4-1=3)
print(compunere[8:12:2]) # unde incepe, unde se termina, din cat in cat
print(compunere[0:12:2]) # numerele din 2 in 2 de la inceput-final
print(compunere[::2]) # same, de la primu la ultimu din 2 in 2
print(compunere[len(compunere)-1])
print(compunere[::-1]) # -1 invers, daca nu pui de unde pana unde ia de la inceput la final(palindrom)

# pt a afla ultima litera
# asa se recomanda
print(len(compunere)) # aflam lungimea
print(compunere[len(compunere)-1]) # lungime - 1

# pt toata propozitia
print(compunere[0:len(compunere)])

# metodele ce le punem in fata la numele variabile -- print direct
# len

# metode '.upper' etc.(si nu au is in nume) trebuie sa le atribuim variabilei/suprascriem
compunere = compunere.upper()
compunere = compunere.replace('ANA', 'MARIA')
print(compunere)
print(compunere.isupper())

compunere_upper = 'ANA ARE CARTI'
# verificam in assert ca textul nostru contine doar litere mari
assert compunere_upper.isupper() == True

# suprascriere
carte = 'lista lui ion'
print(carte)
carte = 'noapte de vara'
print(carte)

nume = 'ion'
print(nume*3)
