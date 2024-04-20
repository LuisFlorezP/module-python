import pandas as pd 

tabla = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'Ventas': [100, 150, 200, 180, 220]
}

data_frame = pd.DataFrame(tabla) 
print('Tabla:')
print(data_frame)

total_ventas = 0
total_ventas = 0
for i in range(3):
    total_ventas = total_ventas + tabla['Ventas'][i]

print(f'\nTotal ventas primer trimestre (Enero, Febrero, Marzo): ${total_ventas}')