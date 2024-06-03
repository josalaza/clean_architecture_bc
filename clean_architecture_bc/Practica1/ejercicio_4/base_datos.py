from abc import ABC, abstractmethod

class BaseDatos(ABC):
    @abstractmethod
    def guardar(self, datos):
        pass

    @abstractmethod
    def leer(self):
        pass