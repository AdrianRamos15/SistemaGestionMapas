from bisect import insort
from Nodo import Nodo

class Frontera:
    def __init__(self):
        self.nodos = [] # Almacena los nodos del árbol

    def insertar(self, nodo: Nodo):# Insertar el nodo en la frontera en orden
        insort(self.nodos, nodo)

    def tomar(self):# Tomar el nodo con mayor prioridad
        return self.nodos.pop(0)
    
    def no_esta_vacia(self): # Indica si la frontera contiene nodos 
        return len(self.nodos) != 0


'''import heapq 
from Nodo import Nodo

class Frontera:
    def __init__(self):
        self.nodos = [] # Alamacena los nodos del arbol de 
        heapq.heapify(self.nodos) 

    def insertar(self, nodo: Nodo):# Insertar el nodo en la frontera en orden
        heapq.heappush(self.nodos, nodo)

    def tomar(self):# Tomar el nodo con mayor prioridad
        return heapq.heappop(self.nodos)
    
    
    def no_esta_vacia(self): # Indica si la frontera contiene nodos 
        return len(self.nodos) != 0'''
    

