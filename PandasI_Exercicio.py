import pandas as pd

dados = {
    "nome": ["Maycon", "Thayna", "Marcos"],
    "cargo": ["Pedagogo", "Quimica", "Biotecnologista"],
    "salario": [5000, 7000, 10000],
}

df = pd.DataFrame(dados)
print(df)