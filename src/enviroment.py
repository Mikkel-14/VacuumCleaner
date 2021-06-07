class Piso:
    def __init__(self,estado,nombre) -> None:
        self.estado = estado
        self.nombre = nombre
    
    def __str__(self) -> str:
        return "La valdosa {:} se encuentra en el estado {:}".format(self.nombre,self.estado)

    #vamos a implementar un patron observador para los cambios de estado
    def setObservado(self, obs):
        self.observed = obs
    
    def update(self):
        result = self.observed.getResultado()
        if result[0] == self.nombre:
            self.estado = result[1]

    