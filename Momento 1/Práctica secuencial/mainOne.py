# MODULO = 4 SEG (35%) - 3 PAR (20% C/U) - AUTO/COE (5%)

print('BUENOS DÍAS Y BIENVENIDO A LA CALCULADORA')

print('MODULO N°1:')
nota_seguimientos = float(input('Seguimiento N°1: '))
nota_seguimientos += float(input('Seguimiento N°2: '))
nota_seguimientos += float(input('Seguimiento N°3: '))
nota_seguimientos += float(input('Seguimiento N°4: '))

nota_paciales = float(input('Parcial N°1: '))
nota_paciales += float(input('Parcial N°2: '))
nota_paciales += float(input('Parcial N°3: '))

nota_auto_coe = float(input('Auto: '))
nota_auto_coe += float(input('Coe: '))

definitiva_general = ((nota_seguimientos / 4) * 0.35) + ((nota_paciales / 3) * 0.60) + ((nota_auto_coe / 2) * 0.05)

print('MODULO N°2:')
nota_seguimientos = float(input('Seguimiento N°1: '))
nota_seguimientos += float(input('Seguimiento N°2: '))
nota_seguimientos += float(input('Seguimiento N°3: '))
nota_seguimientos += float(input('Seguimiento N°4: '))

nota_paciales = float(input('Parcial N°1: '))
nota_paciales += float(input('Parcial N°2: '))
nota_paciales += float(input('Parcial N°3: '))

nota_auto_coe = float(input('Auto: '))
nota_auto_coe += float(input('Coe: '))

definitiva_general += ((nota_seguimientos / 4) * 0.35) + ((nota_paciales / 3) * 0.60) + ((nota_auto_coe / 2) * 0.05)

print('MODULO N°3:')
nota_seguimientos = float(input('Seguimiento N°1: '))
nota_seguimientos += float(input('Seguimiento N°2: '))
nota_seguimientos += float(input('Seguimiento N°3: '))
nota_seguimientos += float(input('Seguimiento N°4: '))

nota_paciales = float(input('Parcial N°1: '))
nota_paciales += float(input('Parcial N°2: '))
nota_paciales += float(input('Parcial N°3: '))

nota_auto_coe = float(input('Auto: '))
nota_auto_coe += float(input('Coe: '))

definitiva_general += ((nota_seguimientos / 4) * 0.35) + ((nota_paciales / 3) * 0.60) + ((nota_auto_coe / 2) * 0.05)

print(f"NOTA FINAL MODULOS: {definitiva_general / 3}")