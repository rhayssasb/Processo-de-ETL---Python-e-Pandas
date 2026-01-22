import pandas as pd 

# E -> Extração 
df = pd.read_csv("usuarios.csv") 
print("Bem-vindo!")
print("A seguir, dados que foram extraídos...") 
print(df)

# T-> Transformação
df["Mensagem"] = df.apply(lambda row: f"Olá {row["Nome"]}, sua conta {row["Conta"]} está ativa e vinculada ao cartão {row["Cartao"]}.", axis=1)
print("\nDados transformados:")
print(df[["Nome", "Mensagem"]])


# L-> Load/Carregamento 
df.to_csv("mensagens_usuarios.csv", index=False) 
print("\nArquivo 'mensagens_usuarios.csv' gerado com sucesso!")
