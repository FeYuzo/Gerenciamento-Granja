from Services.database import get_db_connection
from Models.Ovo import Ovo
import sqlite3

def incluir_ovo(ovo: Ovo):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("""
            INSERT INTO ovo (id_galinha, categoria, tamanho, tipo)
            VALUES (?, ?, ?, ?)
        """, (
            ovo.id_galinha,
            ovo.categoria,
            ovo.tamanho,
            ovo.tipo_ovo
        ))
        conexao.commit()
        print(f"Ovo inserido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir ovo: {e}")
    finally:
        conexao.close()

def consultar_ovos():
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        query = """
            SELECT 
                o.id_ovo, o.categoria, o.tamanho, o.tipo as tipo_ovo,
                g.id_galinha, g.tipo_galinha as tipo_galinha_nome, g.idade as galinha_idade
            FROM ovo o
            LEFT JOIN galinha g ON o.id_galinha = g.id_galinha
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        ovos = []
        for row in rows:
            ovos.append({
                "id_ovo": row[0], "categoria": row[1], "tamanho": row[2], "tipo_ovo": row[3],
                "id_galinha": row[4], "tipo_galinha": row[5], "galinha_idade": row[6]
            })
        return ovos
    except sqlite3.Error as e:
        print(f"Erro ao consultar ovos: {e}")
        return []
    finally:
        conexao.close()

def consultar_ovo_por_id(id_ovo: int):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        query = """
            SELECT 
                o.id_ovo, o.categoria, o.tamanho, o.tipo as tipo_ovo,
                g.id_galinha, g.tipo_galinha as tipo_galinha_nome, g.idade as galinha_idade
            FROM ovo o
            LEFT JOIN galinha g ON o.id_galinha = g.id_galinha
            WHERE o.id_ovo = ?
        """
        cursor.execute(query, (id_ovo,))
        row = cursor.fetchone()
        if row:
            return {
                "id_ovo": row[0], "categoria": row[1], "tamanho": row[2], "tipo_ovo": row[3],
                "id_galinha": row[4], "tipo_galinha": row[5], "galinha_idade": row[6]
            }
        return None
    except sqlite3.Error as e:
        print(f"Erro ao consultar ovo por ID: {e}")
        return None
    finally:
        conexao.close()

def alterar_ovo(ovo: Ovo):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("""
            UPDATE ovo 
            SET id_galinha = ?, categoria = ?, tamanho = ?, tipo = ?
            WHERE id_ovo = ?
        """, (
            ovo.id_galinha, ovo.categoria, ovo.tamanho,
            ovo.tipo_ovo, ovo.id_ovo
        ))
        conexao.commit()
        print(f"Ovo com ID {ovo.id_ovo} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar ovo: {e}")
    finally:
        conexao.close()

def excluir_ovo(id_ovo: int):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM ovo WHERE id_ovo = ?", (id_ovo,))
        conexao.commit()
        print(f"Ovo com ID {id_ovo} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir ovo: {e}")
    finally:
        conexao.close()