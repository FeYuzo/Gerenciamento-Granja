from Services.database import get_db_connection
from Models.Venda import Venda
import sqlite3

def incluir_venda(venda: Venda):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("""
            INSERT INTO venda (codigo, data_venda, qntd_bandeijas_vendidas, qntd_caixas_vendidas, valor_bandeija, valor_caixa, id_cliente, id_entreposto, id_ovo)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            venda.codigo,
            venda.data_venda,
            venda.qntd_bandeijas_vendidas,
            venda.qntd_caixas_vendidas,
            venda.valor_bandeija,
            venda.valor_caixa,
            venda.id_cliente,
            venda.id_entreposto,
            venda.id_ovo
        ))
        conexao.commit()
        print(f"Venda com código {venda.codigo} inserida com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir venda: {e}")
    finally:
        conexao.close()

def consultar_vendas():
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        query = """
            SELECT 
                v.id_venda, v.codigo, v.data_venda, v.qntd_bandeijas_vendidas, v.qntd_caixas_vendidas, v.valor_bandeija, v.valor_caixa,
                c.id_cliente, c.telefone as cliente_telefone,
                e.id_entreposto, e.CNPJ as entreposto_cnpj,
                o.id_ovo, o.tipo as ovo_tipo, o.categoria as ovo_categoria
            FROM venda v
            LEFT JOIN cliente c ON v.id_cliente = c.id_cliente
            LEFT JOIN entreposto_ovos e ON v.id_entreposto = e.id_entreposto
            LEFT JOIN ovo o ON v.id_ovo = o.id_ovo
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        vendas = []
        for row in rows:
            vendas.append({
                "id_venda": row[0], "codigo": row[1], "data_venda": row[2], "qntd_bandeijas_vendidas": row[3], 
                "qntd_caixas_vendidas": row[4], "valor_bandeija": row[5], "valor_caixa": row[6],
                "id_cliente": row[7], "cliente_telefone": row[8],
                "id_entreposto": row[9], "entreposto_cnpj": row[10],
                "id_ovo": row[11], "ovo_tipo": row[12], "ovo_categoria": row[13]
            })
        return vendas
    except sqlite3.Error as e:
        print(f"Erro ao consultar vendas: {e}")
        return []
    finally:
        conexao.close()

def consultar_venda_por_id(id_venda: int):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        query = """
            SELECT 
                v.id_venda, v.codigo, v.data_venda, v.qntd_bandeijas_vendidas, v.qntd_caixas_vendidas, v.valor_bandeija, v.valor_caixa,
                c.id_cliente, c.telefone as cliente_telefone,
                e.id_entreposto, e.CNPJ as entreposto_cnpj,
                o.id_ovo, o.tipo as ovo_tipo, o.categoria as ovo_categoria
            FROM venda v
            LEFT JOIN cliente c ON v.id_cliente = c.id_cliente
            LEFT JOIN entreposto_ovos e ON v.id_entreposto = e.id_entreposto
            LEFT JOIN ovo o ON v.id_ovo = o.id_ovo
            WHERE v.id_venda = ?
        """
        cursor.execute(query, (id_venda,))
        row = cursor.fetchone()
        if row:
            return {
                "id_venda": row[0], "codigo": row[1], "data_venda": row[2], "qntd_bandeijas_vendidas": row[3], 
                "qntd_caixas_vendidas": row[4], "valor_bandeija": row[5], "valor_caixa": row[6],
                "id_cliente": row[7], "cliente_telefone": row[8],
                "id_entreposto": row[9], "entreposto_cnpj": row[10],
                "id_ovo": row[11], "ovo_tipo": row[12], "ovo_categoria": row[13]
            }
        return None
    except sqlite3.Error as e:
        print(f"Erro ao consultar venda por ID: {e}")
        return None
    finally:
        conexao.close()

def alterar_venda(venda: Venda):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("""
            UPDATE venda 
            SET codigo = ?, data_venda = ?, qntd_bandeijas_vendidas = ?, qntd_caixas_vendidas = ?, valor_bandeija = ?, valor_caixa = ?, id_cliente = ?, id_entreposto = ?, id_ovo = ?
            WHERE id_venda = ?
        """, (
            venda.codigo, venda.data_venda, venda.qntd_bandeijas_vendidas, venda.qntd_caixas_vendidas, venda.valor_bandeija,
            venda.valor_caixa, venda.id_cliente, venda.id_entreposto, venda.id_ovo, venda.id_venda
        ))
        conexao.commit()
        print(f"Venda com ID {venda.id_venda} alterada com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar venda: {e}")
    finally:
        conexao.close()

def excluir_venda(id_venda: int):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM venda WHERE id_venda = ?", (id_venda,))
        conexao.commit()
        print(f"Venda com ID {id_venda} excluída com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir venda: {e}")
    finally:
        conexao.close()