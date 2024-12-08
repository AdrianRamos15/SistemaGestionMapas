from Mapa import Mapa
from Estado import Estado
from Problema import Problema
from leer_ejemplo import leer_ejemplo
from algoritmoBusqueda import algoritmoBusqueda

import numpy as np

if __name__ == "__main__":
    
    # Ejemplo de uso de Mapa (Tarea 1)
    hdf5_filename = "NuevoMapa.hdf5" 
    mapa = Mapa(hdf5_filename)
    y_umt = 3123589						
    x_umt = 275945	
    valor = mapa.umt_YX(y_umt, x_umt)
    print(f"Valor en ({y_umt}, {x_umt}): {valor}")
    
    
    '''# EJEMPLO DE USO: Metodo Resize
    # Dejamos el resultado de la operación sin mas para posteriormente sustituir los nan
    def transform(cells):
        if len(cells) == 0 or np.all(np.isnan(cells)):
            return np.nan  # o cualquier valor predeterminado que desees asignar en caso de array vacío o de NaN
        cells[cells < -99990] = np.nan
        return np.nanmean(cells) #PUEDE CAMBIAR 
            

    nuevo_mapa = mapa.resize(200 , transform, "NuevoMapa") #PUEDE CAMBIAR
    print(f"Nuevo mapa creado: {nuevo_mapa.filename}")'''
    
            
    '''# Ejemplo de uso de Problema y Estado (Tarea 2)
    y_inicial = 3109961
    x_inicial = 278853

    problema = Problema(mapa, y_inicial, x_inicial, y_inicial, x_inicial)  # No es necesario especificar las coordenadas del estado objetivo para sacar los sucesores de un estado
    estado_inicial = Estado(y_inicial, x_inicial)

    print("Sucesores del estado inicial:")
    sucesores = problema.sucesores(estado_inicial)

    for sucesor in sucesores:
        print(sucesor)'''
        



    # Ejemplo de uso tarea 3
    archivo_problema = 'archivoLectura.txt' # Reemplazar el con el nombre del archivo que se quiere probar
    problema, estrategia, profundidad_maxima = leer_ejemplo(archivo_problema)
    tipo_heuristica = 'Hmanhattan' #PUEDE CAMBIAR

    # Ejecutar algoritmo de búsqueda
    solucion = algoritmoBusqueda(problema, estrategia, profundidad_maxima, tipo_heuristica)

    
    if solucion:
        print("¡Solución encontrada!")
        print("Camino de la solución:")
        for nodo in solucion:
            print(nodo)
                
    else:
        print("No se encontró una solución dentro de la profundidad máxima.")
        
    
    
