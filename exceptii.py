# # in try punem codul care s-ar putea sa pice, codul periculos
# try:
#     lista = [1,2,3,4]
#     print(lista[4])
# except IndexError as e:
#     print(f'Lungimea listei tale nu e corecta. Incerci sa printezi o pozitie inexistenta')
#
# try:
#     print(mama)
# except NameError as e:
#     mama = 'ioana'
#     print('Variabila nu a fost definita si am definit-o')
# print(mama)
#

i = 4 # variabila index
suma = 0 # variabila suma-ptc vrem sa facem suma primelor 5
while i <= 5:
    print(i)
    suma = suma + i # sau suma +=1 - asta se pune la inceput
    i = i+1 # sau i += 1 - asta se pune la final (crestere nr pt indexare-final)
print(suma)

# j = 10 # de unde incepem
# produs = 1
# while j >= 8:
#     print(j)
#     produs = produs * j
#     j = j-2 # incrementare sau decrementare

