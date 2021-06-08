from enviroment import Piso
from agent import VacuumCleaner
def main():
    inicial = input("Ingrese la posicion inicial de la aspiradora (a, b ó c): ").lower()
    if inicial == 'a':
        ubicacion = 0
    elif inicial=='b':
        ubicacion = 1
    else:
        ubicacion = 2
    vA = int(input("Ingrese estado de la balsoda A (1 es sucio 0 es limplio): "))
    vB = int(input("Ingrese estado de la balsoda B (1 es sucio 0 es limplio): "))
    vC = int(input("Ingrese estado de la balsoda C (1 es sucio 0 es limplio): "))
    print("=========================================\n")
    valdosaA = Piso(vA,'a')
    valdosaB = Piso(vB, 'b')
    valdosaC = Piso(vC,'c')
    aspiradora = VacuumCleaner([valdosaA,valdosaB,valdosaC],ubicacion)
    aspiradora.encender()
main()

