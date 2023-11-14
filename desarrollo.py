#Desarrollo de acciones que tiene el jugador
from random import randint,choice

from aleatorios import sobre, sobrej2,sobrej1

from apuntes import apuntes,apuntesDos

#Funcion para que el jugador realice una suposicion y se compare con las cartas del otro jugador
def suposicion():
    supoPersonaje=input("\ningrese su suposicion de personaje: ")
    supoArma=input("\ningrese su suposicion de Arma: ")
    supoLugar=input("\ningrese su suposicion de Lugar: ")
    supo=[supoPersonaje,supoArma,supoLugar]
    def comparativa():
        rs=choice(supo)
        for i in sobrej2:
            for f in i:
                if f==rs:
                    print("\nAcertaste en: ", f)
                    break
                else:
                    pass    
    comparativa()
    print("\nSi no aparece 'Acertaste en: ', es por que no acertaste en ninguno :,)")
    apuntes()

def suposicionDos():
    supoPersonaje=input("ingrese su suposicion de personaje: ")
    supoArma=input("ingrese su suposicion de Arma: ")
    supoLugar=input("ingrese su suposicion de Lugar: ")
    supo=[supoPersonaje,supoArma,supoLugar]
    def comparativaDos():
        rs=choice(supo)
        for i in sobrej1:
            for f in i:
                if f==rs:
                    print("Acertaste en: ", f)
                    break
                else:
                    pass   
    comparativaDos()
    print("\nSi no aparece 'Acertaste en: ', es por que no acertaste en ninguno :,)")
    apuntesDos()

def suposicionPc():

    Personajes=["Dueño de la mansión", "Señor Sanchez", "Brayan Alfonso", "Andrea Julieta", "Señora Mary", "Carlos Barrios"]
    Armas=["Cuchillo","Pistola","#Correa","Teclado","Extintor","Llave de tubos","Flauta"]
    Lugares=["Biblioteca","Baño","Cafeteria","Oficina de pago","Cancha de futbol","Salon de cine","Parqueadero","Laboratorio","Lago"]

    supoPersonaje=choice(Personajes)
    supoArma=choice(Armas)
    supoLugar=choice(Lugares)
    supo=[supoPersonaje,supoArma,supoLugar]
    print(supo)
    def comparativaPc():
        rs=choice(supo)
        for i in sobrej1:
            for f in i:
                if f==rs:
                    print("\nAcertaste en: ", f)
                    break
                else:
                    pass   
    comparativaPc()
    

#Funcion Para hacer una acusacion directa para ganar, el jugador debe acertar en las 3 cartas para ganar o de lo contrario sera un Game over

def acusacion():
    acuPersonaje=input("ingrese su acusacion de personaje: ")
    acuArma=input("ingrese su acusacion de Arma: ")
    acuLugar=input("ingrese su acusacion de Lugar: ")
    acusa=[acuPersonaje,acuArma,acuLugar]
    if acusa[0]==sobre[0] and acusa[1]==sobre[1] and acusa[2]==sobre[2]:
        print("\nFelicidades ganaste :)")

    else:
        print("\nGame over, las cartas del sobre era:",sobre)


def acusacionPc():
    Personajes=["Dueño de la mansión", "Señor Sanchez", "Brayan Alfonso", "Andrea Julieta", "Señora Mary", "Carlos Barrios"]
    Armas=["Cuchillo","Pistola","#Correa","Teclado","Extintor","Llave de tubos","Flauta"]
    Lugares=["Biblioteca","Baño","Cafeteria","Oficina de pago","Cancha de futbol","Salon de cine","Parqueadero","Laboratorio","Lago"]

    acuPersonaje=choice(Personajes)
    acuArma=choice(Armas)
    acuLugar=choice(Lugares)
    acusa=[acuPersonaje,acuArma,acuLugar]
    print(acusa)
    if acusa[0]==sobre[0] and acusa[1]==sobre[1] and acusa[2]==sobre[2]:
        print("\nFelicidades ganaste :)")

    else:
        print("\nGame over, las cartas del sobre era:",sobre)



