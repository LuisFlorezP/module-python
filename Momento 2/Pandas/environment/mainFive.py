import pandas as pd 

def calculos_notas(notas):
    resultados = {}
    series = pd.Series(notas)
    resultados.update({
        'nota_maxima': series.max(), 
        'nota_minima': series.min(), 
        'nota_media': series.mean(), 
        'desviacion_tipica': series.std()
    })
    return resultados

notas = {
    'n1': 5,
    'n2': 4.5,
    'n3': 4.2,
    'n4': 3,
    'n5': 2.2,
}

print('Resultados:')
print(calculos_notas(notas))