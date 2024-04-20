import pandas as pd 

tabla = {
    'Posiciones específicas': [
        'Delantero centro', 
        'Extremo derecho', 
        'Extremo izquierdo', 
        'Falso 9', 
        'Medio centro atacante',
        'Medio centro defensivo',
        'Medio centro',
        'Medio derecho',
        'Medio izquierdo',
        'Lateral izquierdo',
        'Lateral derecho',
        'Defensa central',
        'Defensa central derecho',
        'Defensa central izquierdo',
        'Carrilero izquierdo',
        'Carrilero derecho',
        'Portero',
    ],
    'Clasificación': [
        'Delantera', 'Delantera', 'Delantera', 'Delantera', 
        'Medio campo', 'Medio campo', 'Medio campo', 'Medio campo', 'Medio campo', 
        'Defensa', 'Defensa', 'Defensa', 'Defensa', 'Defensa', 'Defensa', 'Defensa', 'Defensa'
    ]
}

data_frame = pd.DataFrame(tabla) 
print('Tabla de posiciones del futbol colombiano 2024:')
print(data_frame)