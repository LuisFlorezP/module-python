paises = ['Colombia', 'Argentina', 'Mexico']

pais = paises[0]
print(f'País: {pais}')
paises[1] = 'Brazil'
paises.append('Francia')
paises.append('Inglaterra')
paises.remove(paises[0])
paises.remove(paises[-1])
paises.sort()

print('Países preferidos:', paises)