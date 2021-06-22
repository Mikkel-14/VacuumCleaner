#empezamos creando las estructuras base para nuestro grafo
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
    def __key(self):
        if isinstance(self.value,tuple):
            a,b = self.value
            return (str(a),b)
        return self.value
    def __hash__(self) -> int:
        return hash(self.__key())
    def __eq__(self, o: object) -> bool:
        if(isinstance(o,Node)):
            return self.__key() == o.__key()
        return False
    def __lt__(self,other):
        return hash(self.__key()) < hash(other.__key())
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
            print("El nodo ya se encuentra en el grafo")
    
    def addEdge(self,edge):
        u,v = edge.getIncidentNodes()
        peso = edge.getPeso()
        if (u in self.adjacencyMap) and (v in self.adjacencyMap):
            self.adjacencyMap[u].append((v,peso))
            self.adjacencyMap[v].append((u,peso))
        else:
            print('No se agrego el edge')

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