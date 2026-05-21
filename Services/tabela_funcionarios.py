from database import get_db_connection

def criar_tabela_funcionario():

    conexao = get_db_connection()
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionario (
        id_funcionario  INTEGER PRIMARY KEY AUTOINCREMENT,
        CPF             TEXT NOT NULL UNIQUE,
        nome            TEXT NOT NULL,
        endereco        TEXT NOT NULL,
        telefone        TEXT UNIQUE NOT NULL,  
        RG              INTEGER NOT NULL,  
        email           TEXT NOT NULL
    );
    ''')

    conexao.commit()
    conexao.close()
    print("Tabela 'funcionario' criada com sucesso!")

if __name__ == "__main__":
    criar_tabela_funcionario()