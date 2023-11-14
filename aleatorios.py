#En esta libreria se mostraran las funciones aleatorias :)
from random import choice,sample,randint

Personajes=["Dueño de la mansión", "Señor Sanchez", "Brayan Alfonso", "Andrea Julieta", "Señora Mary", "Carlos Barrios"]
Armas=["Cuchillo","Pistola","Correa","Teclado","Extintor","Llave de tubos","Flauta"]
Lugares=["Biblioteca","Baño","Cafeteria","Oficina de pago","Cancha de futbol","Salon de cine","Parqueadero","Laboratorio","Lago"]

seleccionados=[]

#Estas son las funciones para que el jugador pueda escoger sus sospechosos atravez del numero de carta, los cuales quedaran guardados en las variables 'selecionados'
def hoja(): 
    Personajes1=["#1.Dueño de la mansión", "#2.Señor Sanchez", "#3.Brayan Alfonso", "#4.Andrea Julieta", "#5.Señora Mary", "#6.Carlos Barrios"]
    Armas1=["#7.Cuchillo","#8.Pistola","#9.Correa","#10.Teclado","#11.Extintor","#12.Llave de tubos","#13.Flauta"]
    Lugares1=["#14.Biblioteca","#15.Baño","#16.Cafeteria","#17.Oficina de pago","#18.Cancha de futbol","#19.Salon de cine","#20.Parqueadero","#21.Laboratorio","#22.Lago"]
    print("\nEstas son las posibles sospechosos: ","#1.Dueño de la mansión", "#2.Señor Sanchez", "#3.Brayan Alfonso", "#4.Andrea Julieta", "#5.Señora Mary", "#6.Carlos Barrios")
    print("\nEstas son las posibles Armas: ","#7.Cuchillo","#8.Pistola","#9.Correa","#10.Teclado","#11.Extintor","#12.Llave de tubos","#13.Flauta")
    print("\nEstas son los posibles Lugares: ","#14.Biblioteca","#15.Baño","#16.Cafeteria","#17.Oficina de pago","#18.Cancha de futbol","#19.Salon de cine","#20.Parqueadero","#21.Laboratorio","#22.Lago")
    hj=int(input("Seleccione sus sospechas segun el numero de carta: "))
    if hj==1:
        a=Personajes1[0]
        seleccionados.append(a)                           
    elif hj==2:
        b=Personajes1[1]
        seleccionados.append(b)
    elif hj==3:
        c=Personajes1[2]
        seleccionados.append(c)
    elif hj==4:                                            
        d=Personajes1[3]
        seleccionados.append(d)
    elif hj==5:
        e=Personajes1[4]
        seleccionados.append(e)
    elif hj==6:
        f=Personajes1[5]
        seleccionados.append(f)
    elif hj==7:
        g=Armas1[0]
        seleccionados.append(g)
    elif hj==8:
        h=Armas1[1]
        seleccionados.append(h)
    elif hj==9:
        i=Armas1[2]
        seleccionados.append(i)
    elif hj==10:
        j=Armas1[3]
        seleccionados.append(j)
    elif hj==11:
        k=Armas1[4]
        seleccionados.append(k)
    elif hj==12:
        m=Armas1[5]
        seleccionados.append(m)
    elif hj==13:
        n=Armas1[6]
        seleccionados.append(n)
    elif hj==14:
        l=Lugares1[0]
        seleccionados.append(l)
    elif hj==15:
        o=Lugares1[1]
        seleccionados.append(o)
    elif hj==16:
        p=Lugares1[2]
        seleccionados.append(p)
    elif hj==17:
        q=Lugares1[3]
        seleccionados.append(q)
    elif hj==18:
        r=Lugares1[4]
        seleccionados.append(r)
    elif hj==19:
        s=Lugares1[5]
        seleccionados.append(s)
    elif hj==20:
        t=Lugares1[6]
        seleccionados.append(t)
    elif hj==21:
        u=Lugares1[7]
        seleccionados.append(u)
    elif hj==22:
        v=Lugares1[8]
        seleccionados.append(v)
    else:
        pass
           
