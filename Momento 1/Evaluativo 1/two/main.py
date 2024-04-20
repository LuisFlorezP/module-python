# pedir numero a validar si es primo
numero = int(input('Numero a validar posible primo: '))

# ciclo para ver si es realmente un numero primo o no
count = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        count += 1 

# imprimir si es numero primo o no
print('Número primo:', 'NO' if count > 2 else 'SI')