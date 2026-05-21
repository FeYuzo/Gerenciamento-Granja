from Services.database import get_db_connection
from Models.Rancho import Rancho
import sqlite3

def incluir_rancho(rancho: Rancho):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("""
            INSERT INTO rancho (id_galinha, numeracao, gastos, producao)
            VALUES (?, ?, ?, ?)
        """, (
            rancho.id_galinha,
            rancho.numeracao,
            rancho.gastos,
            rancho.producao
        ))
        conexao.commit()
        print(f"Rancho inserido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir rancho: {e}")
    finally:
        conexao.close()

def consultar_ranchos():
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        query = """
            SELECT 
                r.id_rancho, r.numeracao, r.gastos, r.producao,
                g.tipo_galinha, g.idade as galinha_idade
            FROM rancho r
            LEFT JOIN galinha g ON r.id_galinha = g.id_galinha
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        ranchos = []
        for row in rows:
            ranchos.append({
                "id_rancho": row[0], "numeracao": row[1], "gastos": row[2], "producao": row[3],
                "tipo_galinha": row[4], "galinha_idade": row[5]
            })
        return ranchos
    except sqlite3.Error as e:
        print(f"Erro ao consultar ranchos: {e}")
        return []
    finally:
        conexao.close()

def consultar_rancho_por_id(id_rancho: int):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        query = """
            SELECT 
                r.id_rancho, r.numeracao, r.gastos, r.producao,
                g.tipo_galinha, g.idade as galinha_idade
            FROM rancho r
            LEFT JOIN galinha g ON r.id_galinha = g.id_galinha
            WHERE r.id_rancho = ?
        """
        cursor.execute(query, (id_rancho,))
        row = cursor.fetchone()
        if row:
            return {
                "id_rancho": row[0], "numeracao": row[1], "gastos": row[2], "producao": row[3],
                "tipo_galinha": row[4], "galinha_idade": row[5]
            }
        return None
    except sqlite3.Error as e:
        print(f"Erro ao consultar rancho por ID: {e}")
        return None
    finally:
        conexao.close()

def alterar_rancho(rancho: Rancho):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("""
            UPDATE rancho 
            SET id_galinha = ?, numeracao = ?, gastos = ?, producao = ?
            WHERE id_rancho = ?
        """, (
            rancho.id_galinha, rancho.numeracao, rancho.gastos,
            rancho.producao, rancho.id_rancho
        ))
        conexao.commit()
        print(f"Rancho com ID {rancho.id_rancho} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar rancho: {e}")
    finally:
        conexao.close()

def excluir_rancho(id_rancho: int):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM rancho WHERE id_rancho = ?", (id_rancho,))
        conexao.commit()
        print(f"Rancho com ID {id_rancho} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir rancho: {e}")
    finally:
        conexao.close()