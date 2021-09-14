import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import string
A = [[0,0,0,0,0,0,0],[2.15,0,0,0,0,0,0],[0.7,1.53,0,0,0,0,0],[1.07,1.14,0.43,0,0,0,0],[0.85,1.38,0.21,0.29,0,0,0],[1.16,1.01,0.55,0.22,0.41,0,0],[1.56,2.83,1.86,2.04,2.02,2.05,0]]
G = nx.from_numpy_matrix(np.array(A))
G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),string.ascii_uppercase)))
#G = nx.drawing.nx_agraph.to_agraph(G)
nx.draw(G, with_labels=True)
plt.show()
