palabra = input('Ingresar palabra: ')

count = 0
for letra in palabra.lower():
    if letra in ['a', 'e', 'i', 'o', 'u']:
        count = count + 1

print(f' - Palabra: {palabra}.\n - Cantidad vocales: {count}')