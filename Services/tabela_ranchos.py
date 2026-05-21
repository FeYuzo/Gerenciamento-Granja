from database import get_db_connection

def criar_tabela_rancho():

    conexao = get_db_connection()
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rancho (
        id_rancho       INTEGER PRIMARY KEY AUTOINCREMENT,
        id_galinha      INTEGER NOT NULL,
        numeracao       INTEGER NOT NULL,
        gastos          REAL CHECK (gastos >= 0),
        producao        INTEGER,
        FOREIGN KEY (id_galinha) REFERENCES galinha(id_galinha)
    );
    """)

    conexao.commit()
    conexao.close()
    print("Tabela 'rancho' criada com sucesso e verificação de chave estrangeira ativada!")

if __name__ == "__main__":
    criar_tabela_rancho()