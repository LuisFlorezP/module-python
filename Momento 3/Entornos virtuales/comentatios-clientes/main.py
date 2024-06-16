import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
from wordcloud import WordCloud

data = {
    'comentario': [
        "Great product, really enjoyed it!",
        "Terrible experience, would not recommend.",
        "It was okay, nothing special.",
        "Excellent quality, will buy again.",
        "Not worth the price.",
        "Absolutely fantastic!",
        "Poor quality, broke after one use.",
        "Loved it, altaly recommend.",
        "It's decent, but I've seen better.",
        "Worst product I've ever bought."
    ],
    'calificacion': [5, 1, 3, 5, 2, 5, 1, 5, 3, 1],
    'fecha': ['2024-01-15', '2024-02-20', '2024-03-05', '2024-04-25', '2024-05-14', '2024-06-30', '2024-07-12', '2024-08-21', '2024-09-10', '2024-10-04']
}

df = pd.DataFrame(data)
df['fecha'] = pd.to_datetime(df['fecha'])

def calcular_sentimiento(comentario):
    analysis = TextBlob(comentario)
    if analysis.sentiment.polarity > 0: return 'positive'
    elif analysis.sentiment.polarity < 0: return 'negative'
    else: return 'neutral'

df['sentimiento'] = df['comentario'].apply(calcular_sentimiento)
df['month'] = df['fecha'].dt.to_period('M')
sentimientos_mes = df.groupby(['month', 'sentimiento']).size().unstack(fill_value=0)

plt.figure(figsize=(12, 6))
sentimientos_mes.plot(kind='line', marker='o')
plt.title('Tendencia mensual de sentimientos')
plt.legend(title='Sentimiento')
plt.xlabel('Mes')
plt.ylabel('Cantidad de comentarios')
plt.grid(True)
plt.tight_layout()
plt.savefig('Tendencia mensual de sentimientos.png')
plt.show()

df['categoria'] = pd.cut(df['calificacion'], bins=[0, 2, 3, 5], labels=['baja', 'media', 'alta'])

alta_calificaciones = df[df['categoria'] == 'alta']
baja_calificaciones = df[df['categoria'] == 'baja']

sentimiento_distribution = pd.concat([
    alta_calificaciones['sentimiento'].value_counts(),
    baja_calificaciones['sentimiento'].value_counts()
], axis=1, keys=['Altas', 'Bajas']).fillna(0)

sentimiento_distribution.plot(kind='bar', figsize=(10, 6))
plt.title('Distribución de sentimientos para calificaciones')
plt.xlabel('Sentimiento')
plt.ylabel('Cantidad de Comentarios')
plt.tight_layout()
plt.savefig('Distribución de sentimientos para calificaciones.png')
plt.show()

comentarios_positivos = ' '.join(df[df['sentimiento'] == 'positive']['comentario'])
comentarios_negativos = ' '.join(df[df['sentimiento'] == 'negative']['comentario'])

wordcloud_positive = WordCloud(width=800, height=400, background_color='white').generate(comentarios_positivos)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_positive, interpolation='bilinear')
plt.axis('off')
plt.title('Nube de palabras positivas')
plt.savefig('Nube de palabras positivas.png')
plt.show()

wordcloud_negative = WordCloud(width=800, height=400, background_color='white').generate(comentarios_negativos)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_negative, interpolation='bilinear')
plt.axis('off')
plt.title('Nube de palabras negativos')
plt.savefig('Nube de palabras negativos.png')
plt.show()