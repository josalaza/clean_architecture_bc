import calculadora

class Main():

    calculadora = calculadora.Calculadora()
    print(f'La suma es: {calculadora.sumar(8, 21)}')
    print(f'La resta es: {calculadora.restar(9,2)}')
    print(f'La multiplicacion es: {calculadora.multiplicar(12,12)}')
    print(f'La division es: {calculadora.dividir(6,2)}')


if __name__ == '__main__':
    Main()