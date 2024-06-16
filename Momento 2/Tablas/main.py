import pandas as pd

# df = pd.read_csv('./file_data.csv', sep=';')

# print(df)
# print()

# df = df.dropna(subset=['Salario Mensual'])
# df = df.dropna(subset=['Departamento'])
# df = df.dropna(subset=['Apellido'])
# df = df.drop_duplicates(subset=['Nombre'], )
# print(df)
# print()

# my = df[df['Edad'] > 40]
# print(my[['Nombre', 'Salario Mensual']])
# print()

# df['Salario Anual'] = df['Salario Mensual'] * 12
# print(df[['Nombre', 'Salario Anual']])
# print()

# ventas = df[df['Departamento'] == 'Ventas']
# print(ventas)
# print()

# myN = df[(df['Edad']>40) & (df['Nombre']=='Andrea')]

# print(myN)
# print()


s = pd.Series({'Maematcas': 3.5, 'Sociales': 3.8, 'programacion': 2.3}) 

print(s.sort_values()) 
print(s.sort_index(ascending = False)) 