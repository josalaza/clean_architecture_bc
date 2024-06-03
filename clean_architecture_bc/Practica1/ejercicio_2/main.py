    
import figura

class Main():

    cuadrado =  figura.Cuadrado(lado = 5)
    print(f'El area del cuadrado es: {cuadrado.area()}')
    print(f'El perimetro del cuadrado es: {cuadrado.perimetro()}')

    rectangulo =  figura.Rectangulo(base = 5, altura = 6)
    print(f'El area del rectangulo es: {rectangulo.area()}')
    print(f'El perimetro del rectangulo es: {rectangulo.perimetro()}')

if __name__ == '__main__':
    Main()


