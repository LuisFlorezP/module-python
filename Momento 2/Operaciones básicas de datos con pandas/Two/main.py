import pandas as pd

df = pd.read_csv('./temperatura.csv', sep=';')

# 1
print('\nPrimeras filas:')
print(df.head())

# 2
print('\nValores nulos por columna:', df.isnull().sum())

# 3
print('\nEliminar nulos de Temperatura_3:')
print(df.dropna(subset=['Temperatura_3']))

# 4
print('\nEliminar duplicados de Temperatura_1:')
print(df.drop_duplicates(subset=['Temperatura_1']))

# 5
print('\nTemperaturas mayores a 27 en Temperatura_2:')
print(df[df['Temperatura_2'] > 27]['Temperatura_2'])

# 6
print('\nSumatoria de Temperatura_2:')
print(df['Temperatura_2'].sum())

# 7
print('\nPromedio de Temperatura_3:')
print(df['Temperatura_3'].mean())

# 8
print('\nDescribir estadisticas:')
print(df.describe())

# 9
print('\nTemperaturas iguales a 23.1 en Temperatura_1:', df[df['Temperatura_1'] == 23.1].count()['Temperatura_1'])

# 10
print('\nSortear Temperatura_2 descendentemente:')
print(df['Temperatura_2'].sort_values(ascending=False))