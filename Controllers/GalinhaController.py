from Services.database import get_db_connection
from Models.Galinha import Galinha
import sqlite3

def incluir_galinha(galinha: Galinha):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO galinha (tipo_galinha, idade, data_vacinacao)
            VALUES (?, ?, ?)
        """, (
            galinha.tipo_galinha,
            galinha.idade,
            galinha.data_vacinacao
        ))
        conexao.commit()
        print(f"Galinha do tipo {galinha.tipo_galinha} inserida com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir galinha: {e}")
    finally:
        conexao.close()

def consultar_galinhas():
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT id_galinha, tipo_galinha, idade, data_vacinacao FROM galinha')
        rows = cursor.fetchall()
        galinhas = []
        for row in rows:
            galinhas.append({
                "id_galinha": row[0],
                "tipo_galinha": row[1],
                "idade": row[2],
                "data_vacinacao": row[3]
            })
        return galinhas
    except sqlite3.Error as e:
        print(f"Erro ao consultar galinhas: {e}")
        return []
    finally:
        conexao.close()

def consultar_galinha_por_id(id_galinha: int):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT id_galinha, tipo_galinha, idade, data_vacinacao FROM galinha WHERE id_galinha = ?', (id_galinha,))
        row = cursor.fetchone()
        if row:
            return {
                "id_galinha": row[0],
                "tipo_galinha": row[1],
                "idade": row[2],
                "data_vacinacao": row[3]
            }
        return None
    except sqlite3.Error as e:
        print(f"Erro ao consultar galinha por id: {e}")
        return None
    finally:
        conexao.close()

def alterar_galinha(galinha: Galinha):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            UPDATE galinha 
            SET tipo_galinha = ?, idade = ?, data_vacinacao = ?
            WHERE id_galinha = ?
        """, (
            galinha.tipo_galinha,
            galinha.idade,
            galinha.data_vacinacao,
            galinha.id_galinha
        ))
        conexao.commit()
        print(f"Galinha com id {galinha.id_galinha} alterada com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar galinha: {e}")
    finally:
        conexao.close()

def excluir_galinha(id_galinha: int):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM galinha WHERE id_galinha = ?", (id_galinha,))
        conexao.commit()
        print(f"Galinha com id {id_galinha} excluída com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir galinha: {e}")
    finally:
        conexao.close()
