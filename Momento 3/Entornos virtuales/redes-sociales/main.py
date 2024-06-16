import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'usuario': ['usuario1', 'usuario2', 'usuario3', 'usuario4', 'usuario5', 'usuario1', 'usuario2', 'usuario3', 'usuario4', 'usuario5'],
    'fecha': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10'],
    'texto': ["This is the first post", "Second post here", "Another post", "Interesting content", "This is great", "More posts", "Social media analysis", "Data science is cool", "Learning Python", "Pandas is powerful"],
    'me_gusta': [10, 20, 30, 40, 50, 15, 25, 35, 45, 55],
    'compartidos': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
}
df = pd.DataFrame(data)

df['fecha'] = pd.to_datetime(df['fecha'])

df['longitud_texto'] = df['texto'].apply(len)

promedios = df.groupby('usuario').agg({
    'me_gusta': 'mean',
    'compartidos': 'mean',
    'longitud_texto': 'mean'
}).reset_index()

plt.figure(figsize=(10, 6))
plt.scatter(df['longitud_texto'], df['me_gusta'])
plt.title('Relación entre la longitud del texto y el número de me gusta')
plt.xlabel('Longitud del Texto')
plt.ylabel('Número de me gusta')
plt.grid(True)
plt.savefig('Relación entre la longitud del texto y el número de me gusta.png')
plt.show()

usuarios_mas_activos = df['usuario'].value_counts().head(10).index

promedios_top10 = promedios[promedios['usuario'].isin(usuarios_mas_activos)]

promedios_top10.set_index('usuario')[['me_gusta', 'compartidos']].plot(kind='bar', figsize=(12, 6))
plt.title('Promedio de me gusta y compartidos por usuario')
plt.legend(title='Métrica')
plt.xlabel('Usuario')
plt.ylabel('Promedio')
plt.grid(axis='y')
plt.savefig('Promedio de me gusta y compartidos por usuario.png')
plt.show()

plt.figure(figsize=(12, 6))
sns.violinplot(x='longitud_texto', y='me_gusta', data=df)
plt.title('Distribución del número de me gusta por la longitud del texto de la publicación')
plt.xlabel('Longitud del texto')
plt.ylabel('Número de me gusta')
plt.grid(True)
plt.savefig('Distribución del número de me gusta por la longitud del texto de la publicación.png')
plt.show()