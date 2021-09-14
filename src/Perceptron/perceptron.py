import numpy as np
import matplotlib.pyplot as plt
#valores aleatorios para los pesos
w = np.random.rand(1,3)*10
w1 = np.round(w[0][0],1)
w2 = np.round(w[0][1],1)
w0 = np.round(w[0][2],1)
#informacion base
x = [[0,0],[0,1],[1,0],[1,1]]
inputs = np.asarray(x)
#el AND es equivalente a la multiplicacion
out = inputs[:,0]*inputs[:,1]
#activation fx
def step(net):
    if net >= 0:
        return 1
    else:
        return 0

#vector de error
error = np.array([0,0,0,0])
for i in range(len(x)):
    f_net = step(np.dot(np.asarray([w1,w2]),x[i])+w0)
    error[i] = out[i] - f_net
E = np.sum(error)

#correccion de parametros
max_it = 1000
t = 1
alpha = 0.1
vals = [[w1,w2,w0]]
while t<max_it and E != 0:
    for i in range(len(x)):
        f_net = step(np.dot(np.asarray([w1,w2]),x[i])+w0)
        error[i] = out[i] - f_net
        w1 = w1 + alpha*error[i]*x[i][0]
        w2 = w2 + alpha*error[i]*x[i][1]
        w0 = w0 + alpha*error[i]
        vals.append([w1,w2,w0])
    E = np.sum(error)
    t += 1


lineas  =[]
for pesos in vals:
    linea = []
    for j in x:
        linea.append((1/pesos[1])*(-pesos[0]*j[0]-pesos[2]))
    lineas.append(linea)

plt.scatter(inputs[:,0],inputs[:,1])
imgNumber = 1
for row in lineas:
    plt.plot(inputs[:,0],row)
    plt.savefig('{}.png'.format(imgNumber))
    imgNumber += 1
plt.show()