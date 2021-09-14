from itertools import product
class Node:
    def __init__(self, value) -> None:
        """
        Dentro del nodo se puede almacenar cualquier tipo de dato
        """
        self.value = value
    def getValue(self):
        return self.value
    def __str__(self) -> str:
        return self.value

class Edge:
    def __init__(self, nodoA, nodoB, peso=1) -> None:
        """
        Para la implementacion de una arista, tomamos en cuenta la nocion de un grafo simple: un subconjunto de nodos.
        Adicionalmente, se cuenta con un parametro opcional de peso en el caso de que se necesite un grafo con pesos
        """
        self.nodes = (nodoA,nodoB)
        self.peso = peso
    
    def getIncidentNodes(self):
        return self.nodes
    
    def getPeso(self):
        return self.peso

    def __str__(self) -> str:
        u,v = self.nodes
        return "{:} -- {:}".format(u.getValue(),v.getValue())
        
class Grafo:
    """ Esta clase implementa el comportamiento de un grafo, usando nodos (V)
    y edges (E). Para el problema de las ciudades no requerimos de un grafo dirigido,
    pues se puede ir y volver de una ciudad a otra. La implementacion de este tipo de dato abstracto
    se hace mediante un mapa de adyacencia que guardara los nodos adyacentes del grafo.
    """
    def __init__(self) -> None:
        self.adjacencyMap = dict()
    
    def addNode(self, nodo):
        if nodo not in self.adjacencyMap:
            self.adjacencyMap[nodo] = list()
        else:
            print("El nodo ya se encuentra en el grafo\n")
    
    def addEdge(self,edge):
        u,v = edge.getIncidentNodes()
        peso = edge.getPeso()
        if (u in self.adjacencyMap) and (v in self.adjacencyMap):
            self.adjacencyMap[u].append((v,peso))
            self.adjacencyMap[v].append((u,peso))

    def getChildren(self,node):
        hijos = list()
        if node in self.adjacencyMap:
            hijos = self.adjacencyMap[node]
        return hijos

    def hasNode(self, node):
        return node in self.adjacencyMap
    
    def getNode(self, value):
        for key in self.adjacencyMap:
            if key.getValue() == value:
                return key

def DFS(grafo, nodoInicial, nodoFinal):
    nodosApilados = set()
    pila = list()
    #empezamos desde el nodo inicial
    pila.append(nodoInicial)
    nodosApilados.add(nodoInicial)
    trazadoTrayectoria = 'Trayectoria DFS: '
    while (len(pila)!=0):
        #sacamos de la pila al nodo
        u = pila.pop()
         #el nodo pasa a ser parte de la trayectoria
        trazadoTrayectoria += ' -> ' + str(u.getValue())
        print(trazadoTrayectoria+'\n')
        if u.getValue() == nodoFinal.getValue():
            break
        #adicionamos los hijos a la pila
        hijos = list(map(lambda tupla: tupla[0],grafo.getChildren(u)))
        for v in hijos:
            if v not in nodosApilados:
                pila.append(v)
                nodosApilados.add(v)
        print("En Pila: {:}\n".format(list(map(lambda vertex: vertex.getValue(),pila))))
    return u.getValue() == nodoFinal.getValue()


def main():
    g = Grafo()
    lista = list(product([0,1],repeat=4))
    for c in lista:
        g.addNode(Node(c))
    
    #construimos el grafo de acuerdo al espacio de estados
    g.addEdge(Edge(g.getNode((0,0,0,0)),g.getNode((1,0,1,0))))
    g.addEdge(Edge(g.getNode((0,0,1,0)),g.getNode((1,0,1,0))))
    g.addEdge(Edge(g.getNode((0,0,1,0)),g.getNode((1,1,1,0))))
    g.addEdge(Edge(g.getNode((0,0,1,0)),g.getNode((1,0,1,1))))
    g.addEdge(Edge(g.getNode((1,0,1,1)),g.getNode((0,0,0,1))))
    g.addEdge(Edge(g.getNode((1,1,1,0)),g.getNode((0,1,0,0))))
    g.addEdge(Edge(g.getNode((0,1,0,0)),g.getNode((1,1,0,1))))
    g.addEdge(Edge(g.getNode((0,0,1,0)),g.getNode((1,1,0,1))))
    g.addEdge(Edge(g.getNode((1,1,1,1)),g.getNode((1,1,0,1))))
    DFS(g,g.getNode((0,0,1,0)),g.getNode((1,1,1,1)))
    #g.getChildren(g.getNode((0,0,0,0)))

main()