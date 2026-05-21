from database import get_db_connection

def criar_tabela_entreposto_ovos():

    conexao = get_db_connection()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS entreposto_ovos (
        id_entreposto       INTEGER PRIMARY KEY AUTOINCREMENT,
        CNPJ                VARCHAR(14) NOT NULL UNIQUE,
        endereco            TEXT NOT NULL,
        capacidade_armz     REAL NOT NULL CHECK (capacidade_armz >= 0),
        qtd_compra          INTEGER
    );
    """)

    conexao.commit()
    conexao.close()
    print("Tabela 'entreposto_ovos' criada com sucesso!")

if __name__ == "__main__":
    criar_tabela_entreposto_ovos()