import streamlit as st
import pandas as pd
from Controllers.FuncionarioController import *
from Models.Funcionario import Funcionario

class FuncionarioConcreto(Funcionario):
    def __init__(self, id_funcionario, CPF, nome, rg, endereco, telefone, email):
        super().__init__(id_funcionario, CPF, nome, rg, endereco, telefone, email)

    def calcular_salario(self):
        pass

def show_funcionario_page():
    st.title('Gestão de Funcionários 👷')

    tab_cons, tab_incl, tab_alt, tab_excl = st.tabs(["📋 Consultar", "➕ Novo Funcionário", "✏️ Alterar", "🗑️ Excluir"])

    with tab_incl:
        st.subheader("Cadastrar Novo Funcionário")
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                nome = st.text_input("Nome Completo:", key="func_nome")
                CPF = st.text_input("CPF:", key="func_cpf")
                rg = st.text_input("RG:", key="func_rg")
            with col2:
                telefone = st.text_input("Telefone:", key="func_tel")
                email = st.text_input("Email:", key="func_email")
                endereco = st.text_input("Endereço:", key="func_end")

            if st.button("Salvar Funcionário", use_container_width=True):
                if nome and CPF:
                    novo_funcionario = FuncionarioConcreto(id_funcionario=None, CPF=CPF, nome=nome, rg=rg, 
                                                          endereco=endereco, telefone=telefone, email=email)
                    incluir_funcionario(novo_funcionario)
                    st.success(f"Funcionário {nome} cadastrado!")
                    st.rerun()
                else:
                    st.error("Nome e CPF são obrigatórios!")

    with tab_cons:
        st.subheader("Lista de Funcionários")
        funcionarios = consultar_funcionarios()
        if funcionarios:
            df = pd.DataFrame(funcionarios)
            busca = st.text_input("Filtrar por nome ou CPF:", key="busca_func")
            if busca:
                df = df[df.apply(lambda row: busca.lower() in str(row['nome']).lower() or busca in str(row['CPF']), axis=1)]
            st.dataframe(df, use_container_width=True)
        else:
            st.info("Nenhum funcionário cadastrado.")

    with tab_excl:
        st.subheader("Remover Funcionário")
        id_func = st.number_input("ID do funcionário a excluir:", min_value=1, key="excluir_id_func")
        if st.button("Excluir Definitivamente", type="primary", use_container_width=True):
            excluir_funcionario(id_func)
            st.success("Funcionário removido!")
            st.rerun()

    with tab_alt:
        st.subheader("Atualizar Cadastro")
        funcionarios = consultar_funcionarios()
        if funcionarios:
            id_func_alt = st.number_input("ID do funcionário:", min_value=1, key="alt_id_func")
            func_data = next((f for f in funcionarios if f['id_funcionario'] == id_func_alt), None)

            if func_data:
                with st.form(key="form_alt_func"):
                    col1, col2 = st.columns(2)
                    with col1:
                        nome = st.text_input("Nome:", value=func_data['nome'])
                        cpf = st.text_input("CPF:", value=func_data['CPF'])
                    with col2:
                        tel = st.text_input("Telefone:", value=func_data['telefone'])
                        mail = st.text_input("Email:", value=func_data['email'])

                    if st.form_submit_button("Salvar Alterações", use_container_width=True):
                        func_alt = FuncionarioConcreto(id_funcionario=id_func_alt, CPF=cpf, nome=nome, rg=func_data['RG'], 
                                                      endereco=func_data['endereco'], telefone=tel, email=mail)
                        alterar_funcionario(func_alt)
                        st.success("Cadastro atualizado!")
                        st.rerun()
            elif id_func_alt != 0:
                st.warning("Funcionário não encontrado!")