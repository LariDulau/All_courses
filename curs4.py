# '''pt intervale intre 5-20'''
# # x = int(input('Introdu un nr: '))
# # # range este si un interval. primul nr: de unde incepe inclusiv, ultimul nr: pana unde, fara ultimul nr
# # if x in range(5, 21):
# #     print(x)
# #
# # # toate metodele care incerc cu 'is' - returneaza True/False
# # text = input('Introdu un text: ')
# # # dupa assert trebuie sa punem ceva ce e adevarat sau fals
# # # doar daca e adevarat nu iti da eroare si trece la linia urmatoare
# # # assert text.isnumeric()
# # print(text)
# # print('*'*len(text))
# #
# # # nota = float(input('Introdu o nota: '))
# # # if nota >= 9 and nota <= 10:
# # #     print('A')
# # # elif nota >= 8 and nota < 9:
# # #     print('B')
# # # else:
# # #     print('d')
# #
# # # text1, text2, text3 = input('Datimi 3 texte: ').split()
# # # print(text1)
# # # print(text2)
# # # print(text3)
# #
# # # tema jucatori tema3
# # # cate schimbari s-au produs in joc pana acum
# # # putem sa citim si de la tastatura doar sa fie mai mic decat 3 sa putem face schimbari
# # jucatori = ['j1', 'j2', 'j3', 'j4', 'j5']
# # SCHIMBARI_MAXIME = 3
# # SCHIMBARI_EFECTUATE = 2
# # # un nume de jucator de scos, pe care vrem sa-l stergem
# # jucator_out = 'j2'
# # # un alt nume nu din lista
# # jucator_in = 'j6'
# #
# # if jucator_out in jucatori and SCHIMBARI_EFECTUATE < SCHIMBARI_MAXIME:
# #     print('efectual schimbarea')
# #     jucatori.remove(jucator_out)
# #     print(jucatori)
# #     jucatori.insert(1, jucator_in)
# #     print('noua echipa', jucatori)
# #     print(f'A iesit {jucator_out}, a intrat {jucator_in}, mai aveti {SCHIMBARI_MAXIME-SCHIMBARI_EFECTUATE-1} schimbari')
# # else:
# #     print('jucatorul nu e in teren/au ajuns la nr maxim de schimbari')
#
# '''
# while, while else, for'''

# while (repetitiv) = executa atata timp cat o conditie e adevarata
# se poate adauga optional la final else: se executa la final dupa ciclu

# printati numerele pana la 5
# de unde incep
# Atentie! conditia sa fie si falsa lumd, daca nu, intra in ciclu infinit
# i = 1 # variabila index
# suma = 0 # variabila suma-ptc vrem sa facem suma primelor 5
# while i <= 5:
#     print(i)
#     suma = suma + i # sau suma +=1 - asta se pune la inceput
#     i = i+1 # sau i += 1 - asta se pune la final (crestere nr pt indexare-final)
# print(suma)
#
# # pin_incercari = 0
# # while (pin != pin_corect) and pin_incercari<=3:
# #     print('mai ai atatea incercari, mai introdu odata')
# #     pin_incercari += 1 # incremenari la final
#
# # WHILE ELSE
# # else se executa o singura data la final daca conditia e true sau false, e optional
# # initializarea, conditia cum o facem, decrementarea, incrementarea ( sa nu mearga la infinit )
# # j = 10 # de unde incepem
# # produs = 1
# # while j >= 0:
# #     print(i)
# #     produs *= i
# #     j = j-2 # incrementare sau decrementare
# # else:
# #     print('s-a terminat')
# # print(produs)
#
# # FOR
# # executa o bucata de cod pt fiecare element dintr-un interval, lista
# # printam nr de la 0-10
# # sum = 0
# # prod = 1
# # for i in range (20, 0, -5):
# #     print(i)
# #     sum += i
# #     prod *= i
# # else:
# #     print('e gata codu') # se printeaza o singura data la final-optional
# # print(sum)
# # print(prod)
#
# # o lista de culori in care inlocuim alb cu roz
culori = ['portocaliu', 'alb', 'rosu', 'albastru', 'alb', 'negru']
print(culori)
for culoare in range (0, len(culori)):
    print(f'culoarea este {culori[culoare]}')
    if (culori[culoare]=='alb'):
        # daca da, suprascriu cu culoarea roz
        culori[culoare] = 'roz'
print(culori)
# #
# FOR EACH
# nu avem nevoie de pozitie si range, ia efectiv fiecare element din lista
numar = 0
for culoare in culori: # pt fiecare culoare din lista culori executa urm pasi
    print(f'culoarea este {culoare}')
    if culoare[0] == 'p':
        numar += 1
print(numar)
#
#
# note = [2,3,4,5,10]
# # cati elevi au peste nota 10?
# numar_elevi = 0
# for nota in note:
#     if nota >= 5:
#         numar_elevi += 1
# print(f'numarul elevilor cu nota de trecere este {numar_elevi}')



# DE CE NU IA DIN 2 IN 2?
# i = 1
# # este unul din numerele 1,2,3,4,5,6,7,8,9?
# while i in range(1,10, 2):
#     print(i)
#     i += 1 # daca nu punem asta intra in ciclu inifinit, for adauga singur fara conditie