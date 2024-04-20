import pandas as pd 

def aprobados(notas):
    serie_notas = pd.Series(notas)
    serie_notas = serie_notas.sort_values(ascending=False)

    return serie_notas[serie_notas >= 3.5]

notas = {
    'n1': 4.5,
    'n2': 5,
    'n3': 1.2,
    'n4': 3,
    'n5': 4.2,
}

print('Notas aprobadas ordenadas de mayor a menor:')
print(aprobados(notas))