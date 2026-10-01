#CRIE O DATAFRAME A PARTIR DO DICIONARIO E FAÇA OS SEGUINTES FILTROS:
#FUNCIONARIOS COM SALARIO MAIOR QUE 3000.00
#FUNCIONARIOS COM O CARGO DE VENDEDO

import pandas as pd

dicionario = {"nome": ["Geronimo", "martha", "patroclos", "tiberios", "janaina", "mercedes"], 
              "cargo": ["gerente", "gerente", "vendedor", "secretario", "vendedora", "vendedor"], 
              "salario": [9600.56, 9600.56, 2600.90, 4500.45, 2600.90, 2600.90]}

df = pd.DataFrame(dicionario)

print(df[df["salario"] > 3000.00])

print(df[df["cargo"] == "vendedor"])

print(df[(df["cargo"] == "vendedor") | (df["cargo"] == "vendedora")])
