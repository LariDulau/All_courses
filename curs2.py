'''
operatori de atribuire, aritmetici, de comparare, logici.
if
'''

# operatori de atribuire += -= *= /=
x = 10
x = x + 5
print(x)
# e acelasi lucru doar ca scris mai frumos
x += 5 # + - * /
print(x)
x *= 3
print(x)
x /= 2
print(x)

# operatori de comparare
# operatori de egalitate
assert 5 == 5
assert 'Maria' == 'Maria' # e egal
assert 'Maria' != 'maria' # Nu e egal !=
# > < >= <=

# operatori logici
# operatorul and ( ambele conditii trebuie sa fie adev)
assert x > 25 and x < 31
# assert parola are lungimea > 10 and o litera mare and un caracter special...

# operatorul or ( doar una din conditii sa fie adevarate )
assert x > 25 or x < 1

# not ( face din fals in true, sau din true in fals )
print( not(5 == 5)) # 5 != 5 (same)


# if - slow control ( controlam unde merge codul respectiv )
# daca o conditie e adevarata atunci se executa un cod
# daca nu e adevarata conditia se executa alt cod
# daca pin-ul e corect se afiseaza ecranul cu optiunile pe care le avem
# daca pin-ul e incorect se afiseaza un mesaj de eroare : ai introdus pin-ul gresit

'''
bagi username
bagi parola
click ok
daca parola e corecta -> afiseara bine ai venit
daca parola e gresita -> parola e gresita
'''

# doar if, doar cod de executaat pt cand conditia e adevarata
numar = int(input('Introdu numar'))
if numar < 20:
    print('numarul este bun')

# if, else - se executa cod si daca conditia noastra este falsa
parola = input('introduceti parola')
if parola == 'Ana':
    print('Parola corecta')
else :
    print('Parola gresita')

nota = float(input('Nota este: '))
if nota > 4.5:
    print('Ai trecut examenul')
else:
    print('Nu ai promovat examenul')

# calificativ -> A - f bine, B - bine, C - satisfacator, S - suficient
calificativ = input('Introdu calificativul: ')
if calificativ == 'A':
    print('F bine')
elif calificativ == 'B':
    print('Bine')
elif calificativ == 'C':
    print('Satisfacator')
else:
    print('Ai luat suficient')





