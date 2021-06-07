from enviroment import Piso
from agent import VacuumCleaner
def main():
    inicial = input("Ingrese la posicion inicial de la aspiradora: ").lower()
    if inicial == 'a':
        ubicacion = 0
    else:
        ubicacion = 1
    vA = int(input("Ingrese estado de la balsoda A: "))
    vB = int(input("Ingrese estado de la balsoda B: "))
    valdosaA = Piso(vA,'a')
    valdosaB = Piso(vB, 'b')
    aspiradora = VacuumCleaner([valdosaA,valdosaB],ubicacion)
    aspiradora.encender()
main()