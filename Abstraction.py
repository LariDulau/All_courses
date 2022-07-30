# abstraction
# ascunde unele chestii de user

# importam ABC ca sa ne folosim de abstractizare in python
from abc import ABC, abstractmethod


class Car(ABC):
    # @ = decoratori si schimba functiile astea, metoda noastra e abstracta, e o metoda fara corp
    @abstractmethod
    def accelerate(self):
        raise NotImplementedError

    @classmethod
    def stop(self): # poate sa contina si metode normale ( cu logica interna )
        print('STOP!')


class Ferrari(Car):
    def accelerate(self):
        print('I am accelerating from 0 to 100 in 5 seconds')

    def descriere(self):
        print('Ferrari')


masina = Ferrari()
masina.descriere()
masina.accelerate()

# encapsulation
# __nume (ascunde)