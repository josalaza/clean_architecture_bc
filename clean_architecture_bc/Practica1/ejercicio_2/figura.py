from dataclasses import dataclass

@dataclass
class Figura:

    def area(self):
        pass
    
    def perimetro(self):
        pass

@dataclass
class Cuadrado(Figura):

    lado : int

    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return self.lado * 4



@dataclass
class Rectangulo(Figura):

    base : int
    altura : int

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return (self.base + self.altura) * 2 









