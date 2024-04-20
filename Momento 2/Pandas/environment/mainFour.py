import pandas as pd 

inicial = int(input('Ingresa el año inicial del rango de ventas: '))
final = int(input('Ingresa el año final del rango de ventas: '))

ventas_pre = {}
ventas_post = {}
for i in range(final - inicial + 1):
    venta = float(input(f'Ingresa las ventas del año {inicial + i}: '))
    ventas_pre.update({f'{final - i}': venta})
    ventas_post.update({f'{final - i}': venta * 0.1})

ventas_pre_serie = pd.Series(ventas_pre)
ventas_post_serie = pd.Series(ventas_post)

print('\nSerie de ventas antes del descuento del 10%:')
print(ventas_pre_serie)
print('\nSerie de ventas despues del descuento del 10%:')
print(ventas_post_serie)