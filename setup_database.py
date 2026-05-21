import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), 'Services'))

from tabela_cliente import criar_tabela_cliente
from tabela_entreposto_ovo import criar_tabela_entreposto_ovos
from tabela_funcionarios import criar_tabela_funcionario
from tabela_galinhas import criar_tabela_galinha
from tabela_ovos import criar_tabela_ovo
from tabela_ranchos import criar_tabela_rancho
from tabela_venda import criar_tabela_venda

def setup_all_tables():

    print("Iniciando a criação das tabelas...")
    
    criar_tabela_cliente()
    criar_tabela_funcionario()
    criar_tabela_galinha()
    

    criar_tabela_rancho()
    criar_tabela_ovo()
    criar_tabela_entreposto_ovos()
    
   
    criar_tabela_venda()
    
    print("Criação de todas as tabelas concluída com sucesso!")

if __name__ == "__main__":
   
    db_path = 'Granja.db'
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Banco de dados '{db_path}' antigo removido.")
        
    setup_all_tables()
