#En esta libreria se mostraran las funciones para los menus :)
from random import randint

from desarrollo import suposicion, acusacion,suposicionDos, suposicionPc,acusacionPc 

from apuntes import apuntes,apuntesDos,apuntesPc

from aleatorios import sobrej1,sobrej2



#Es una de las funciones principales que maneja la mayor parte de las opciones y los diferentes ciclos, nos permite romper un ciclo sin salir del anterior 
def jugar():
    print("\nElija 1 para jugar contra el pc, elija 2 para dos jugadores ó elija 3 para volver al menu principal: ")
    opt1=int(input("Ingrese la opcion deseada: "))
    while True:
        if opt1==2: 
            while True:
                print("\nEsta en el modo two players")
                turno=int(input("digite '1' para el turno del jugador 1, '2' para el turno del jugaror 2, '3' para volver al menu principal: "))
                if turno==1:
                    while True:
                        print("\nJugador '1' estas son sus cartas: ",sobrej1)
                        print("\nEstas son sus acciones por juego: ")
                        print("\nElija 1 para realizar una suposicion")
                        print("\nElija 2 para realizar una acusacion")
                        print("\nElija 3 para ingresar a su hoja de usuario")
                        print("\nElija 4 para rendirte y pasar el turno")
                        jug=int(input("Ingrese su opcion: "))
                        if jug==1:
                            suposicion()
                            pass
                        elif jug==2:
                            acusacion()
                            break
                        elif jug==3:
                            apuntes()
                            pass
                        elif jug==4:
                            break
                        else:
                            print("\nEscoja una opcion valida: ")
                elif turno==2:
                    while True:
                        print("\nJugador '2' estas son sus cartas: ",sobrej2)
                        print("\nEstas son sus acciones por juego: ")
                        print("\nElija 1 para realizar una suposicion")
                        print("\nElija 2 para realizar una acusacion")
                        print("\nElija 3 para ingresar a su hoja de usuario")
                        print("\nElija 4 para rendirte y pasar el turno")
                        jug=int(input("Ingrese su opcion: "))
                        if jug==1:
                            suposicionDos()
                            pass
                        elif jug==2:
                            acusacion()
                            break
                        elif jug==3:
                            apuntesDos()
                            pass
                        elif jug==4:
                            break
                        else:
                            print("Escoja una opcion valida: ")
                elif turno==3:
                    break
                else:
                    print("Elija una opcion valida")
            break
        elif opt1==1:
            while True:
                print("\nEsta en el modo off line, contra pc.")
                turno=int(input("digite '1' para el turno del jugador 1, '2' para el turno de la pc, '3' para volver al menu principal: "))
                if turno==1:
                    while True:
                        print("\nJugador '1' estas son sus cartas: ",sobrej1)
                        print("\nEstas son sus acciones por juego: ")
                        print("\nElija 1 para realizar una suposicion")
                        print("\nElija 2 para realizar una acusacion")
                        print("\nElija 3 para ingresar a su hoja de usuario")
                        print("\nElija 4 para rendirte y pasar el turno")
                        jug=int(input("Ingrese su opcion: "))
                        if jug==1:
                            suposicion()
                            pass
                        elif jug==2:
                            acusacion()
                            break
                        elif jug==3:
                            apuntes()
                            pass
                        elif jug==4:
                            break
                        else:
                            print("Escoja una opcion valida: ")
                elif turno==2:
                    while True:
                        print("\nPc, estas son sus cartas: ",sobrej2)
                        jug=randint(1,4)
                        print(jug)
                        if jug==1:
                            suposicionPc()
                            pass
                        elif jug==2:
                            acusacionPc()
                            break
                        elif jug==3:
                            apuntesPc()
                            pass
                        elif jug==4:
                            break
                        else:
                            print("Escoja una opcion valida: ")
                elif turno==3:
                    break
                else:
                    print("Elija una opcion valida")
            break
        elif opt1==3:
            break
        else:
            print("Escoja una opcion valida ")
            jugar()

                
          





