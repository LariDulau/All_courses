# pollymorfism - cand exista 2 metode cu acelasi nume, dar poate sa aiba forme diferite

# built polymorfic function
def add(a, b, c):
    return a + b + c

def add2(d, e, f=10):
    return d + e + f


print(add(3, 4, 5))
print(add2(3, 4))
print(add2(1, 2, 3))  # daca dam noi le ia asa, daca nu punem aici ia de sus valoarea din def
sum = sum([4, 5, 10, 10, 1])
print(sum)

def descriere(nume, prenume):
    print(f'Numele meu e {nume}, prenumele e {prenume}')

# descriere('ion') # nu merge doar cu un parametru

class Bird:
    def describe (self):
        print('I am a bird')

    def fly(self):
        print('Flu Flu Flu! I am flying')

class Parrot (Bird):
    def talk (self):
        print('I can talk')

    def fly(self): # suprascrie def fly de la bird
        print('I can not fly. I am sick')

    def fly(self):
        print(f'I can t fly. I am sick')

coco = Parrot()
coco.describe()
coco.fly()
coco.talk()

