import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd 
df = pd.read_csv("house_price.csv")
x = df.iloc[:,[1,6,7]].values

model = KMeans(n_clusters=2,init='random',n_init = 10, max_iter = 300,tol = 1e-04, random_state=0)
y_clusters = model.fit_predict(x)
# 3d scatterplot using matplotlib
fig = plt.figure(figsize = (15,15))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x[y_clusters == 0,0],x[y_clusters == 0,1],x[y_clusters == 0,2], s = 40 , color = 'blue', label = "cluster 0")
ax.scatter(x[y_clusters == 1,0],x[y_clusters == 1,1],x[y_clusters == 1,2], s = 40 , color = 'orange', label = "cluster 1")
ax.set_xlabel('Precio')
ax.set_ylabel('Fecha de contruccion')
ax.set_zlabel('Area')
ax.legend()
plt.show()