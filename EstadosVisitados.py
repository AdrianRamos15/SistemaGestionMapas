class EstadosVisitados:
    def __init__(self):
        self.estados = set()

    def contiene(self, estado): # Comprobacion de si un estado esta en el conjunto 
        return estado.id in self.estados 
    

    def insertar(self, estado): # Incorporar un estado al conjunto 
        self.estados.add(estado.id)


