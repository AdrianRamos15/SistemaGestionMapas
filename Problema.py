from Estado import Estado
from math import sqrt
 

class Problema:
    def __init__(self, mapa, y_inicial, x_inicial, y_destino, x_destino):
        self.mapa = mapa
        self.estado_inicial = Estado(y_inicial, x_inicial)
        self.estado_objetivo = Estado(y_destino, x_destino)

    def objetivo(self, estado):
        return estado.y == self.estado_objetivo.y and estado.x == self.estado_objetivo.x

    def sucesores(self, estado):
        sucesores = []
        
        #for direccion in ['N', 'E', 'S', 'O']: #PUEDE CAMBIAR
        for direccion in ['N', 'NE', 'E', 'SE', 'S', 'SO', 'O', 'NO']: #PUEDE CAMBIAR
            nuevo_estado = self.desplazar(estado, direccion)
            if self.acc_valida1(nuevo_estado):
                longitud, altura = self.calcular_costo(estado, nuevo_estado,direccion)
                acc = (direccion, nuevo_estado, (longitud, round(altura, 3)))
                if self.acc_valida2(acc):
                    sucesores.append(acc)

        return sucesores

    def desplazar(self, estado, direccion):
        '''movimiento = {'N': (1, 0), 'NE': (1, 1),'E': (0, 1), 'SE': (-1, 1), 'S': (-1, 0), 'SO': (-1, -1), 'O': (0, -1), 'NO': (1, -1)} #PUEDE CAMBIAR 
        nuevo_y = (estado.y + movimiento[direccion][0] * self.mapa.sizeCell)
        nuevo_x = (estado.x + movimiento[direccion][1] * self.mapa.sizeCell)'''
        if direccion == 'N':
            nuevo_y = estado.y + 1 * self.mapa.sizeCell
            nuevo_x = estado.x
        elif direccion == 'NE':
            nuevo_y = estado.y + 1 * self.mapa.sizeCell
            nuevo_x = estado.x + 1 * self.mapa.sizeCell
        elif direccion == 'E':
            nuevo_y = estado.y
            nuevo_x = estado.x + 1 * self.mapa.sizeCell
        elif direccion == 'SE':
            nuevo_y = estado.y - 1 * self.mapa.sizeCell
            nuevo_x = estado.x + 1 * self.mapa.sizeCell
        elif direccion == 'S':
            nuevo_y = estado.y - 1 * self.mapa.sizeCell
            nuevo_x = estado.x
        elif direccion == 'SO':
            nuevo_y = estado.y - 1 * self.mapa.sizeCell
            nuevo_x = estado.x - 1 * self.mapa.sizeCell
        elif direccion == 'O':
            nuevo_y = estado.y
            nuevo_x = estado.x - 1 * self.mapa.sizeCell
        elif direccion == 'NO':
            nuevo_y = estado.y + 1 * self.mapa.sizeCell
            nuevo_x = estado.x - 1 * self.mapa.sizeCell
        else:
            raise ValueError("Dirección no válida")

        return Estado(nuevo_y, nuevo_x)

    def calcular_costo(self, estado_actual, nuevo_estado, direccion):
        if direccion in ['NE','SE','SO','NO']: #PUEDE CAMBIAR 
            longitud = 1 * self.mapa.sizeCell * sqrt(2)
        else: 
            longitud = 1 * self.mapa.sizeCell
        altura = abs(self.mapa.umt_YX(nuevo_estado.y, nuevo_estado.x) - self.mapa.umt_YX(estado_actual.y, estado_actual.x))
        return longitud, altura

    def acc_valida1(self, nuevo_estado):
        return self.mapa.umt_YX(nuevo_estado.y, nuevo_estado.x) != self.mapa.nodata_value
        
    def acc_valida2(self, acc):
        #acc[2][1] es la altura del nuevo estado 
        return acc[2][1] <= 456  #altura maxima #PUEDE CAMBIAR 
    

