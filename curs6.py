class Caine:
    # rasa = 'labrador'
    # varsta = 2
    # este_agresiv = False
    # are_pedigree = True
    # culoare = 'negru'
    nr_picioare = 4

    # CONSTRUCTOR: def init - required
    def __init__(self, rasa, varsta, este_agresiv, are_pedigree, culoare):
        self.rasa = rasa
        self.varsta = varsta
        self.este_agresiv = este_agresiv
        self.are_pedigree = are_pedigree
        self.culoare = culoare



    def descriere(self):
        print(f'Am un caine misto {self.rasa}, are {self.varsta} ani, este agresiv {self.este_agresiv}')

    def ani_omenesti(self):
        print(f'Cainele are {self.varsta * 7} ani omenesti')

    def este_agresive(self):
        return self.este_agresiv


zoro = Caine('labrador', 3, True, True, 'alb')

# print(zoro.rasa)
# print(zoro.varsta)
#
# zoro.descriere()
# zoro.ani_omenesti()
#
# print(zoro.este_agresive())
#
# assert zoro.are_pedigree
# assert zoro.este_agresiv -- false (error)

# if zoro.este_agresive(): --- NU merge bine
#     print('du-l la dresaj')
# else:
#     print('este o alegere buna pt copii')
#
# spark = Caine('buldog', 10, False, False, 'gri')
# azorel = Caine('dog german', 3, True, True, 'maro')
# luna = Caine('bichon', 4, True, True, 'alb')
#
# spark.descriere()
# spark.ani_omenesti()
