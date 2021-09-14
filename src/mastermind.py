from logic import *
import itertools
COLORES  = ['ROJO','AZUL','VERDE','AMARILLO']
POSICIONES = [(x,y) for x in range(4) for y in range(4)]
conocimiento = And()
#Los colores no se repiten en mas de una posicion
for col in COLORES:
    for i, j in POSICIONES:
        if (i!=j):
            conocimiento.add(
                Implication(
                    Symbol("{}{}".format(col,i)),
                    Not(Symbol("{}{}".format(col,j)))
                )
            )

#Una posicion hace referencia a un solo color
for i in range(4):
    for colorA in COLORES:
        for colorB in COLORES:
            if colorA != colorB:
                conocimiento.add(
                    Implication(
                    Symbol("{}{}".format(colorA,i)),
                    Not(Symbol("{}{}".format(colorB,i)))
                    )
                )

#todos los colores deben estar en alguna posicion
for color in COLORES:
    conocimiento.add(
        Or(
            Symbol("{}{}".format(color,0)),
            Symbol("{}{}".format(color,1)),
            Symbol("{}{}".format(color,2)),
            Symbol("{}{}".format(color,3))
        )
    )            

#elementos conocidos
#1. el primer arreglo de color con todos los elementos validos
ARREGLO = list()
ARREGLO.append(Symbol("ROJO0"))
ARREGLO.append(Symbol("AZUL1"))
ARREGLO.append(Symbol("VERDE2"))
ARREGLO.append(Symbol("AMARILLO3"))


conocimiento.add(
    Or(
        And(ARREGLO[0],ARREGLO[1],Not(ARREGLO[2]),Not(ARREGLO[3])),
        And(Not(ARREGLO[0]),Not(ARREGLO[1]),ARREGLO[2],ARREGLO[3]),
        And(ARREGLO[0],Not(ARREGLO[1]),Not(ARREGLO[2]),ARREGLO[3]),
        And(Not(ARREGLO[0]),ARREGLO[1],ARREGLO[2],Not(ARREGLO[3])),
        And(ARREGLO[0],Not(ARREGLO[1]),ARREGLO[2],Not(ARREGLO[3])),
        And(Not(ARREGLO[0]),ARREGLO[1],Not(ARREGLO[2]),ARREGLO[3])
    )
)
#2. el segundo arreglo de color con ningun elemento valido
conocimiento.add(
    And(
        Not(Symbol("AZUL0")),
        Not(Symbol("ROJO1")),
        Not(Symbol("VERDE2")),
        Not(Symbol("AMARILLO3"))
    )
)

#creamos las 16 posibles opciones
simbolos = list()
for t in range(4):
    for color in COLORES:
        simbolos.append(Symbol("{}{}".format(color,t)))

#Comprobamos
for s in simbolos:
    if model_check(conocimiento,s):
        print(s)
