codigo_empleado = input('Código empleado: ')
valor_hora = float(input('Valor x hora: '))
horas = float(input('Horas en la semana: '))

incremento = ((horas - 48) * valor_hora) * 0.35 if horas > 48 else 0

print(f'Código empleado: {codigo_empleado}\nTotal a pagar:', (horas * valor_hora) + incremento)