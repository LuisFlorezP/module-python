import pandas as pd
import matplotlib.pyplot as plt

productos_data = {
    'producto_id': [1, 2, 3, 4, 5],
    'categoria': ['Electrodomésticos', 'Moda', 'Electrodomésticos', 'Moda', 'Libros'],
    'precio': [100, 50, 150, 30, 20]
}

usuarios_data = {
    'usuario_id': [1, 2, 3, 4, 5],
    'nombre': ['Alicia', 'Rosa', 'Carlos', 'Pedro', 'Evelin'],
    'visitas': [10, 20, 15, 5, 8]
}

transacciones_data = {
    'transaccion_id': [1, 2, 3, 4, 5],
    'usuario_id': [1, 2, 1, 3, 4],
    'producto_id': [1, 2, 3, 1, 4],
    'fecha': ['2024-01-01', '2024-01-15', '2024-02-01', '2024-03-01', '2024-03-15']
}

resenas_data = {
    'resena_id': [1, 2, 3, 4, 5],
    'producto_id': [1, 2, 3, 4, 5],
    'calificacion': [5, 4, 3, 2, 5],
    'comentario': ['Great product!', 'Good quality', 'Average', 'Not good', 'Excellent!']
}

df_productos = pd.DataFrame(productos_data)
df_usuarios = pd.DataFrame(usuarios_data)
df_transacciones = pd.DataFrame(transacciones_data)
df_resenas = pd.DataFrame(resenas_data)

df_transacciones['fecha'] = pd.to_datetime(df_transacciones['fecha'])

df = df_transacciones.merge(df_productos, on='producto_id').merge(df_usuarios, on='usuario_id').merge(df_resenas, on='producto_id')

visitas_por_categoria = df.groupby('categoria')['visitas'].sum()
transacciones_por_categoria = df['categoria'].value_counts()
tasa_conversion = transacciones_por_categoria / visitas_por_categoria

plt.figure(figsize=(10, 6))
tasa_conversion.plot(kind='bar')
plt.title('Tasa de conversión por categoría de producto')
plt.xlabel('Categoría')
plt.ylabel('Tasa de conversión')
plt.grid(True)
plt.savefig('Tasa de conversión por categoría de producto.png')
plt.show()

print("Calificación promedio por producto:\n", df_resenas.groupby('producto_id')['calificacion'].mean())
print("Distribución de calificaciones:\n", df_resenas['calificacion'].value_counts())

ventas_mensuales = df_transacciones.set_index('fecha').resample('ME').size()

plt.figure(figsize=(10, 6))
ventas_mensuales.plot(kind='line', marker='o')
plt.title('Tendencia de las ventas mensuales')
plt.xlabel('Mes')
plt.ylabel('Número de ventas')
plt.grid(True)
plt.savefig('Tendencia de las ventas mensuales.png')
plt.show()

plt.figure(figsize=(10, 6))
df_productos.boxplot(column='precio', by='categoria', grid=True)
plt.title('Distribución de precios por categoría de producto')
plt.suptitle('')
plt.xlabel('Categoría')
plt.ylabel('Precio')
plt.savefig('Distribución de precios por categoría de producto.png')
plt.show()