from itertools import product
#granjero, lobo, cabra, col
I = 0
D = 1
estadoInicial = (I,I,I,I)

def seComen(estado):
    estadosMalos = set()
    estadosMalos.add((0,0,1,1))
    estadosMalos.add((0,1,1,0))
    estadosMalos.add((0,1,1,1))
    estadosMalos.add((1,0,0,0))
    estadosMalos.add((1,1,0,0))
    estadosMalos.add((1,0,0,1))
    return estado in estadosMalos

def seAcabo(estado):
    return estado == (D,D,D,D)

def DFS(estado):
    mapaEstados = set()
    for opciones in list(product([0,1],repeat=4)):
        mapaEstados.add(opciones)
    pila = list()
    pila.append(estado)
    camino = []
    while pila!=[]:
        #desapila
        s = pila.pop()
        camino.append(s)
        #verifica
        if not seAcabo(s):
            #explora las opciones
            mapaEstados = mapaEstados - {s}
            if not mapaEstados == set():
                for estados in list(mapaEstados):
                    if not seComen(estados):
                        pila.append(estados)
            else:
                break 
        else:
            pila = []


DFS(estadoInicial)