from Services.database import get_db_connection
from Models.Entreposto_de_ovos import EntrePostoOvos
import sqlite3

def incluir_entreposto_ovos(entreposto: EntrePostoOvos):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO entreposto_ovos (CNPJ, endereco, capacidade_armz, qtd_compra)
            VALUES (?, ?, ?, ?)
        """, (
            entreposto.cnpj,
            entreposto.endereco,
            entreposto.capacidade_armazenamento,
            entreposto.quantidade_compra
        ))
        conexao.commit()
        print(f"Entreposto de Ovos {entreposto.cnpj} inserido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir entreposto de ovos: {e}")
    finally:
        conexao.close()

def consultar_entrepostos_ovos():
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT id_entreposto, CNPJ, endereco, capacidade_armz, qtd_compra FROM entreposto_ovos')
        rows = cursor.fetchall()
        entrepostos = []
        for row in rows:
            entrepostos.append({
                "id_entreposto": row[0],
                "CNPJ": row[1],
                "endereco": row[2],
                "capacidade_armz": row[3],
                "qtd_compra": row[4]
            })
        return entrepostos
    except sqlite3.Error as e:
        print(f"Erro ao consultar entrepostos de ovos: {e}")
        return []
    finally:
        conexao.close()

def consultar_entreposto_ovos_por_id(id_entreposto: int):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT id_entreposto, CNPJ, endereco, capacidade_armz, qtd_compra FROM entreposto_ovos WHERE id_entreposto = ?', (id_entreposto,))
        row = cursor.fetchone()
        if row:
            return {
                "id_entreposto": row[0],
                "CNPJ": row[1],
                "endereco": row[2],
                "capacidade_armz": row[3],
                "qtd_compra": row[4]
            }
        return None
    except sqlite3.Error as e:
        print(f"Erro ao consultar entreposto de ovos por ID: {e}")
        return None
    finally:
        conexao.close()

def alterar_entreposto_ovos(entreposto: EntrePostoOvos):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            UPDATE entreposto_ovos 
            SET CNPJ = ?, endereco = ?, capacidade_armz = ?, qtd_compra = ?
            WHERE id_entreposto = ?
        """, (
            entreposto.cnpj,
            entreposto.endereco,
            entreposto.capacidade_armazenamento,
            entreposto.quantidade_compra,
            entreposto.id_entreposto
        ))
        conexao.commit()
        print(f"Entreposto de Ovos com ID {entreposto.id_entreposto} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar entreposto de ovos: {e}")
    finally:
        conexao.close()

def excluir_entreposto_ovos(id_entreposto: int):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM entreposto_ovos WHERE id_entreposto = ?", (id_entreposto,))
        conexao.commit()
        print(f"Entreposto de Ovos com ID {id_entreposto} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir entreposto de ovos: {e}")
    finally:
        conexao.close()
