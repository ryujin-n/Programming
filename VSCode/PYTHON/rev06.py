#planilha
import pandas as pd

dados = {
    'Nome': ['Antonio', 'Pedro','Maria'],
    'Idade': [30,24,53],
    'Cidade': ['SP','RJ','BH']
}
df = pd.DataFrame(data=dados)
nome_arquivo = 'rev04.xlsx'
df.to_excel(nome_arquivo, index=False)
print(f"Planilha de pesquisa: {nome_arquivo}")
