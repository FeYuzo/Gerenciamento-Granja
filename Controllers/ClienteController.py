from Services.database import get_db_connection
from Models.Clientes import Cliente
import sqlite3

def incluir_cliente(cliente: Cliente):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO cliente (nome, telefone, endereco, qntd_compra_bandeija, observacoes)
            VALUES (?, ?, ?, ?, ?)
        """, (
            cliente.nome,
            cliente.telefone,
            cliente.endereco,
            cliente.qntd_compra_bandeija,
            cliente.observacoes
        ))
        conexao.commit()
        print(f"Cliente {cliente.nome} inserido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir cliente: {e}")
    finally:
        conexao.close()

import streamlit as st

@st.cache_data
def consultar_clientes():
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT id_cliente, nome, telefone, endereco, qntd_compra_bandeija, observacoes FROM cliente')
        rows = cursor.fetchall()
        clientes = []
        for row in rows:
            clientes.append({
                "id_cliente": row[0],
                "nome": row[1],
                "telefone": row[2],
                "endereco": row[3],
                "qntd_compra_bandeija": row[4],
                "observacoes": row[5]
            })
        return clientes
    except sqlite3.Error as e:
        print(f"Erro ao consultar clientes: {e}")
        return []
    finally:
        conexao.close()

def consultar_cliente_por_id(id_cliente: int):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT id_cliente, nome, telefone, endereco, qntd_compra_bandeija, observacoes FROM cliente WHERE id_cliente = ?', (id_cliente,))
        row = cursor.fetchone()
        if row:
            return {
                "id_cliente": row[0],
                "nome": row[1],
                "telefone": row[2],
                "endereco": row[3],
                "qntd_compra_bandeija": row[4],
                "observacoes": row[5]
            }
        return None
    except sqlite3.Error as e:
        print(f"Erro ao consultar cliente por ID: {e}")
        return None
    finally:
        conexao.close()

def alterar_cliente(cliente: Cliente):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            UPDATE cliente 
            SET nome = ?, telefone = ?, endereco = ?, qntd_compra_bandeija = ?, observacoes = ?
            WHERE id_cliente = ?
        """, (
            cliente.nome,
            cliente.telefone,
            cliente.endereco,
            cliente.qntd_compra_bandeija,
            cliente.observacoes,
            cliente.id_cliente
        ))
        conexao.commit()
        print(f"Cliente com ID {cliente.id_cliente} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar cliente: {e}")
    finally:
        conexao.close()

def excluir_cliente(id_cliente: int):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM cliente WHERE id_cliente = ?", (id_cliente,))
        conexao.commit()
        print(f"Cliente com ID {id_cliente} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir cliente: {e}")
    finally:
        conexao.close()
