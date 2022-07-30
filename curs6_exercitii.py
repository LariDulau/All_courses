class Dreptunghi:
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def perimetru(self):
        return 2*self.latime + 2*self.lungime

    def aria(self):
        return self.latime * self.lungime

    def este_patrat(self):
        return self.lungime == self.latime

    def mareste_perimetru(self, n):
        return n * self.perimetru()

    def scade_perimetru(self, n):
        return self.perimetru()/n


dreptunghi1 = Dreptunghi(3,4)
print(f'perimetrul este {dreptunghi1.perimetru()}')
print(f'aria este {dreptunghi1.aria}')
print(f'dreptunghiul este patrat {dreptunghi1.este_patrat()}')
print(f'noul perimetru este de {dreptunghi1.mareste_perimetru(2)}')
print(f'noul noul perimetru este {dreptunghi1.scade_perimetru(2)}')

dreptunghi2 = Dreptunghi(5,5)
print(f'dreptunghiul este patrat {dreptunghi2.este_patrat()}')

