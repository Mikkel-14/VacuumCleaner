class Node:
    def __init__(self, value) -> None:
        """
        Dentro del nodo se puede almacenar cualquier tipo de dato
        """
        self.value = value
        self.parent = [] 
        self.util = None
    def getValue(self):
        return self.value
    def setParent(self, node):
        self.parent.append(node)
    def getParent(self):
        return self.parent
    def hasUtil(self):
        return self.util != None
    def setUtil(self, val):
        self.util = val
    def getUtil(self):
        return self.util
    def __key(self):
        return str(self.value)
    def __hash__(self) -> int:
        return hash(str(self.value))
    def __eq__(self, o: object) -> bool:
        if(isinstance(o,Node)):
            return self.value == o.value
        return False

class Edge:
    """
    Vamos a tener aristas dirigidas
    A -> B
    """
    def __init__(self, nodoA, nodoB) -> None:
        self.nodes = (nodoA,nodoB)
        nodoB.setParent(nodoA)
    def getIncidentNodes(self):
        return self.nodes

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Grafo(metaclass=Singleton):
    """ Esta clase implementa el comportamiento de un grafo, usando nodos (V)
    y edges (E) mediante un mapa de adyacencia
    """
    def __init__(self) -> None:
        self.adjacencyMap = dict()
    
    def addNode(self,nodo):
        if nodo not in self.adjacencyMap:
            self.adjacencyMap[nodo] = list()
        else:
            print("El nodo ya se encuentra en el grafo")
    def addEdge(self,edge):
        u,v = edge.getIncidentNodes()
        if (u in self.adjacencyMap) and (v in self.adjacencyMap):
            self.adjacencyMap[u].append(v)
        else:
            print('No se agrego la arista')
    def getChildren(self,node):
        hijos = list()
        if node in self.adjacencyMap:
            hijos = self.adjacencyMap[node]
        return hijos
    def isEmpty(self):
        return self.adjacencyMap == dict()
    def getNode(self, value):
        for key in self.adjacencyMap:
            if key.getValue() == value:
                return key
        return None
    def getLeaves(self):
        leaves = list()
        for key in self.adjacencyMap:
            if self.adjacencyMap[key] == []:
                leaves.append(key)
        return leaves
            

