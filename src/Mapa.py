import h5py
import numpy as np
import math



class Mapa:
    def __init__(self, filename):
        self.filename = filename
        self.f = h5py.File(filename, 'r')

        # Obtener una lista de todos los nombres de los datasets en la raiz del archivo
        self.dataset_names = list(self.f['/'].keys())

        # Obtener propiedades de todos los datasets
        self.dataset_properties = {}
        for dataset_name in self.dataset_names:
            self.dataset_properties[dataset_name] = self._load_dataset_properties(dataset_name)

    def _load_dataset_properties(self, dataset_name):
        dataset = self.f['/' + dataset_name]
        properties = {
            'nodata_value': dataset.attrs['nodata_value'],
            'sizeCell': dataset.attrs['cellsize'],
            'dim': dataset.shape,
            'upLeft': (dataset.attrs['yinf'], dataset.attrs['xinf']),
            'downRight': (dataset.attrs['ysup'], dataset.attrs['xsup']),  
        }

        # Almacena las propiedades en el objeto Mapa
        self.nodata_value = properties['nodata_value']
        self.sizeCell = properties['sizeCell']
        self.dim = properties['dim']
        self.upLeft = properties['upLeft']
        self.downRight = properties['downRight']

        return properties


    def umt_YX(self, y, x):
        for dataset_name in self.dataset_names:
            properties = self.dataset_properties[dataset_name]
            up_left = properties['upLeft']
            down_right = properties['downRight']

            # Verifica si las coordenadas están dentro de los límites del dataset, excluyendo los bordes
            if up_left[0] <= y < down_right[0] and up_left[1] <= x < down_right[1]:
                dataset = self.f['/' + dataset_name]
                
                # Ajusta las coordenadas para asegurarse de estar dentro de los límites del dataset
                col = min(max(int((x - up_left[1]) / properties['sizeCell']), 0), properties['dim'][1] - 1)
                row = min(max(int((down_right[0] - y) / properties['sizeCell']), 0), properties['dim'][0] - 1)

                return dataset[row][col]

        return self.dataset_properties[self.dataset_names[0]]['nodata_value']
   
        
    def resize(self, factor, transform, nombre):
        # Calcula las nuevas dimensiones y nuevo tamaño de celda
        new_rows = int(math.ceil(self.dim[0] / factor))
        new_cols = int(math.ceil(self.dim[1] / factor))
        new_celsize = self.sizeCell * factor  

        # Crea un nuevo archivo HDF5
        new_filename = f"{nombre}.hdf5"
        new_f = h5py.File(new_filename, 'w')

        # Recorre todos los datasets originales
        for dataset_name in self.dataset_names:
            dataset = self.f['/' + dataset_name]

            # Crea un nuevo dataset en el archivo HDF5/creo matriz
            new_grid = np.full((new_rows,new_cols),-99999.0)
            
            # Calcula las coordenadas en el dataset original para seleccionar un bloque de celdas que se utilizará para calcular el valor de una celda en el nuevo dataset
            for i in range(new_rows):
                for j in range(new_cols):
                    # Coordenadas en el dataset original que corresponden a la celda actual del nuevo dataset
                    start_row = int(i * factor)  
                    end_row = int(start_row + factor)
                    start_col = int(j * factor)
                    end_col = int(start_col + factor)

                    # Calcula el valor para la nueva celda utilizando la función transform
                    cells = dataset[start_row:end_row, start_col:end_col]
                    new_value = transform(cells)
                    
                    # Asigna el valor al nuevo dataset
                    new_grid[i][j] = new_value
                    
                    
            #Sustituimos todos los NaN por -99999 
            new_grid=np.nan_to_num(new_grid,nan=-99999)
            new_dataset = new_f.create_dataset(f'/{dataset_name}', shape=(new_rows, new_cols), dtype='float64',data=new_grid)

            
            # Actualiza las propiedades del nuevo dataset, incluyendo el nuevo tamaño de celda
            properties = self.dataset_properties[dataset_name]
            new_dataset.attrs['nodata_value'] = properties['nodata_value']
            new_dataset.attrs['cellsize'] = new_celsize
            new_dataset.attrs['xinf'] = properties['upLeft'][1]
            new_dataset.attrs['yinf'] = properties['upLeft'][0]
            new_dataset.attrs['xsup'] = properties['downRight'][1]
            new_dataset.attrs['ysup'] = properties['downRight'][0]
            
        return Mapa(new_filename)