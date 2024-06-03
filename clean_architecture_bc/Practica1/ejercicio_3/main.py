import animal

class Main():

    perro = animal.Perro()
    vaca = animal.Vaca()

    perro.respirar() 
    perro.comer()    
    perro.dormir() 
    perro.cazar()    

    vaca.respirar()  
    vaca.comer()  
    vaca.dormir()   
    vaca.pastar()    

if __name__ == '__main__':
    Main()
