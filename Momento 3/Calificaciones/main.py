import matplotlib.pyplot as plt 
import pandas as pd

calificaciones = {
    'Submodulo1': [4, 5, 2.2, 3.1, 5],
    'Submodulo2': [4.0, 2.5, 4.7, 2.8, 1],
    'Submodulo3': [3, 4.1, 3, 1.8, 4.8],
    'Submodulo4': [2.1, 3.9, 4.4, 5, 1.1]
}

data_frame = pd.DataFrame(calificaciones) 
notas_maximas = data_frame.max()
notas_minimas = data_frame.min()
notas_medias = data_frame.mean()

print('\nMáximos:')
print(notas_maximas)
print('\nMínimos:')
print(notas_minimas)
print('\nMedias:')
print(notas_medias)

fig, ax = plt.subplots(3, 1, figsize=(5, 5))

ax[0].bar(notas_maximas.index, notas_maximas.values, color='blue')
ax[0].set_title('Máximos de cada submódulo')
ax[0].set_ylabel('Calificación')
ax[0].set_xlabel('Submódulo')

ax[1].bar(notas_minimas.index, notas_minimas.values, color='green')
ax[1].set_title('Mínimos de cada submódulo')
ax[1].set_ylabel('Calificación')
ax[1].set_xlabel('Submódulo')

ax[2].bar(notas_medias.index, notas_medias.values, color='red')
ax[2].set_title('Medias de cada submódulo')
ax[2].set_ylabel('Calificación')
ax[2].set_xlabel('Submódulo')

plt.tight_layout()
plt.show()

fig, ax = plt.subplots(1, 3, figsize=(5, 5))

ax[0].pie(notas_maximas, labels=notas_maximas.index, autopct='%1.1f%%', startangle=140)
ax[0].set_title('Distribución de máximos')

ax[1].pie(notas_minimas, labels=notas_minimas.index, autopct='%1.1f%%', startangle=140)
ax[1].set_title('Distribución de mínimos')

ax[2].pie(notas_medias, labels=notas_medias.index, autopct='%1.1f%%', startangle=140)
ax[2].set_title('Distribución de medias')

plt.tight_layout()
plt.show()