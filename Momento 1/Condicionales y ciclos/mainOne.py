print('BUENOS DÍAS Y BIENVENIDO A LA AGENCIA DE ALQUILER')

valor_hora = float(input('Valor x hora: '))
horas = float(input('Horas: '))

descuento = ((horas - 10) * valor_hora) * 0.2 if horas > 10 else 0
sub_total = horas * valor_hora if descuento == 0 else valor_hora * 10

print('Total a pagar:', sub_total + descuento)