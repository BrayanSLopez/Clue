#Hecho por Dayana Escobar y Brayan Lopez 

#Rama principal
from menus import jugar

print("""
    En un misterioso asesinato en la mansion Sanchez, el inspector de policia
    necesita tu ayuda para resolver el caso. Luego de estar en una reunion con
    diferentes personajes de la farandula San Bonaventuriana, en la mansion aparecio
    asesinado el amo de llaves. En la reunion estaban presentes 6 invitad@s, que incluyen 
    al dueño de la mansion, el señor Sanchez, Brayan Alfonso, Andrea Julieta, Señora Mary 
    y Carlos Barrios. Dentro de los cuales se encuentra el asesino del amo de llaves.
    ¿Podras resolver el misterio?🤔""")
#Esta funcion sera la principal y servira de giia para la introduccion y guia del juego
def clue():
    while True:
        ab=(input("\nBienvenido a clue, ingrese cualquier letra o valor para iniciar el juego o 'a' para acabar el juego: "))
        if ab=="a":
            print("Gracias por jugar 👍")
            break
        else:
            print("\nLos presuntos sospechosos son: Dueño de la mansión, Señor Sanches, Brayan Alfonso, Andrea Julieta, Señora Mary, Carlos Barrios")
            print("\nLas presuntas armas para el asesinato son: Cuchillo, Pistola, Correa, Teclado, Extintor, Llave de tubos, Flauta")
            print("\nLos lugares para el asesinato podrian ser: Biblioteca, Baño, Cafeteria, Oficina de pago, Cancha de futbol, Salon de cine, Parqueadero, Laboratorio, Lago")
            jugar()
clue()
#El ejecutador de la funcion 












