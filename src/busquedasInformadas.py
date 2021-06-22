from  ADT import Node, Edge, Grafo
from queue import PriorityQueue
#empezamos por determinar la heuristica de la linea recta 
h = dict()
h['Arad'] = 366
h['Bucharest'] = 0
h['Craiova'] = 160
h['Drobeta'] = 242
h['Eforie'] = 161
h['Fagaras'] = 176
h['Giurgiu'] = 77
h['Hirsova'] = 151
h['Iasi'] = 226
h['Lugoj'] = 244
h['Mehadia'] = 241
h['Neamt'] = 234
h['Oradea'] = 380
h['Pitesti'] = 100
h['Rimnicu'] = 193
h['Sibiu'] = 253
h['Timisoara'] = 329
h['Urziceni'] = 80
h['Vaslui'] = 199
h['Zerind'] = 374

def AStar(graph, nodoInicial, nodoFinal, heuristica):
    """
        Esta implementacion de la funcion A* usa f(n) = w(n) + h(n).
        Esto es, es como el algoritmo de Dijstra pero en vez de usar solo los pesos
        usa f.
    """
    nodosVisitados = set()
    g = dict()
    f = dict()
    colaPriorizada = PriorityQueue()
    for nodes in graph.adjacencyMap:
        g[nodes] = 100000
    g[nodoInicial] = 0
    for nodes in graph.adjacencyMap:
        f[nodes] = g[nodes]+heuristica[nodes.getValue()]
        colaPriorizada.put((f[nodes],nodes))
    u = nodoInicial
    while not u == nodoFinal:
        f_u, u = colaPriorizada.get()
        if u in nodosVisitados:
            continue
        print("Lugar actual: {:}, f = {:} + {:}".format(u.getValue(),g[u],heuristica[u.getValue()]))
        nodosVisitados.add(u)
        adyacentes = graph.getChildren(u)
        for (v, peso) in adyacentes:
            if v not in nodosVisitados:
                if g[u] + peso < g[v]:
                    g[v] = g[u] + peso
                    f[v] = g[v] + heuristica[v.getValue()]
                    colaPriorizada.put((f[v],v)) 

def main():
    """
        En esta funcion construiremos el grafo y aplicaremos la busqueda A*
    """
    gr = Grafo()
    ciudades = ['Oradea','Zerind','Arad','Sibiu','Timisoara','Lugoj','Mehadia','Drobeta','Craiova','Rimnicu','Pitesti','Fagaras','Bucharest','Giurgiu','Urziceni','Hirsova','Eforie','Vaslui','Iasi','Neamt']
    for c in ciudades:
        gr.addNode(Node(c))
    gr.addEdge(Edge(gr.getNode('Oradea'),gr.getNode('Zerind'),71))
    gr.addEdge(Edge(gr.getNode('Oradea'),gr.getNode('Sibiu'),151))
    gr.addEdge(Edge(gr.getNode('Arad'),gr.getNode('Zerind'),75))
    gr.addEdge(Edge(gr.getNode('Arad'),gr.getNode('Sibiu'),140))
    gr.addEdge(Edge(gr.getNode('Arad'),gr.getNode('Timisoara'),118))
    gr.addEdge(Edge(gr.getNode('Lugoj'),gr.getNode('Timisoara'),111))
    gr.addEdge(Edge(gr.getNode('Lugoj'),gr.getNode('Mehadia'),70))
    gr.addEdge(Edge(gr.getNode('Drobeta'),gr.getNode('Mehadia'),75))
    gr.addEdge(Edge(gr.getNode('Drobeta'),gr.getNode('Craiova'),120))
    gr.addEdge(Edge(gr.getNode('Rimnicu'),gr.getNode('Craiova'),146))
    gr.addEdge(Edge(gr.getNode('Pitesti'),gr.getNode('Craiova'),138))
    gr.addEdge(Edge(gr.getNode('Rimnicu'),gr.getNode('Pitesti'),97))
    gr.addEdge(Edge(gr.getNode('Rimnicu'),gr.getNode('Sibiu'),80))
    gr.addEdge(Edge(gr.getNode('Fagaras'),gr.getNode('Sibiu'),99))
    gr.addEdge(Edge(gr.getNode('Fagaras'),gr.getNode('Bucharest'),211))
    gr.addEdge(Edge(gr.getNode('Pitesti'),gr.getNode('Bucharest'),101))

    AStar(gr,gr.getNode("Lugoj"),gr.getNode("Bucharest"),h)

main()
    