seleccionadosDos=[]
def hojaDos(): 
    Personajes2=["#1.Dueño de la mansión", "#2.Señor Sanchez", "#3.Brayan Alfonso", "#4.Andrea Julieta", "#5.Señora Mary", "#6.Carlos Barrios"]
    Armas2=["#7.Cuchillo","#8.Pistola","#9.Correa","#10.Teclado","#11.Extintor","#12.Llave de tubos","#13.Flauta"]
    Lugares2=["#14.Biblioteca","#15.Baño","#16.Cafeteria","#17.Oficina de pago","#18.Cancha de futbol","#19.Salon de cine","#20.Parqueadero","#21.Laboratorio","#22.Lago"]
    print("\nEstas son las posibles sospechosos: ","#1.Dueño de la mansión", "#2.Señor Sanchez", "#3.Brayan Alfonso", "#4.Andrea Julieta", "#5.Señora Mary", "#6.Carlos Barrios")
    print("\nEstas son las posibles Armas: ","#7.Cuchillo","#8.Pistola","#9.Correa","#10.Teclado","#11.Extintor","#12.Llave de tubos","#13.Flauta")
    print("\nEstas son los posibles Lugares: ","#14.Biblioteca","#15.Baño","#16.Cafeteria","#17.Oficina de pago","#18.Cancha de futbol","#19.Salon de cine","#20.Parqueadero","#21.Laboratorio","#22.Lago")
    hj=int(input("Seleccione sus sospechas segun el numero de carta: "))
    if hj==1:
        a=Personajes2[0]
        seleccionadosDos.append(a)                           
    elif hj==2:
        b=Personajes2[1]
        seleccionadosDos.append(b)
    elif hj==3:
        c=Personajes2[2]
        seleccionadosDos.append(c)
    elif hj==4:                                            
        d=Personajes2[3]
        seleccionadosDos.append(d)
    elif hj==5:
        e=Personajes2[4]
        seleccionadosDos.append(e)
    elif hj==6:
        f=Personajes2[5]
        seleccionadosDos.append(f)
    elif hj==7:
        g=Armas2[0]
        seleccionadosDos.append(g)
    elif hj==8:
        h=Armas2[1]
        seleccionadosDos.append(h)
    elif hj==9:
        i=Armas2[2]
        seleccionadosDos.append(i)
    elif hj==10:
        j=Armas2[3]
        seleccionadosDos.append(j)
    elif hj==11:
        k=Armas2[4]
        seleccionadosDos.append(k)
    elif hj==12:
        m=Armas2[5]
        seleccionadosDos.append(m)
    elif hj==13:
        n=Armas2[6]
        seleccionadosDos.append(n)
    elif hj==14:
        l=Lugares2[0]
        seleccionadosDos.append(l)
    elif hj==15:
        o=Lugares2[1]
        seleccionadosDos.append(o)
    elif hj==16:
        p=Lugares2[2]
        seleccionadosDos.append(p)
    elif hj==17:
        q=Lugares2[3]
        seleccionadosDos.append(q)
    elif hj==18:
        r=Lugares2[4]
        seleccionadosDos.append(r)
    elif hj==19:
        s=Lugares2[5]
        seleccionadosDos.append(s)
    elif hj==20:
        t=Lugares2[6]
        seleccionadosDos.append(t)
    elif hj==21:
        u=Lugares2[7]
        seleccionadosDos.append(u)
    elif hj==22:
        v=Lugares2[8]
        seleccionadosDos.append(v)
    else:
        pass

