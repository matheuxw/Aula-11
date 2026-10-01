#CRIE UM DATAFRAME COM OS DADOS DO ARQUIVO FUNCIONARIOS.CSV E FILTRE:
#TODOS OS FUNCIONARIOS ATIVOS NO DEPARTAMENTO DE VENDAS 
#TODOS OS FUNCIONARIOS ATIVOS COM LUCRO MAIOR QUE 5000
#TODOS OS FUNCIONARIOS INATIVOS 
#CADA FILTRO TERA QUE SER SALVO EM UMA VARIAVEL
#EXPORTAR CADA FILTRO PARA UM ARQUIVO CSV

import pandas as pd

df = pd.read_csv("funcionarios.csv")

ativos_vendas = df[(df["ativo"]) & (df["departamento"] == "Vendas")]

ativos_lucro_alto = df[(df["ativo"]) & (df["lucro"] > 5000)]

inativos = df[~df["ativo"]]

ativos_vendas.to_csv("ativos_vendas.csv", index=False)
ativos_lucro_alto.to_csv("ativos_lucro_alto.csv", index=False)
inativos.to_csv("inativos.csv", index=False)

print(ativos_vendas)
print(ativos_lucro_alto)
print(inativos)