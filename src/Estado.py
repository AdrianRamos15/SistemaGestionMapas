class Estado:
    
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.id = f"({y},{x})"
    
    def __str__(self):
        return f"({self.y},{self.x})"
    
    def __repr__(self):
        return f"({self.y},{self.x})"
    
    '''#comprobar si un estado está repetido 
    def es_igual(self, otro_estado): #para comprobar que el estado no está repetido
        return self.id == otro_estado.id'''
       

    