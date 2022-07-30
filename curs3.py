# zi = input('Introdu o zi: ')

# # if simplu
# if zi == 'marti' or 'Marti':
#     print('Azi avem curs')
#
# if zi.lower() == 'marti': #adica orice litere punem le ia cu litera mica
#     print('Azi avem curs')

# # if else
# NOTA_DE_TRECERE_EXAMEN = 4.5
# NOTA_DE_TRECERE_PURTARE = 7
# nota_examen = float(input('Introdu nota examen: '))
# nota_purtare = float(input('Introdu nota purtare: '))
# if nota_examen >= NOTA_DE_TRECERE_EXAMEN and nota_purtare >= NOTA_DE_TRECERE_PURTARE:
#     print('Am trecut clasa')
#     if nota_examen == 10 and nota_purtare == 10:
#         print('Ai luat premiul I')
# else:
#     print('Nu ai trecut clasa')

# testam capetele 4.5 7, 10 10, ai picat, si random

# varsta = int(input('Introdu varsta: '))
# if varsta < 14:
#     print('Este minor')
# elif varsta < 18:
#     print('Este minor cu buletin')
# else:
#     print('Este major')

# # ex cu NOT ( daca nu e numele vasile sa printeze x, daca e vasile nu print nimic)
# nume = input('Introdu nume: ')
# if not (nume == 'Vasile'):
#     print('Numele nu corespunde')

'''
Curs 3 - Structuri de date
'''
# # 1. LIST []
# # = variabila in care se pastreaza mai multe valori
# # putem avea toate tipurile de date, poate avea duplicat (2x), este ordonata
# # putem adauga elemente noi sau putem sterge, putem moifica
# list1 = ['abc', 455, 34.5, True, 'mara', 'primavara', 45, 'abc']
#
# # lungimea unei liste
# print(len(list1))
#
# # cum accesam un element
# print(list1[1])
#
# # cum facem slicing
# print(list1[0:4])
# print(list1[:4])
# # cum afisam ultimul element
# print(list1[-1])
# print(list1[len(list1)-1])
#
# # suprascriere
# list1[0] = 'Elena'
# print(list1)
#
# # cum adaugam
# list1.insert(1, 10) # pe pozitia 1 vreau sa puna '10'
# print(list1)
# list1.append('Ioana') # adauga la final daca nu zic unde
# print(list1)
#
# # cum stergem
# list1.pop() # sterge ultimu daca nu zic care
# print(list1)
#
# list1.pop(0) # sterge elementul de pe pozitia ceruta
# print(list1)
#
# list1.remove('mara') # sterge elementul mentionat ( dupa valoare)
# print(list1)
#
# list2 = [2, 3, 'elena', [1, 2, 3], ['a', 'e', [3, 4, 5]], 'lola']
# print(list2[4])
# print(list2[4][0]) # de pe pozitia 4, pozitia 0 din 4
#
# import random # se pune la inceput
# luni = ['ian', 'feb', 'martie', 'aprilie']
# random_nr = random.randint(0,len(luni)-1)
# print(luni[random_nr])
#
# luna_curenta = input('Introdu luna: ')
# if luna_curenta in luni:
#     print('luna este buna')
#
# vocale = ['a', 'e', 'i', 'o', 'u']
# voc = input('Introdu litera: ')
# if voc in vocale:  # voc.lower() ca sa putem introduce si A si sa il ia
#     print(voc*10)
# else:
#     print('E alta lit')

# # 2. DICTIONARE - DICT { x: y}
# # nu putem avea duplicate, putem adauga si sterge
# # key: value
# masina = {'brand': 'dacia', 'model': 'spring', 'culoare': 'verde', 'cp': 1220}
# print(masina.get('brand'))
# print(masina['brand'])
# print(masina.keys())
# print(masina.values())
#
# # cum adaugam o cheie noua in dict
# masina['cutie'] = 'automata'
# print(masina)
#
# # suprascriere - update
# masina['cutie'] = 'manuala'
# print(masina)
#
# # cum stergem
# masina.pop('brand')
# print(masina)
#
# produse = {'masina de spalat': [23,45]}
# print(produse['masina de spalat'][0])
# assert 'pretul produsului' == produse['masina de spalat'][0] or produse['masina de spalat'][1]

# 3. SET {}
# ca lista dar are doar valori unice (nu se schimba), nu duplicate
# nu sunt ordonate, nu au index ptc nu-s ordonate (afiseaza random)
# se pot adauga si sterge elemente
culori = {'alb', 'rosu', 'verde'}
print(len(culori))

# cum adaugam - dar nu de mai multe ori un element
culori.add('alb') # nu
print(culori)

culori.add('albastru') # da
print(culori)

# cum stergem
culori.remove('alb')
print(culori)

# 4. TUPLE ()
# ca o lista, ordonate-au index
# nu se pot adauga si sterge valori
# accepta duplicate
vocals = ('a', 'e', 'i', 'a')
print(vocals[0]) # afiseaza dupa index
print(len(vocals)) # lungime
print(vocals.index('e')) # pe ce pozitie se afla 'e'
