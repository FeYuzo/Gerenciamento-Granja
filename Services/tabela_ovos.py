from database import get_db_connection

def criar_tabela_ovo():

    conexao = get_db_connection()
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ovo (
        id_ovo          INTEGER PRIMARY KEY AUTOINCREMENT,
        id_galinha      INTEGER NOT NULL,
        categoria       TEXT NOT NULL,
        tamanho         TEXT NOT NULL,
        tipo            TEXT NOT NULL,
        FOREIGN KEY (id_galinha) REFERENCES galinha(id_galinha)
    );
    """)

    conexao.commit()
    conexao.close()
    print("Tabela 'ovo' criada com sucesso e verificação de chave estrangeira ativada!")

if __name__ == "__main__":
    criar_tabela_ovo()