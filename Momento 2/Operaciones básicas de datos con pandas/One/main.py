import pandas as pd

df = pd.read_csv('./ventas.csv', sep=',')

print('\nPrimeras filas del DataFrame:') 
print(df.head())

print('\nNumero de filas y columnas:', df.shape)

null_counts = df.isnull().sum()
print('\nCantidad de valores nulos por columna:')
print(null_counts)

total_ventas = df['Ventas'].sum()
print('\nSuma total de ventas:', total_ventas)

promedio_por_mes = df.groupby('Mes')['Ventas'].mean()
print('\nPromedio de ventas por mes:')
print(promedio_por_mes)

ventas_por_producto = df.groupby('Producto')['Ventas'].sum()

producto_mas_vendido = ventas_por_producto.idxmax()
cantidad_total_vendida = ventas_por_producto.max()

print('\nProducto más vendido:', producto_mas_vendido)
print('Cantidad total vendida de ese producto:', cantidad_total_vendida)

df_electronica = df[df['Categoria'] == 'Electronica']

print('\nDataFrame con ventas de productos en la categoria \'Electronica\':')
print(df_electronica)

df_electronica.to_csv('Ventas_electronica.csv', index=False)

print('\nArchivo \'Ventas_electronica.csv\' guardado exitosamente.')