from enviroment import Piso
#vamos a elaborar un agente reflejo simple, sin tablas de busqueda
#sino con reglas condicion-accion
class VacuumCleaner:
    def __init__(self, listaValdosas,ubicacion) -> None:
        self.ubicacion = ubicacion
        self.resultado = None
        self.listaValdosas = listaValdosas
        for valdosa in listaValdosas:
            valdosa.setObservado(self)
    
    def sensar(self):
        """
        El agente sensa el ambiente, esto es, mira las baldosas
        en las que no se encuentra
        """
        self.entorno = list()
        for valdosa in self.listaValdosas:
            if not valdosa.nombre == self.listaValdosas[self.ubicacion].nombre:
                self.entorno.append(valdosa)

    def derecha(self):
        if self.ubicacion +1 >3:
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
        self.notify() #notificamos la acción al entorno
    
    def getResultado(self):
        return self.resultado

    def notify(self):
        for valdosa in self.listaValdosas:
            valdosa.update()

    def encender(self):
        objetivo = False #el objetivo es que todo el ambiente este limpio
        pasos = 0 #los pasos nos indican el numero de iteraciones
        while not objetivo:
            print('--->Estado presente, (posicion de aspiradora y estado de valdosa): ({:},{:})\n'.format(self.listaValdosas[self.ubicacion].nombre,self.listaValdosas[self.ubicacion].estado ))
            self.sensar() #el senso del ambiente es una condicion necesaria porque un ambiente parcialmente observable limitaría incluso más la inteligencia del agente
            if self.listaValdosas[self.ubicacion].estado ==1: #REGLA 1 := Si mi baldosa actual esta sucia, limpio, caso contrario, me muevo
                print("==>Acción: Limpiar la valdosa {:} \n".format(self.listaValdosas[self.ubicacion].nombre))
                self.limpiar(self.listaValdosas[self.ubicacion])
            else:
                for z in self.entorno: #ahora voy a buscar una baldosa sucia en en entorno
                    if z.estado ==1:
                        #con el offset comparo por los nombres de las baldosas el orden
                        # (si es mayor o menor ej a>b?) para saber a donde moverse
                        offset = z.nombre > self.listaValdosas[self.ubicacion].nombre
                        if offset:
                            print("==>Accion: nos movemos a la derecha\n")
                            self.derecha()
                        else:
                            print("==>Accion: nos movemos a la izquierda\n")
                            self.izquierda()
                        break
            pasos +=1 
            sum = 0
            for v in self.listaValdosas: #si la sumatoria es 0, implica que todo el entorno esta limpio
                sum += v.estado
            objetivo = sum == 0
        for v in self.listaValdosas: #imprimo el estado final de las valdosas
            print(v)
            print("\n")
        print("=========================================\n")
        print("Numero total de pasos: {:}".format(pasos)) 