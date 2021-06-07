from enviroment import Piso

class VacuumCleaner:
    def __init__(self, listaValdosas,ubicacion) -> None:
        self.ubicacion = ubicacion
        self.resultado = None
        self.listaValdosas = listaValdosas
        for valdosa in listaValdosas:
            valdosa.setObservado(self)
    
    def sensar(self):
        for valdosa in self.listaValdosas:
            if not valdosa.nombre == self.listaValdosas[self.ubicacion].nombre:
                self.next = valdosa

    def derecha(self):
        if self.ubicacion +1 >2:
            pass
        else:
            self.ubicacion += 1
    
    def izquierda(self):
        if self.ubicacion -1 <0:
            pass
        else:
            self.ubicacion -= 1
    
    def limpiar(self, valdosa):
        self.resultado = (valdosa.nombre, 0)
        self.notify()
    
    def getResultado(self):
        return self.resultado

    def notify(self):
        for valdosa in self.listaValdosas:
            valdosa.update()

    def encender(self):
        objetivo = False
        pasos = 0
        while not objetivo:
            self.sensar()
            if self.listaValdosas[self.ubicacion].estado ==1:
                print("==>Acción: Limpiar la valdosa {:} \n".format(self.listaValdosas[self.ubicacion].nombre))
                self.limpiar(self.listaValdosas[self.ubicacion])
            else:
                if self.listaValdosas[self.ubicacion].nombre == 'a':
                    print("==>Accion: nos movemos a la derecha\n")
                    self.derecha()
                elif self.listaValdosas[self.ubicacion].nombre == 'b':
                     print("==>Accion: nos movemos a la izquierda\n")
                     self.izquierda()
            pasos +=1 
            sum = 0
            for v in self.listaValdosas:
                sum += v.estado
            objetivo = sum == 0
        for v in self.listaValdosas:
            print(v)
            print("\n")
        print("=========================================\n")
        print("Numero total de pasos: {:}".format(pasos))