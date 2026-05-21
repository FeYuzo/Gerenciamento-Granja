from Services.database import get_db_connection
from Models.Funcionario import Funcionario
import sqlite3

def incluir_funcionario(funcionario: Funcionario):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO funcionario (CPF, nome, endereco, telefone, RG, email)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            funcionario.CPF,
            funcionario.nome,
            funcionario.endereco,
            funcionario.telefone,
            funcionario.rg,
            funcionario.email
        ))
        conexao.commit()
        print(f"Funcionário com CPF {funcionario.CPF} inserido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir funcionário: {e}")
    finally:
        conexao.close()

def consultar_funcionarios():
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT id_funcionario, CPF, nome, endereco, telefone, RG, email FROM funcionario')
        rows = cursor.fetchall()
        funcionarios = []
        for row in rows:
            funcionarios.append({
                "id_funcionario": row[0],
                "CPF": row[1],
                "nome": row[2],
                "endereco": row[3],
                "telefone": row[4],
                "RG": row[5],
                "email": row[6]
            })
        return funcionarios
    except sqlite3.Error as e:
        print(f"Erro ao consultar funcionários: {e}")
        return []
    finally:
        conexao.close()

def consultar_funcionario_por_id(id_funcionario: int):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT id_funcionario, CPF, nome, endereco, telefone, RG, email FROM funcionario WHERE id_funcionario = ?', (id_funcionario,))
        row = cursor.fetchone()
        if row:
            return {
                "id_funcionario": row[0],
                "CPF": row[1],
                "nome": row[2],
                "endereco": row[3],
                "telefone": row[4],
                "RG": row[5],
                "email": row[6]
            }
        return None
    except sqlite3.Error as e:
        print(f"Erro ao consultar funcionário por ID: {e}")
        return None
    finally:
        conexao.close()

def alterar_funcionario(funcionario: Funcionario):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            UPDATE funcionario 
            SET CPF = ?, nome = ?, endereco = ?, telefone = ?, RG = ?, email = ?
            WHERE id_funcionario = ?
        """, (
            funcionario.CPF,
            funcionario.nome,
            funcionario.endereco,
            funcionario.telefone,
            funcionario.rg,
            funcionario.email,
            funcionario.id_funcionario
        ))
        conexao.commit()
        print(f"Funcionário com ID {funcionario.id_funcionario} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar funcionário: {e}")
    finally:
        conexao.close()

def excluir_funcionario(id_funcionario: int):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM funcionario WHERE id_funcionario = ?", (id_funcionario,))
        conexao.commit()
        print(f"Funcionário com ID {id_funcionario} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir funcionário: {e}")
    finally:
        conexao.close()
