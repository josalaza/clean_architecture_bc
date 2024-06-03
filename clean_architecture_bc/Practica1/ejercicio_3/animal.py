
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def respirar(self):
        pass

    @abstractmethod    
    def comer(self):
        pass

    @abstractmethod
    def dormir(self):
        pass

class Carnivoro(Animal):

    @abstractmethod
    def cazar(self):
        pass

class Herbivoro(Animal):
    @abstractmethod
    def pastar(self):
        pass

class Perro(Carnivoro):
    def respirar(self):
        print('El perro respira')

    def comer(self):
        print('El perro come')

    def dormir(self):
        print('El perro duerme')
    
    def cazar(self):
        print('El perro caza')

class Vaca(Herbivoro):
    def respirar(self):
        print('La vaca respira')

    def comer(self):
        print('La vaca  come')

    def dormir(self):
        print('La vaca  duerme')
    
    def pastar(self):
        print('La vaca  pasta')        







