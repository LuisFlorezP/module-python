import matplotlib.pyplot as plt
import pandas as pd

def condicion_operacion(row):
    if row['tipo_de_transaccion'] == 'Depósito': return row['saldo_final'] - row['cantidad']
    else: return row['saldo_final'] + row['cantidad']

data = {
    "usuario": ["Pedro", "Pedro", "Pedro", "María", "María", "Alejandra", "Alejandra", "Alejandra", "Carlos", "Carlos"],
    "cantidad": [100, 200, 50, 300, 150, 75, 90, 125, 200, 300],
    "fecha": ["2024-01-01", "2024-01-03", "2024-01-05", "2024-01-07", "2024-01-09", "2024-01-11", "2024-01-13", "2024-01-15", "2024-01-17", "2024-01-19"],
    "tipo_de_transaccion": ["Depósito", "Retiro", "Depósito", "Depósito", "Retiro", "Depósito", "Retiro", "Depósito", "Depósito", "Retiro"],
    "saldo_final": [1500, 1300, 1350, 1600, 1450, 1300, 1210, 1335, 1550, 1250]
}
df = pd.DataFrame(data)

df['fecha'] = pd.to_datetime(df['fecha'])

df['saldo_diario'] = df.apply(condicion_operacion, axis=1)

saldo_promedio_diario = df.groupby('usuario')['saldo_diario'].mean()
total_depositos = df.loc[df['tipo_de_transaccion'] == 'Depósito'].groupby('usuario')['cantidad'].sum()
total_retiros = df.loc[df['tipo_de_transaccion'] == 'Retiro'].groupby('usuario')['cantidad'].sum()

usuarios_top5 = df.groupby('usuario').size().sort_values(ascending=False).head(5).index
saldo_promedio_diario_top5 = saldo_promedio_diario.loc[usuarios_top5]
total_depositos_top5 = total_depositos.loc[usuarios_top5]
total_retiros_top5 = total_retiros.loc[usuarios_top5]

plt.figure(figsize=(10, 6))
for usuario in saldo_promedio_diario_top5.index:
    plt.plot(df[df['usuario'] == usuario]['fecha'], df[df['usuario'] == usuario]['saldo_diario'], label=usuario, marker='o')
plt.title('Evolución del saldo Promedio diario para Top 5 usuarios con más transacciones')
plt.legend(title='Usuario')
plt.xlabel('Fecha')
plt.ylabel('Saldo promedio diario')
plt.grid(True)
plt.tight_layout()
plt.savefig('Evolución del saldo Promedio diario para Top 5 usuarios con más transacciones.png')
plt.show()

plt.figure(figsize=(10, 6))
ancho_barras = 0.2
index = range(len(total_depositos_top5))
plt.bar(index, total_depositos_top5, width=ancho_barras, label='Depósitos')
plt.bar([i + ancho_barras for i in index], total_retiros_top5, width=ancho_barras, label='Retiros')
plt.title('Total de depósitos y retiros para Top 5 usuarios con más transacciones')
plt.legend(title='Comparación')
plt.xlabel('Usuario')
plt.ylabel('Cantidad')
plt.grid(True)
plt.tight_layout()
plt.xticks([i + ancho_barras / 2 for i in index], total_depositos_top5.index)
plt.savefig('Total de depósitos y retiros para Top 5 usuarios con más transacciones.png')
plt.show()