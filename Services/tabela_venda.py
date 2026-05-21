from database import get_db_connection

def criar_tabela_venda():

    conexao = get_db_connection()
    cursor = conexao.cursor()

 
    cursor.execute("PRAGMA foreign_keys = ON;")

  
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS venda (
        id_venda                INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo                  TEXT NOT NULL UNIQUE,
        data_venda              TEXT NOT NULL,
        qntd_bandeijas_vendidas INTEGER NOT NULL CHECK (qntd_bandeijas_vendidas >= 0),
        qntd_caixas_vendidas    INTEGER NOT NULL CHECK (qntd_caixas_vendidas >= 0),
        valor_bandeija          REAL NOT NULL CHECK (valor_bandeija >= 0),
        valor_caixa             REAL NOT NULL CHECK (valor_caixa >= 0),
        id_cliente              INTEGER NOT NULL,
        id_entreposto           INTEGER NOT NULL,
        id_ovo                  INTEGER NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
        FOREIGN KEY (id_entreposto) REFERENCES entreposto_ovos(id_entreposto),
        FOREIGN KEY (id_ovo) REFERENCES ovo(id_ovo)
    );
    """)

    conexao.commit()
    conexao.close()
    print("Tabela 'venda' criada com sucesso e verificação de chave estrangeira ativada!")

if __name__ == "__main__":
    criar_tabela_venda()
