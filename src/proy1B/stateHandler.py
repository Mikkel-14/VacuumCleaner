"""
Tic Tac Toe Player
"""
from ADT import Edge, Grafo, Node
from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def actions(state):
    """
    Returns the set of legal moves in a state
    vamos a usar el estado como una lista, donde 
    EMPTY implica espacio vacio y 'x' o 'o' para los
    espacios ocupados
    """
    acciones = list()
    for i in range(3):
        for j in range(3):
            if state[i][j] == EMPTY:
                acciones.append((i,j))
    return acciones

def player(state):
    """
    Returns player who has next turn on a board.
    """
    #vamos a contar la cantidad de x y la cantidad de o
    Xs = 0
    Os = 0
    for values in state:
        for val in values:
            if val == X:
                Xs += 1
            elif val == O:
                Os += 1
    if Xs > Os:
        return O
    elif Xs == Os:
        return X
    else:
        return X

def result(state, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action 
    state[i][j] = player(state)
    return state 

def winner(state):
    """
    Returns the winner of the game, if there is one.
    """
    ganador = None
    for symbol in [X, O]:
        expresionGanadora = [symbol,symbol,symbol]
        #comprobamos las filas
        for fila in state:
            if fila == expresionGanadora:
                ganador = symbol
                return ganador
        #comprobamos las columnas
        for i in range(0,3):
            columna = list()
            for j in range(0,3):
                columna.append(state[j][i])
            if columna == expresionGanadora:
                ganador = symbol
                return ganador
        #diagonales
        diagonalA = list()
        diagonalB = list()
        for i in range(0,3):
            diagonalA.append(state[i][i])
            diagonalB.append(state[i][2-i])
        if diagonalA == expresionGanadora or diagonalB ==expresionGanadora:
            ganador = symbol
            return ganador
    return ganador

def terminal(state):
    """
    Returns True if game is over, False otherwise.
    """
    resultado = False
    if winner(state) == None:
        #verifico que todos los espacios esten llenos
        for i in range(3):
            for j in range(3):
                if state[i][j] == EMPTY:
                    return resultado
        return True 
    else:
        resultado = True 
    return resultado

def utility(state):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    value = 0
    ganador = winner(state)
    if ganador == X: 
        value = 1
    elif ganador == O:
        value = -1
    return value
    
def minimax(state):
    """
    Returns the optimal action for the current player on the board.
    """
    g = Grafo()
    if g.isEmpty():
        #si el grafo esta vacio lo construimos
        nodo = Node(state)
        g.addNode(nodo)
        pila = list()
        pila.append(nodo)
        while  pila != []:
            #exploramos el nodo
            n = pila.pop()
            if not terminal(n.getValue()):
                acciones = actions(n.getValue())
                for action in acciones:
                    estadoResultado = result(deepcopy(n.getValue()),action)
                    nodoResultante = Node(estadoResultado)
                    arista = Edge(n, nodoResultante)
                    g.addNode(nodoResultante)
                    g.addEdge(arista)
                    pila.insert(0,nodoResultante)
            else:
                n.setUtil(utility(n.getValue()))
                pilaReversa = list()
                pilaReversa.append(n)
                while pilaReversa != []:
                    hijo = pilaReversa.pop()
                    padres = hijo.getParent()
                    if padres != []:
                        for nodoPadre in padres:
                            next= player(nodoPadre.getValue())
                            utilidad = hijo.getUtil()
                            if next == X:
                                #implica que el padre jugo O, y hay que maximizar
                                if nodoPadre.hasUtil():
                                    utilidadPadre = nodoPadre.getUtil()
                                    if utilidad > utilidadPadre:
                                        nodoPadre.setUtil(utilidad)
                                else:
                                    nodoPadre.setUtil(utilidad)
                            else:
                                #significa que el padre jugo X, y hay que minimizar
                                if nodoPadre.hasUtil():
                                    utilidadPadre = nodoPadre.getUtil()
                                    if utilidad < utilidadPadre:
                                        nodoPadre.setUtil(utilidad)
                                else:
                                    nodoPadre.setUtil(utilidad)        
                            pilaReversa.insert(0,nodoPadre)  
    nodoPresente = g.getNode(state)
    valor = nodoPresente.getUtil()
    act = actions(nodoPresente.getValue())
    for accion in act:
        resultado = result(deepcopy(nodoPresente.getValue()),accion)
        nodoResultante = g.getNode(resultado)
        if nodoResultante.getUtil() == valor:
            return accion
    
        
    
    
    

#inicial = [[EMPTY,EMPTY,EMPTY],[EMPTY,X,EMPTY],[EMPTY,EMPTY,EMPTY]]
#inicial = [[O, None, None], [None, X, None], [None, None, None]]
#print(minimax(inicial))
#inicio = Grafo().getNode(inicial)
#print(inicio.getUtil())
#for hijo in Grafo().getChildren(inicio):
#    print(str(hijo.getValue()) + ' '+str(hijo.getUtil()))
#for hijo in Grafo().getChildren(Grafo().getNode([['O', 'X', None], [None, 'X', None], [None, None, None]])):
#    print(str(hijo.getValue()) + ' '+str(hijo.getUtil()))