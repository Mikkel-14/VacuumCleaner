from ADT import Grafo, Node, Edge
import functools
from queue import PriorityQueue
from copy import deepcopy
def numCasillasErroneas(mat,obj):
    """
        Implementacion de la heuristica 1
    """
    matActual = mat[0] + mat[1] + mat[2]
    matObj = obj[0] + obj[1] + obj[2]
    casillasErroneas = list()
    for i in range(0,9):
        if matActual[i] == matObj[i]:
            casillasErroneas.append(0)
        else:
            casillasErroneas.append(1)
    return functools.reduce(lambda a,b: a+b,casillasErroneas)

def sumMovimientos(mat,obj):
    """
        Implementacion de la heuristica 2
    """
    indices = [(x,y) for x in range(0,3) for y in range(0,3)]
    #creemos dos copias de los objetos para no sufir modificaciones
    actual = deepcopy(mat)
    buscada = deepcopy(obj)
    movimientos = 0
    for i in range(0,3):
        #vamos a ir recorriendo cada espacio de la matriz actual
        #y vamos a buscar las coordenadas de su posicion en la matriz
        #buscada
        for j in range(0,3):
            posicionABuscar = actual[i][j]
            for posA,posB in indices:
                if buscada[posA][posB] == posicionABuscar:
                    movimientos += abs(posA-i) + abs(posB-j)
                    break 
    return movimientos


def verificarAcciones(posicion):
    """
        En base a la posicion, se puede determinar que subconjunto de las acciones se puede obtener
    """
    i,j = posicion
    acciones = set()
    if j>0:
        acciones.add('L')
    if j<2:
        acciones.add('R')
    if i>0:
        acciones.add('U')
    if i<2:
        acciones.add('D')
    return acciones

#impelentamos las operaciones
def arriba(mat0, pos):
    i,j = pos
    mat = mat0[:]
    #como quiero mover hacia arriba, quiero subir una fila
    valor = mat[i][j]
    mat[i][j]= mat[i-1][j]
    mat[i-1][j] = valor
    return mat, (i-1,j) 
def abajo(mat0,pos):
    i,j = pos
    mat = mat0[:]
    valor = mat[i][j]
    mat[i][j]= mat[i+1][j]
    mat[i+1][j] = valor
    return mat, (i+1,j)
def izquierta(mat0,pos):
    i,j = pos
    mat = mat0[:]
    #ahora me quiero mover de columna
    valor = mat[i][j]
    mat[i][j] = mat[i][j-1]
    mat[i][j-1] = valor
    return mat, (i,j-1)
def derecha(mat0,pos):
    i,j = pos
    mat = mat0[:]
     #ahora me quiero mover de columna
    valor = mat[i][j]
    mat[i][j] = mat[i][j+1]
    mat[i][j+1] = valor
    return mat, (i,j+1)

def operar(tipo,matriz,posicion):
    if tipo == 'L':
        nMat, nPos = izquierta(matriz,posicion)
    elif tipo == 'R':
        nMat, nPos = derecha(matriz,posicion)
    elif tipo == 'U':
        nMat, nPos = arriba(matriz,posicion)
    elif tipo == 'D':
        nMat, nPos = abajo(matriz,posicion)
    return nMat, nPos 

def problemSolverAgent(estadoInicial,posBlanco,estadoObjetivo, heuristica):
    """
    El agente recibe un estado inicial, debe poder tomar una secuencia de acciones,
    determinar los estados, calcular la busqueda en base a heuristicas y asi desarrollar
    el siguiente estado
    """
    #creo mi grafo con el nodo raiz en el estado inicial
    G = Grafo()
    nodoInicial = Node((estadoInicial,posBlanco))
    G.addNode(nodoInicial)
    #creo mi cola de prioridad
    pq = PriorityQueue()
    nodosEnCola = set()
    #evaluo mi heuristica sobre el nodo inicial
    hVal = heuristica(estadoInicial,estadoObjetivo)
    #encolo mi resultado
    pq.put((hVal,nodoInicial))
    nodosEnCola.add(nodoInicial)
    estadoPresente = deepcopy(estadoInicial)
    # A partir de aqui el agente debe hacer una busqueda best-first
    pasos = 0
    while (estadoPresente != estadoObjetivo) and (not pq.empty()):
        #sacamos el nodo ingresado
        h_u,u = pq.get()
        estadoPresente = deepcopy(u.getValue()[0])
        pos = u.getValue()[1]
        print("\nNodo visitado: {:}".format(estadoPresente))
        #Tienen que entrar los hijos del nodo que salio
        #El agente determina que acciones pueden efectuarse sobre el estado actual
        acciones = verificarAcciones(pos)
        print("Posibles acciones: {:}".format(acciones))
        #El agente efectua las acciones para cada posibilidad y obtiene un estadoSucesor
        for action in acciones:
            estadoSucesor, posSuc = operar(action,deepcopy(estadoPresente),pos)
            #añadimos el resultado al grafo
            nodoSucesor = Node((estadoSucesor,posSuc))
            G.addNode(nodoSucesor)
            G.addEdge(Edge(u,nodoSucesor))
        #ahora busquemos los hijos del nodo 
        hijos = list(map(lambda t: t[0],G.getChildren(u)))
        #print('Nodos Sucesores: {:}'.format(hijos))
        for v in hijos:
            if v not in nodosEnCola:
                hVal = heuristica(v.getValue()[0],estadoObjetivo)
                print("Estado sucesor {:}, con h = {:}".format(v.getValue()[0],hVal))
                pq.put((hVal,v))
                nodosEnCola.add(v)
        pasos +=1
    print("Problema resuelto con {:} pasos".format(pasos))
           

def main():
    inicial = [[7,2,4],[5,0,6],[8,3,1]]
    pos0 = (1,1)
    objetivo = [[0,1,2],[3,4,5],[6,7,8]]
    #inicial = [[2,8,1],[3,6,4],[7,0,5]]
    #pos0 = (2,1)
    #objetivo= [[1,2,3],[8,0,4],[7,6,5]]
    #para probar las distintas heuristicas descomentar la linea 160
    #problemSolverAgent(inicial,pos0,objetivo,numCasillasErroneas)
    problemSolverAgent(inicial,pos0,objetivo,sumMovimientos)
main()
