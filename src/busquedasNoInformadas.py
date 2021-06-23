#empezamos creando las estructuras base para nuestro grafo
from typing import ContextManager


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

#ahora podemos implementar la busqueda sobre nuestro grafo
def BFS(grafo, nodoInicial, nodoFinal):
    """
    La busqueda primero en anchura hace uso de una cola para recorrer el grafo 
    y un conjunto de nodos encolados para evitar repeticiones
    """
    nodosEncolados = set()
    cola = list()
    #empezamos desde el nodo inicial
    cola.insert(0,nodoInicial)
    u = nodoInicial
    nodosEncolados.add(u)
    trazadoTrayectoria = 'Trayectoria BFS: '
    while not u.getValue()==nodoFinal.getValue():
        #sacamos el primer nodo ingresado
        u = cola.pop()
        #el nodo pasa a ser parte de la trayectoria
        trazadoTrayectoria += ' -> ' +u.getValue()
        print(trazadoTrayectoria+'\n')
        #adicionamos los hijos del nodo a la cola
        hijos = list(map(lambda tupla: tupla[0],grafo.getChildren(u)))
        for v in hijos:
            if v not in nodosEncolados:
                cola.insert(0,v)
                nodosEncolados.add(v)
        print("En Cola: {:}\n".format(list(map(lambda vertex: vertex.getValue(),cola))))

def limitedDFS(grafo, nodoInicial, nodoFinal, limiteD):
    """
    Esta funcion implementa una busqueda primero en profundidad con un limite de exploracion en profundidad d. Igual que en
    BFS, tiene un conjunto de nodos ya apilados
    """
    nodosApilados = set()
    pila = list()
    #empezamos desde el nodo inicial
    pila.append(nodoInicial)
    u = nodoInicial
    nodosApilados.add(u)
    trazadoTrayectoria = 'Trayectoria DFS, con limite d={:}: '.format(limiteD)
    profundidad  = 0
    while (profundidad <= limiteD) and (len(pila)!=0):
        anterior = u
        #sacamos de la pila al nodo
        u = pila.pop()
         #el nodo pasa a ser parte de la trayectoria
        trazadoTrayectoria += ' -> ' +u.getValue()
        print(trazadoTrayectoria+'\n')
        if u.getValue() == nodoFinal.getValue():
            break
        if u in list(map(lambda tupla: tupla[0],grafo.getChildren(anterior))):
            profundidad += 1
        else:
            profundidad -= 1
        if profundidad == limiteD:
            continue
        #adicionamos los hijos a la pila
        hijos = list(map(lambda tupla: tupla[0],grafo.getChildren(u)))
        for v in hijos:
            if v not in nodosApilados:
                pila.append(v)
                nodosApilados.add(v)
        print("En Pila: {:}\n".format(list(map(lambda vertex: vertex.getValue(),pila))))
    return u.getValue() == nodoFinal.getValue()

def DFSIterativo(grafo, n0,nf):
    incremento = 1
    while True:
        if limitedDFS(grafo,n0,nf,incremento):
            break
        incremento += 1

