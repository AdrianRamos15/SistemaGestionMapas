# Sistema de Gestión de Mapas y Resolución de Problemas 🗺️

## Descripción General
Este proyecto desarrolla un sistema para procesar mapas geoespaciales almacenados en archivos HDF5 y resolver problemas definidos en el contexto de un espacio de estados. Utilizando Python como lenguaje principal, se implementan módulos y clases que permiten la manipulación de mapas, el modelado de estados y la ejecución de algoritmos de búsqueda.

El sistema está diseñado para ser modular y flexible, permitiendo su extensión a diferentes casos de uso relacionados con datos geográficos y análisis espacial.

---

## Características Principales

1. **Manipulación de Mapas:**
   - Carga de mapas desde archivos HDF5.
   - Operaciones como lectura de valores en coordenadas específicas (UMT) y redimensionamiento de mapas con transformaciones personalizables.

2. **Modelado de Estados y Problemas:**
   - Representación de estados dentro de un espacio definido por el mapa.
   - Generación de sucesores válidos desde un estado inicial.
   - Definición de problemas con estados iniciales y estrategias de búsqueda.

3. **Algoritmos de Búsqueda:**
   - Implementación de búsqueda basada en estrategias como BFS, DFS, A*, y Greedy.
   - Soporte para heurísticas específicas:
     - **Distancia Euclidiana (Heuclidea):** Calcula la distancia geométrica entre un estado y el objetivo.
     - **Distancia Manhattan (Hmanhattan):** Calcula la distancia basada en movimientos ortogonales.

---

## Algoritmos de Búsqueda Implementados
El sistema incluye un algoritmo de búsqueda general con soporte para diferentes estrategias y heurísticas. Este algoritmo:
- Administra una **frontera** de nodos ordenados según la estrategia seleccionada.
- Usa una lista de **estados visitados** para evitar ciclos y reducir la complejidad.
- Permite especificar una profundidad máxima para la poda del árbol de búsqueda.

### Funcionamiento del Algoritmo
1. **Inicialización:**
   - Se crea un nodo inicial con costo, heurística y estrategia definidos.
   - Se calcula la heurística inicial (si aplica) y se inserta el nodo en la frontera.

2. **Expansión de Nodos:**
   - Mientras la frontera no esté vacía y no se haya encontrado la solución:
     - Se toma el nodo con mayor prioridad según la estrategia.
     - Si el nodo representa el objetivo, se termina la búsqueda.
     - Si no, se expanden sus sucesores (calculando costos y heurísticas) y se añaden a la frontera.

3. **Heurísticas Soportadas:**
   - **Heuclidea:**
     ```python
     def heuristica_heuclidea(estado, estado_objetivo):
         dy, dx = estado_objetivo.y, estado_objetivo.x
         y, x = estado.y, estado.x
         return sqrt((dx - x) ** 2 + (dy - y) ** 2)
     ```
   - **Hmanhattan:**
     ```python
     def heuristica_hmanhattan(estado, estado_objetivo):
         dy, dx = estado_objetivo.y, estado_objetivo.x
         y, x = estado.y, estado.x
         return abs(dx - x) + abs(dy - y)
     ```

4. **Resultado:**
   - Si se encuentra solución, se devuelve el camino desde el nodo inicial hasta el objetivo.
   - Si no se encuentra solución, el resultado será un camino vacío.

---

## Componentes Principales

### Clases y Funciones
- **Mapa:** Maneja la carga y manipulación de datos geoespaciales, incluyendo operaciones como `umt_YX` para recuperar valores en coordenadas específicas y `resize` para redimensionar mapas.
- **Estado y Problema:** Modelan configuraciones iniciales y reglas para generar nuevos estados en el contexto del espacio de búsqueda.
- **Frontera y Estados Visitados:** Estructuras que manejan la expansión y validación de nodos durante la búsqueda.
- **Algoritmo de Búsqueda:** Implementa la lógica para explorar el espacio de estados y encontrar soluciones según parámetros definidos.

---

## Configuración
1. **Dependencias:**
   - Instala las dependencias necesarias ejecutando:
     ```bash
     pip install numpy h5py
     ```

2. **Archivos de Entrada:**
   - **Mapas:** Los datos geoespaciales se almacenan en archivos HDF5.
   - **Problemas:** Los problemas se configuran en archivos de texto, como `ejemploExam.txt`.

3. **Parámetros Personalizables:**
   - Estrategias de búsqueda (e.g., BFS, DFS, A*, Greedy).
   - Heurísticas (Heuclidea, Hmanhattan).
   - Profundidad máxima para la poda.

---

## Ejecución
1. Configura los archivos de entrada en el script `main.py`.
2. Ejecuta el script para probar las diferentes funcionalidades:
   ```bash
   python main.py
