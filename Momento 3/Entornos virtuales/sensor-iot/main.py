import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'tiempo': ['2024-06-01 01:00', '2024-06-01 02:00', '2024-06-01 03:00', '2024-06-01 04:00', '2024-06-02 01:00', '2024-06-02 02:00', '2024-06-02 03:00', '2024-06-02 04:00', '2024-06-03 01:00', '2024-06-03 02:00', '2024-06-03 03:00', '2024-06-03 04:00'],
    'temperatura': [22.5, 23.0, 22.8, 22.9, 21.0, 21.5, 21.7, 21.6, 20.0, 20.5, 20.3, 20.4],
    'humedad': [55, 57, 56, 55, 60, 61, 62, 61, 65, 64, 63, 62],
    'calidad_aire': [30, 32, 31, 33, 28, 29, 27, 28, 25, 24, 23, 22]
}

df = pd.DataFrame(data)

df['tiempo'] = pd.to_datetime(df['tiempo'])

df.set_index('tiempo', inplace=True)

promedios = df.resample('D').mean()

plt.figure(figsize=(12, 6))
plt.plot(promedios.index, promedios['temperatura'], label='Temperatura')
plt.title('Tendencia diaria temperatura')
plt.xlabel('Fecha')
plt.ylabel('Temperatura')
plt.grid(True)
plt.tight_layout()
plt.savefig('Tendencia diaria temperatura.png')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(promedios.index, promedios['humedad'], label='Humedad')
plt.title('Tendencia diaria humedad')
plt.xlabel('Fecha')
plt.ylabel('Humedad')
plt.grid(True)
plt.tight_layout()
plt.savefig('Tendencia diaria humedad.png')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(promedios.index, promedios['calidad_aire'], label='Calidad del Aire')
plt.title('Tendencia diaria calidad del aire')
plt.xlabel('Fecha')
plt.ylabel('Calidad del Aire')
plt.grid(True)
plt.tight_layout()
plt.savefig('Tendencia diaria calidad del aire.png')
plt.show()

correlation_matrix = promedios.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap de correlaciones entre métricas')
plt.savefig('Heatmap de correlaciones entre métricas.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.regplot(x='temperatura', y='humedad', data=promedios, line_kws={'color':'red'})
plt.title('Relación entre temperatura y humedad')
plt.xlabel('Temperatura')
plt.ylabel('Humedad')
plt.grid(True)
plt.tight_layout()
plt.savefig('Relación entre temperatura y humedad.png')
plt.show()