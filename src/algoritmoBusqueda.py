from Nodo import Nodo
from Frontera import Frontera
from EstadosVisitados import EstadosVisitados
from math import sqrt 




def algoritmoBusqueda(problema, estrategia, profundidad_maxima, tipo_heuristica):
    frontera = Frontera()
    visitados = EstadosVisitados()  
    id_nodo = 0
    solucion = False

    
    #id, nodo_padre, estado, costo, accion, profundidad, heuristica, estrategia(valor)
    nodo_inicial = Nodo(id_nodo, None, problema.estado_inicial, (0, 0), "", 0, 0, estrategia)
    
    # Calcular heurística para el nodo inicial
    if estrategia == "GREEDY" or estrategia == "A*":
        if tipo_heuristica == "Heuclidea":
            heuristica_inicial = heuristica_heuclidea(nodo_inicial.estado, problema.estado_objetivo)
        elif tipo_heuristica == "Hmanhattan":
            heuristica_inicial = heuristica_hmanhattan(nodo_inicial.estado, problema.estado_objetivo)
    else:
        heuristica_inicial = 0

    nodo_inicial.heuristica = heuristica_inicial
    frontera.insertar(nodo_inicial)
    

    
    while frontera.no_esta_vacia() and not solucion: 
        nodo_actual = frontera.tomar()
        
        
        
        if problema.objetivo(nodo_actual.estado):
            solucion = True
        
        
        #aqui se realiza la poda
        elif nodo_actual.profundidad <= profundidad_maxima and not visitados.contiene(nodo_actual.estado):  
            visitados.insertar(nodo_actual.estado)  

            
            
            sucesores = problema.sucesores(nodo_actual.estado) 
            
            for sucesor in sucesores:
                id_nodo += 1
                
                # Calculo de costo 
                costo = (nodo_actual.costo[0] + sucesor[2][0], 
                            max(nodo_actual.costo[1], sucesor[2][1]))
                
                if estrategia == "GREEDY" or estrategia == "A*":
                    if tipo_heuristica == "Heuclidea":
                        heuristica = heuristica_heuclidea(sucesor[1], problema.estado_objetivo)
                    elif tipo_heuristica == "Hmanhattan":
                        heuristica = heuristica_hmanhattan(sucesor[1], problema.estado_objetivo)
                else:
                    heuristica = 0
                 
                # Propiedades del nuevo nodo
                nuevo_nodo = Nodo(id_nodo,
                                  nodo_actual, 
                                  sucesor[1],
                                  costo,
                                  sucesor[0],
                                  nodo_actual.profundidad + 1,
                                  heuristica,
                                  estrategia)      
                frontera.insertar(nuevo_nodo)  
                
    
                
    camino = []     
    if solucion:
        camino = nodo_actual.camino()
         
    return camino #si camino esta vacio no se encontro solucion
    
#f"[{self.ID}][{self.costo},{self.estado.id},{self.padre.ID},{self.accion},{self.profundidad},{self.heuristica},{self.valor}]" -> Nodo


def heuristica_heuclidea(estado, estado_objetivo):
    dy, dx = estado_objetivo.y, estado_objetivo.x
    y, x = estado.y, estado.x
    return sqrt((dx - x) ** 2 + (dy - y) ** 2)


def heuristica_hmanhattan(estado, estado_objetivo):
    dy, dx = estado_objetivo.y, estado_objetivo.x
    y, x = estado.y, estado.x
    return abs(dx - x) + abs(dy - y)


        
