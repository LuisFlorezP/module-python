import pandas as pd

df = pd.read_csv('./yarleanspuntocoom.csv', sep=',')

print('\nDataFrame:')
print(df)

print('\nNombre completo:')
print(df['Nombre completo'])

print('\nEdad:')
print(df['Edad'])

print('\nCargo:')
print(df['Cargo'])

print('\nSalario:')
print(df['Salario'])

print('\nSede:')
print(df['Sede'])

print('\nSede(s) que tiene(n) 3 chefs y 5 meseros:')
sedes = df.groupby('Sede').apply(lambda x: (x['Cargo'] == 'Chef').sum() == 3 and (x['Cargo'] == 'Mesero').sum() == 5)
print(sedes[sedes].index.tolist())

print('\nTotal de salarios por sede:')
print(df.groupby('Sede')['Salario'].sum())

print('\nPromedio de salarios:')
print(df['Salario'].mean())

print('\nTotal de salarios:')
print(df['Salario'].sum())