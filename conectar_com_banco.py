import mysql.connector
def conectar_bd():
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="123456",
            database="Cozzinhe"
        )
        print("Conexão bem-sucedida ao banco de dados MySQL")
        return conexao
    except mysql.connector.Error as erro:
        print("Erro ao conectar ao banco de dados MySQL:", erro)
        return None