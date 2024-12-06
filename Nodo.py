class Nodo:

    def __init__(self, ID, padre, estado, costo, accion, profundidad, heuristica, estrategia):
        self.ID = ID
        self.padre = padre
        self.estado = estado
        self.costo = costo
        self.accion = accion
        self.profundidad = profundidad
        self.heuristica = heuristica
        self.valor = 0
        self.estrategia(estrategia) 

    def __lt__(self, other):
        if self.valor == other.valor:
            return self.ID < other.ID
        return self.valor < other.valor

    def camino(self): 
        if self.padre is None: #si el nodo es la raiz del arbol
            return [self] #se devuelve a el mismo 
        else:
            return self.padre.camino() + [self] #imprimimos desde el nodo actual hasta el padre
    
    def estrategia(self ,estrategia):
        if estrategia == "BFS": #anchura
            self.valor = self.profundidad 
        elif estrategia == "DFS": #profundidad
            self.valor = 1 / (1 + self.profundidad)
        elif estrategia == "UCS": #costo uniforme
            self.valor = self.costo[0]
        elif estrategia == "GREEDY": #voraz
            self.valor = self.heuristica
        elif estrategia == "A*": #A*
            self.valor = self.costo[0] + self.heuristica
            
        else:
            raise ValueError(f"Estrategia no reconocida: {estrategia}")
        
    def __repr__(self):
        if self.padre == None: # Para que no el nodo inicial no imprima el id del padre ya que no tiene
            return f"[{self.ID}][{self.costo},{self.estado.id},{self.padre},{self.accion},{self.profundidad},{self.heuristica},{self.valor}]"
            
        return f"[{self.ID}][{self.costo},{self.estado.id},{self.padre.ID},{self.accion},{self.profundidad},{self.heuristica},{self.valor}]"
