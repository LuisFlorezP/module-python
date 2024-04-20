import pandas as pd 

tabla = {
    'Nombre': ['Juan', 'Maria', 'Pedro', 'Sandra'],
    'Edad': [40, 25, 47, 28],
    'Ciudad': ['Bogotá', 'Medellín', 'Cali', 'Armenia']
}

data_frame = pd.DataFrame(tabla) 
print('Tabla:')
print(data_frame)