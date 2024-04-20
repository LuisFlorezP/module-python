# declara el valor de hora constante
valor_hora = 33000

# ciclo para validar que el valor de la hora extra sea mayor a una normal, de lo contrario ingresar nuevamente hasta hacerlo correcto
while True:
    valor_hora_extra = float(input('Valor x hora extra: '))
    if valor_hora_extra > valor_hora:
        break
    print('El valor de la hora extra debe ser mayor al valor de la hora normal')

# pedir las horas trabajadas
horas = float(input('Horas: '))

# calcular las horas extras 
horas_extras = horas - 42 if horas > 42 else 0

# calcular salario a calcular
total = horas * valor_hora if horas_extras == 0 else (valor_hora * 42) + (valor_hora_extra * horas_extras) 

# mostrar valor a pagar
print('Salario del trabajador:', total)