def main():
    g = Grafo()
    ciudades = ['Reynosa', 'Matamoros','Tampico','Tuxpan','Poza Rica','Veracruz','Jalapa','Cordoba','Orizaba','Puebla','CDMX','Oaxaca','Tehuantepec','Salina Cruz','Huatulco','Puerto Escondido','Juchitan','Ixtepec','Ixaltepec','Acayucan','Mihatitlan','Coatzacoalcos','Cardenas','Villahermosa','Tuxtla Gutierrez','Tonala','Pijijlapan','Huixtla','Tapachula','Palenque','Ococingo','San Cristobal de las Casas','Comitan','Ciudad del Carmen','Campeche','Chetumal','Merida','Playa del Carmen','Cancun']
    for c in ciudades:
        g.addNode(Node(c))
    g.addEdge(Edge(g.getNode('Reynosa'),g.getNode('Matamoros')))
    g.addEdge(Edge(g.getNode('Tampico'),g.getNode('Matamoros')))
    g.addEdge(Edge(g.getNode('Tampico'),g.getNode('Tuxpan')))
    g.addEdge(Edge(g.getNode('Tuxpan'),g.getNode('Poza Rica')))
    g.addEdge(Edge(g.getNode('Poza Rica'),g.getNode('Veracruz')))
    g.addEdge(Edge(g.getNode('Jalapa'),g.getNode('Veracruz')))
    g.addEdge(Edge(g.getNode('Cordoba'),g.getNode('Veracruz')))
    g.addEdge(Edge(g.getNode('Acayucan'),g.getNode('Veracruz')))
    g.addEdge(Edge(g.getNode('Cordoba'),g.getNode('Orizaba')))
    g.addEdge(Edge(g.getNode('Puebla'),g.getNode('Orizaba')))
    g.addEdge(Edge(g.getNode('Puebla'),g.getNode('CDMX')))
    g.addEdge(Edge(g.getNode('Puebla'),g.getNode('Oaxaca')))
    g.addEdge(Edge(g.getNode('Tehuantepec'),g.getNode('Oaxaca')))
    g.addEdge(Edge(g.getNode('Tehuantepec'),g.getNode('Salina Cruz')))
    g.addEdge(Edge(g.getNode('Tehuantepec'),g.getNode('Juchitan')))
    g.addEdge(Edge(g.getNode('Huatulco'),g.getNode('Salina Cruz')))
    g.addEdge(Edge(g.getNode('Huatulco'),g.getNode('Puerto Escondido')))
    g.addEdge(Edge(g.getNode('Ixtepec'),g.getNode('Juchitan')))
    g.addEdge(Edge(g.getNode('Ixtepec'),g.getNode('Ixaltepec')))
    g.addEdge(Edge(g.getNode('Acayucan'),g.getNode('Juchitan')))
    g.addEdge(Edge(g.getNode('Tonala'),g.getNode('Juchitan')))
    g.addEdge(Edge(g.getNode('Acayucan'),g.getNode('Mihatitlan')))
    g.addEdge(Edge(g.getNode('Coatzacoalcos'),g.getNode('Mihatitlan')))
    g.addEdge(Edge(g.getNode('Coatzacoalcos'),g.getNode('Cardenas')))
    g.addEdge(Edge(g.getNode('Villahermosa'),g.getNode('Cardenas')))
    g.addEdge(Edge(g.getNode('Tuxtla Gutierrez'),g.getNode('Cardenas')))
    g.addEdge(Edge(g.getNode('Tuxtla Gutierrez'),g.getNode('Tonala')))
    g.addEdge(Edge(g.getNode('Pijijlapan'),g.getNode('Tonala')))
    g.addEdge(Edge(g.getNode('Pijijlapan'),g.getNode('Huixtla')))
    g.addEdge(Edge(g.getNode('Tapachula'),g.getNode('Huixtla')))
    g.addEdge(Edge(g.getNode('Villahermosa'),g.getNode('Palenque')))
    g.addEdge(Edge(g.getNode('Villahermosa'),g.getNode('Ciudad del Carmen')))
    g.addEdge(Edge(g.getNode('Ococingo'),g.getNode('Palenque')))
    g.addEdge(Edge(g.getNode('Ococingo'),g.getNode('San Cristobal de las Casas')))
    g.addEdge(Edge(g.getNode('Comitan'),g.getNode('San Cristobal de las Casas')))
    g.addEdge(Edge(g.getNode('Campeche'),g.getNode('Ciudad del Carmen')))
    g.addEdge(Edge(g.getNode('Campeche'),g.getNode('Chetumal')))
    g.addEdge(Edge(g.getNode('Campeche'),g.getNode('Merida')))
    g.addEdge(Edge(g.getNode('Cancun'),g.getNode('Merida')))
    g.addEdge(Edge(g.getNode('Cancun'),g.getNode('Playa del Carmen')))
    g.addEdge(Edge(g.getNode('Chetumal'),g.getNode('Playa del Carmen')))
    #mandamos a correr el BFS
    BFS(g,g.getNode('Salina Cruz'),g.getNode('Reynosa'))
    #print(limitedDFS(g,g.getNode('Salina Cruz'),g.getNode('Reynosa'),5))
    #DFSIterativo(g,g.getNode('Salina Cruz'),g.getNode('Reynosa'))
main()
