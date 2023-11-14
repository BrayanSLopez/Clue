#Dentro de esta libreria se asignan las funciones de apuntes para cada jugador
from random import randint

from aleatorios import hoja,seleccionados,hojaDos,seleccionadosDos, hojaPc, seleccionadosPc

#Funciones las cuales arrogan las opciones para ingresar a la hoja de usuario
def apuntes ():
   while True:
        print("\nEsta es su hoja de usuario.")
        apu=int(input("Elija 1 para anotar un sospechoso, elija 2 para visualizar sus apuntes o 3 para seguir jugando: "))
        if apu==1:
             hoja()
        elif apu==2:
            print("\n",seleccionados)
        elif apu==3:
            break
        else:
            print("Elija una opcion valida: ")

def apuntesDos ():
   while True:
        print("\nEsta es su hoja de usuario.")
        apu=int(input("Elija 1 para anotar un sospechoso, elija 2 para visualizar sus apuntes o 3 para seguir jugando: "))
        if apu==1:
             hojaDos()
        elif apu==2:
            print("\n",seleccionadosDos)
        elif apu==3:
            break
        else:
            print("Elija una opcion valida: ")   


def apuntesPc ():
   while True:
        apu=randint(1,3)
        print(apu)
        if apu==1:
             hojaPc()
        elif apu==2:
            print(seleccionadosPc)
            pass
        elif apu==3:
            break
        else:
            print("Elija una opcion valida: ")           


            

