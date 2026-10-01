import pandas as pd 

df = pd.read_csv(r"C:\Users\matheus.sandrade\Downloads\funcionarios.csv")


print(df)


df_funcionarios_com_lucro_ativos = df[(df["lucro"] !=0) & (df["ativo"] == True)]



print(df_funcionarios_com_lucro_ativos)