class Elev:
    def __init__(self, nume, varsta, profil, medie):
        self.nume = nume
        self.varsta = varsta
        self.profil = profil
        self.medie = medie

    def descriere(self):
        print(f'Ma numesc {self.nume}, am {self.varsta} ani, studiez {self.profil} si am media {self.medie}')


    def la_multi_ani(self):
        self.varsta += 1



elev1 = Elev('Matei', 17, 'mate-info', 9.44)
elev2 = Elev('Cristi', 18, 'stiinte sociale', 9.50)
elev3 = Elev('Andreea', 18, 'stiinte sociale', 7.87)

elev1.descriere()
elev2.descriere()
elev3.descriere()

elev3.medie = 10
elev3.descriere()

elev1.la_multi_ani()
elev2.la_multi_ani()
elev3.la_multi_ani()
elev1.descriere()
elev2.descriere()
elev3.descriere()

elev3.nume = 'Elena'
elev3.descriere()
elev3 = Elev('Andreea', 18, 'stiinte sociale', 7.87)
elev3.descriere()

# toate modificarile facute se salveaza
# ultima modificare o tine minte


 