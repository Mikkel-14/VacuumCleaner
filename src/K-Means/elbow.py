import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data = [
    [1,1],
    [2,4],
    [3,2],
    [3,5],
    [4,4],
    [4,7],
    [6,4],
    [6,6]
]

distorsiones = list()

for i in range(1,8):
    km = KMeans(
        n_clusters = i, init ='random',
        n_init = 10, max_iter = 300,
        tol = 1e-04, random_state=0
    )
    km.fit(data)
    distorsiones.append(km.inertia_)
plt.plot(range(1,8),distorsiones, marker = "o")
plt.xlabel("Number of clusters")
plt.ylabel('Distortion')
plt.show()