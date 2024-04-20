departamentos_colombia = []

cantidad_usuarios = int(input('Cantidad departamentos: '))

for i in range(1, cantidad_usuarios + 1):
    departamentos_colombia.append(input(f'Departamento N°{i}: '))

departamentos_colombia.reverse()
print('Departamentos ordeados descendentemente: ', departamentos_colombia)
print(f'Últimos departamentos: {departamentos_colombia[-2]}, {departamentos_colombia[-1]}')