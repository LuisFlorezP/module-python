import requests
import os
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request

def saveFig(directorio_destino, nombre_archivo):
    if not os.path.exists(directorio_destino): os.makedirs(directorio_destino)

    ruta_destino = os.path.join(directorio_destino, nombre_archivo)
    plt.savefig(ruta_destino)

def runProject():
    data = requests.get("https://api.github.com/search/repositories?q=stars:>10000").json()

    df = pd.json_normalize(data['items'])

    print('DataFrame - Head():')
    print(df.head())

    print('DataFrame - Info():')
    print(df.info())

    print('DataFrame - Describe():')
    print(df.describe())

    df = df[['name', 'stargazers_count', 'language', 'forks_count', 'open_issues_count']]

    df = df.dropna()

    df['stargazers_count'] = df['stargazers_count'].astype(int)
    df['forks_count'] = df['forks_count'].astype(int)
    df['open_issues_count'] = df['open_issues_count'].astype(int)

    top_10 = df.nlargest(10, 'stargazers_count')
    plt.figure(figsize=(10, 5))
    plt.bar(top_10['name'], top_10['stargazers_count'], color='skyblue')
    plt.title('Top 10 repositorios de GitHub con mas estrellas')
    plt.xlabel('Nombre de repositorio')
    plt.ylabel('Estrellas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    saveFig('./static', 'top_10_repositories.png')

    plt.figure(figsize=(10, 5))
    plt.scatter(df['stargazers_count'], df['forks_count'], alpha=0.5)
    plt.xlabel('Estrellas')
    plt.ylabel('Sincronización')
    plt.title('Stars vs Forks')
    plt.tight_layout()
    saveFig('./static', 'stars_vs_forks.png')

app = Flask(__name__)

@app.route('/')
def index():
    result = "Resultado de tu script"
    runProject()
    return render_template('./index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)