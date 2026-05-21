from database import get_db_connection

def criar_tabela_galinha():
  
    conexao = get_db_connection()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS galinha (
        id_galinha      INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo_galinha    TEXT NOT NULL,
        idade           INTEGER NOT NULL, -- Idade em semanas
        data_vacinacao  DATE NOT NULL
    );
    """)

    conexao.commit()
    conexao.close()
    print("Tabela 'galinha' criada com sucesso!")

if __name__ == "__main__":
    criar_tabela_galinha()