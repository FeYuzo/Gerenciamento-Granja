import sqlite3
import os

def get_db_connection():

    caminho = os.path.join(os.path.dirname(__file__), '..', 'Granja.db')
    caminho = os.path.abspath(caminho)
    print(f"Tentando conectar ao banco de dados em: {caminho}")


    banco_existe = os.path.exists(caminho)

    conexao = sqlite3.connect(caminho)

 
    if not banco_existe:
        print("Banco de dados 'Granja.db' criado com sucesso!")

    return conexao



if __name__ == "__main__":
    get_db_connection()
