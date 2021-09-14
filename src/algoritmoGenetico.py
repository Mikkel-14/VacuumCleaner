import copy
import math
import random
from copy import deepcopy
class city:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = math.sqrt((xDis ** 2) + (yDis ** 2))
        return distance
    
    def _repr_(self):
        return "(" + str(self.x) + "," + str(self.y)+ ")"
    
 
Londres = city(x=int(51.509865), y=int(-0.118092))
Venecia= city(x=int(45.438759), y=int(12.327145))
Dunedin = city(x=int(-45.8742), y=int(170.5036))
Singapur = city(x=int(1.290270),y=int(103.851959))
Beijing = city(x=int(39.916668),y=int(116.383331))
Phoenix = city(x=int(33.448376),y=int(-112.074036))
Tokio = city(x=int(35.652832),y=int(139.839478))
Victoria = city(x=int(48.407326),y=int(-123.329773))
ciudades = list()
ciudades.append(Londres)
ciudades.append(Venecia)
ciudades.append(Dunedin)
ciudades.append(Singapur)
ciudades.append(Beijing)
ciudades.append(Phoenix)
ciudades.append(Tokio)
ciudades.append(Victoria)
LISTA1 = [3,5,7,2,1,6,4,8]
LISTA2 = [2,5,7,6,8,1,3,4]
LISTA3 = [1,6,7,5,2,4,3,8]
LISTA4 = [4,2,7,1,3,8,6,5]

def idoneidad(arreglo):
    suma = 0
    for i in range(1,8):
        suma +=  ciudades[arreglo[i]-1].distance(ciudades[arreglo[i-1]-1])
    return suma

def seleccion(population,fitness):
    #calculamos la idoneidad de cada elemento
    utilidades = list()
    for element in population:
        utilidades.append((fitness(element),element))
    ordenados = sorted(utilidades,reverse=True)
    number = random.randint(0,len(population)-1)
    return ordenados[number][1]

def reproducir(x,y):
    progenitorA = copy.deepcopy(x)
    progenitorB = copy.deepcopy(y)
    aleatorio = random.randint(0,len(x)-1)
    fragmentoA = progenitorA[aleatorio:]
    fragmentoB = progenitorB[aleatorio:]
    subcadenaA = []
    subcadenaB = []
    for i in progenitorA[:aleatorio]:
        while i in fragmentoB:
            i = fragmentoA[fragmentoB.index(i)]
        subcadenaA.append(i)
    for i in progenitorB[:aleatorio]:
        while i in fragmentoA:
            i = fragmentoB[fragmentoA.index(i)]
        subcadenaB.append(i)
    return fragmentoA + subcadenaB

def GA(population,fitness):
    newPopularion = list() 
    for i in range(len(population)):
        x = seleccion(population,fitness)
        y = seleccion(population,fitness)
        hijo = reproducir(x,y)
        if random.randint(1,6)==3:
            cambio = random.randint(0,len(hijo)-1)
            cambio2 = random.randint(0,len(hijo)-1)
            val = hijo[cambio]
            hijo[cambio] = hijo[cambio2]
            hijo[cambio2] = val
        newPopularion.append(hijo)
    return newPopularion

POBLACION = [LISTA1,LISTA2,LISTA3,LISTA4]
print("POBLACION")
for p in POBLACION:
    valor = idoneidad(p)
    print("El padre {} tiene una idoneidad {}".format(p,valor))
print("--------------------------")
print("Hijos:")
hijos = GA(POBLACION,idoneidad) 
print(hijos)
print("Idoneidad por cada hijo:")
for h in hijos:
    valor = idoneidad(h)
    print("El hijo {} tiene una idoneidad {}".format(h,valor))