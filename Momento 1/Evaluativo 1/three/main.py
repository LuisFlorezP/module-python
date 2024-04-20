# pedir el primer y segundo nombre a validar
primer_nombre = input('Primer nombre: ')
segundo_nombre = input('Segundo nombre: ')

# validar si tienen misma longitud
misma_longitud = True if len(primer_nombre) == len(segundo_nombre) else False

# validar si tienen misma inicial
mismo_inicio = True if primer_nombre[0] == segundo_nombre[0] else False

# imprimir si se cumplen las condiciones o si no coinciden
if mismo_inicio and misma_longitud:
    print('Los nombres comienzan con la misma letra y la longitud de estos')
else:
    print('No coinciden')