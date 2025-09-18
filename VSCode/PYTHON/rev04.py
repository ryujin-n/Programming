#Grafico

import panda as pd
import matplotlib.pyplot as plt
from IPython.core.display_functions import display
from google.colab import drive

drive.mount('/content/drive')
caminho_planilha = '/content/rev04.xlsx'

try:
    df = pd.read_excel(caminho_planilha)
    print("Dataframe lido com sucesso:")
    display(df.head())

    plt.figure(figsize=(8,6))
    plt.bar(df['Nome'], df['Idade'])
    plt.xlabel('Nome')
    plt.ylabel('Idade')
    plt.title('Idade por Nome')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_planilha}' nao foi encontrado no drive")
except Exception as e:
    print(f"Erro: {e}")
    