seleccionadosPc=[]
def hojaPc(): 
    PersonajesPc=["#1.Dueño de la mansión", "#2.Señor Sanchez", "#3.Brayan Alfonso", "#4.Andrea Julieta", "#5.Señora Mary", "#6.Carlos Barrios"]
    ArmasPc=["#7.Cuchillo","#8.Pistola","#9.Correa","#10.Teclado","#11.Extintor","#12.Llave de tubos","#13.Flauta"]
    LugaresPc=["#14.Biblioteca","#15.Baño","#16.Cafeteria","#17.Oficina de pago","#18.Cancha de futbol","#19.Salon de cine","#20.Parqueadero","#21.Laboratorio","#22.Lago"]
    hj=randint(1,22)
    print(hj)
    if hj==1:
        a=PersonajesPc[0]
        seleccionadosPc.append(a)                           
    elif hj==2:
        b=PersonajesPc[1]
        seleccionadosPc.append(b)
    elif hj==3:
        c=PersonajesPc[2]
        seleccionadosPc.append(c)
    elif hj==4:                                            
        d=PersonajesPc[3]
        seleccionadosPc.append(d)
    elif hj==5:
        e=PersonajesPc[4]
        seleccionadosPc.append(e)
    elif hj==6:
        f=PersonajesPc[5]
        seleccionadosPc.append(f)
    elif hj==7:
        g=ArmasPc[0]
        seleccionadosPc.append(g)
    elif hj==8:
        h=ArmasPc[1]
        seleccionadosPc.append(h)
    elif hj==9:
        i=ArmasPc[2]
        seleccionadosPc.append(i)
    elif hj==10:
        j=ArmasPc[3]
        seleccionadosPc.append(j)
    elif hj==11:
        k=ArmasPc[4]
        seleccionadosPc.append(k)
    elif hj==12:
        m=ArmasPc[5]
        seleccionadosPc.append(m)
    elif hj==13:
        n=ArmasPc[6]
        seleccionadosPc.append(n)
    elif hj==14:
        l=LugaresPc[0]
        seleccionadosPc.append(l)
    elif hj==15:
        o=LugaresPc[1]
        seleccionadosPc.append(o)
    elif hj==16:
        p=LugaresPc[2]
        seleccionadosPc.append(p)
    elif hj==17:
        q=LugaresPc[3]
        seleccionadosPc.append(q)
    elif hj==18:
        r=LugaresPc[4]
        seleccionadosPc.append(r)
    elif hj==19:
        s=LugaresPc[5]
        seleccionadosPc.append(s)
    elif hj==20:
        t=LugaresPc[6]
        seleccionadosPc.append(t)
    elif hj==21:
        u=LugaresPc[7]
        seleccionadosPc.append(u)
    elif hj==22:
        v=LugaresPc[8]
        seleccionadosPc.append(v)
    else:
        pass



sobre=[]
#Estas son las funciones que permiten escoger de manera aleatoria las cartas para el sobre secreto, el jugador1, el jugador 2 y el Pc
def asignacion ():
    sobre.append(choice(Personajes))
    sobre.append(choice(Armas))
    sobre.append(choice(Lugares))
asignacion()

Personajes = [elemento for elemento in Personajes if elemento not in sobre]
Armas = [elemento for elemento in Armas if elemento not in sobre]
Lugares = [elemento for elemento in Lugares if elemento not in sobre]

sobrej1=[]

def asignacionj1():
    sobrej1.append(sample(Personajes, 2))
    sobrej1.append(sample(Armas, 2))
    sobrej1.append(sample(Lugares, 3))

asignacionj1()

Personajes = [elemento for elemento in Personajes if elemento not in sobrej1[0]]
Armas = [elemento for elemento in Armas if elemento not in sobrej1[1]]
Lugares = [elemento for elemento in Lugares if elemento not in sobrej1[2]]

sobrej2=[]

def asignacionj2():
    sobrej2.append(sample(Personajes, 2))
    sobrej2.append(sample(Armas, 2))
    sobrej2.append(sample(Lugares, 3))

asignacionj2()



