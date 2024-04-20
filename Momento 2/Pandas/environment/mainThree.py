import pandas as pd 

numeros = {
    'a': 100, 
    'b': 200, 
    'c': 300, 
    'd': 400
}
serie = pd.Series(numeros) 
print('Valor de la etiqueta \'b\':', serie.loc['b']) 