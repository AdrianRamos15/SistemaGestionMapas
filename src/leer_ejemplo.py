from Mapa import Mapa
from Problema import Problema
import ast

def leer_ejemplo(archivo):
    with open(archivo, 'r') as file:
        lines = file.readlines()

    # Extraer información del archivo
    hdf5_filename = lines[0].split(':')[1].strip()
    init_coords = ast.literal_eval(lines[1].split(':')[1].strip())
    goal_coords = ast.literal_eval(lines[2].split(':')[1].strip())
    strategy = lines[3].split(':')[1].strip()
    max_depth = int(lines[4].split(':')[1].strip())

    # Crear instancia del problema
    mapa = Mapa(hdf5_filename)
    problema = Problema(mapa, init_coords[0], init_coords[1], goal_coords[0], goal_coords[1])

    return problema, strategy, max_depth