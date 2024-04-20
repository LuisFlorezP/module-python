# importar funcionalidad para randoms
import random

# obtener numero random e inicializar variable de proceso
numero_random = random.randint(1, 100)
resultado = False

# pedir al usuario el numero para adivinar por unas máximas 3 veces
for i in range(3):
    numero_usuario = int(input('¿Cuál crees que es mi número secreto?: '))
    if numero_usuario == numero_random:
        resultado = True    
        break
    print('El número secreto es', 'mayor' if numero_random > numero_usuario else 'menor')

# expresar si adivino o no el resultado, además mostrar el número random 
print('\nResultado:', '¡Atinaste!' if resultado else '¡Fallaste!', '\nNúmero secreto:', numero_random)