from database import get_db_connection

def criar_tabela_cliente():
    conexao = get_db_connection()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cliente (
        id_cliente      INTEGER PRIMARY KEY AUTOINCREMENT,
        nome            TEXT NOT NULL,
        telefone        TEXT UNIQUE NOT NULL,
        endereco        TEXT NOT NULL,
        qntd_compra_bandeija      INTEGER,
        observacoes     TEXT
    );
    """)

    conexao.commit()
    conexao.close()
    print("Tabela 'cliente' criada com sucesso!")

if __name__ == "__main__":
    criar_tabela_cliente()