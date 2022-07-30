#
# # iteratie = valoarea pe care o are i-u
#
# # while, for = structuri repetitive, acelasi cod se repeta de mai multe ori = avem mai multe iteratii (repetitii de cod)
#
# # # executa cat timp conditia de dupa cuvantul while este adevarata
# # numar = int(input('Introdu un numar: '))
# # # cat timp conditia de mai jos e adevarata tot citim nr de la tastatura
# # while numar != 10:
# #     print(f'Numarul tau are o diferenta de {numar-10} de numarul 10')
# #     numar = int(input('Introdu un numar: '))
# # print('Ai introdus valoarea corecta')
#
# # la while tot timpu trebuie sa declaram o valoare pe care ulterior sa o incrementam sau sa facem ceva cu ea
#
# # produsul tuturor nr pana la 10
# i = 1 # valoare de inceput
# produs = 1
# # trebuie sa ne asiguram ca o sa se opreasca while-ul, adica conditia o sa fie falsa lumd
# while i <= 10:
#     # produs = produs * i
#     produs *= i
#     i += 2
# print(produs)
#
# # la for nu avem pas special pt declarare variabila de incrementare (i=) nici pt schimbarea valorii (i+=1 sau 2)
# produs2 = 1
# for i in range(1, 10, 2):
#     produs2 *= i
# print(produs2)
#
# # cand aveti nevoie de pozitia elementelor dintr-o lista, parcurgeti lista cu for i in range
#
# masini = ['cielo', 'dacia', 'audi']
# # for each (nu se face in functie de nr, ia fiecare element pe rand), nu avem nevoie de pozitie
# for masina in masini:
#     print(masina)
#
# # continue - sare peste o iteratie (repetare de cod)
# produs2 = 1
# for i in range(1, 10, 2):
#     if i% 7 == 0:
#         continue
#     produs2 *= i
# print(produs2)
#
#
# # break - opreste for, while - opreste iteratiile
# # cand produsul e 500 sa se opreasca
# produs2 = 1
# for i in range(1, 12, 2):
#     if i% 7 == 0:
#         continue
#     if produs2 >= 500: # primu produs peste 500 = 1485
#         break
#     produs2 *= i
# print(produs2)
#
# FUNCTII/ METODE SIMPLE

print(max(4, 6, 7, 8, 9, 22))
lista = [2,3,56,7,8,89]
max =lista[0]
for element in lista:
    if element > max:
        max = element
print (max)

# def - pt definire, numele metodei:
def maxim(lista):
    max = lista[0]
    for element in lista:
        if element > max:
            max = element
    print(max)

maxim(lista)
# maxim() missing 1 required positional argument: 'lista' - ai uitat sa dai parametru


# # FUNCTII/ METODE CU PARAMETRII
#
# def perimetru_dreptunghiului(lungime, latime):
#     print(f'Perimetrul dreptunghiului este {lungime * latime}')
#
# # perimetru_dreptunghiului(4,5)
# # perimetru_dreptunghiului(67,56)
# #
# # def descriere_persoana(nume, varsta, oras= 'Jimbolia'):
# #     print(f'Ma numesc {nume}, am {varsta} ani, sunt din {oras}')
# #
# # descriere_persoana('Larisa', 27, 'Oradea')
# # descriere_persoana('Ruben', 28)
# # ce e intre () = parametrii, putem avea oricati de orice tip, neaparat de resp ordinea
# # putem sa declaram parametrii ca sa nu avem eroare
#
#
#
# # FUNCTII/ METODE CU RETURN
# # metode care returneaza ceva, un rezultat
# # metode pe care le intrebam ceva
# # text = 'ana'
# # print(text.islower())
#
# def is_par(numar):
#     if numar % 2 == 0:
#         return 'nr e par'
#     else:
#         return 'nr e impar'
# print(is_par(10))
#
# # def primetru_dreptunghiului(lungime, latime):
# #     return lungime*latime
# # print(perimetru_dreptunghiului(5,6))
#
# # !!!!!! sesiune rec la perimetru, am pierdut siru !!!!!!!!

# Exercitii
# avem o lista de nr, facem media lor, parametru lista, return
numere = [2, 3, 4, 5, 67, 89, 90]
# def medie_nr(numere): # declarare
def media(numere):
    i = 0
    media = 0
    while i < len(numere):
        print(numere[i])
        media += numere[i]
        i += 1
    media= media/len(numere)
    return media


print(media(numere))
print(media([2, 3, 4, 55, 78, 11, 29]))
print(media([2, 3, 4, 55, 78, 11, 29]) + media(numere))

def media2(numere):
    media = 0
    for numar in numere:
        media += numar
    media = media / len(numere)
    return media
print(media2(numere))
print(media2([2, 3, 4, 55, 78, 11, 29]))
print(media2([2, 3, 4, 55, 78, 11, 29]) + media2(numere))
