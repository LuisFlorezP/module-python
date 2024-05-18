import pandas as pd

df = pd.read_csv('./plantilla.csv', sep=',')

cantidad_productos = df[['Producto', 'Cantidad']]
ventas_octubre = df[['Ventas Octubre 9%']].dropna()

print('\nCantidad total de cada producto:')
print(cantidad_productos)
print('\nProducto más vendido en octubre:')
print(df['Producto'][ventas_octubre.idxmax()])
print('\nPrecio total generado por el trimestre:')
print(df['Total Trimestre'].sum())