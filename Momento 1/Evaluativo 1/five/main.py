dinero = float(input('Cuánto dinero?: '))

while True:
    dias = int(input('Cuántos días?: '))
    if dias >= 90 and dias < 720:
        break
    print('Deben ser mayor a 3 meses (90 días) y menor a 2 años (720 días)')

if dias == 90:
    interes = 3.14
elif dias > 90 and dias <= 180:
    interes = 4.85
elif dias > 180 and dias <= 360:
    interes = 5.75
else:
    while True:
        interes = float(input('Ingresar el porcentaje decimal o entero del interez en el rango de 361-720 días: '))
        if interes > 5.75:
            break
        print('El porcentaje debería ser mayor al anterior rango en este caso de 181-360 días')

print('Valor ganado por el usuario:', (dinero + (dinero * interes)))