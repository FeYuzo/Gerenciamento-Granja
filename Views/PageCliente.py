import streamlit as st
import pandas as pd
from Controllers.ClienteController import *
from Models.Clientes import Cliente

def show_cliente_page():
    st.title('Gestão de Clientes 👥')

    tab_cons, tab_incl, tab_alt, tab_excl = st.tabs(["📋 Consultar", "➕ Novo Cliente", "✏️ Alterar", "🗑️ Excluir"])

    with tab_incl:
        st.subheader("Cadastrar Novo Cliente")
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                nome = st.text_input("Nome Completo:")
                telefone = st.text_input("Telefone/WhatsApp:")
            with col2:
                endereco = st.text_input("Endereço:")
                qntd_compra_bandeija = st.number_input("Média de Compra (Bandejas):", min_value=0)

            observacoes = st.text_area("Observações Adicionais:")

            if st.button("Salvar Cadastro", use_container_width=True):
                if nome and telefone:
                    novo_cliente = Cliente(id_cliente=None, nome=nome, telefone=telefone, endereco=endereco, 
                                          qntd_compra_bandeija=qntd_compra_bandeija, observacoes=observacoes)
                    incluir_cliente(novo_cliente)
                    st.success(f"Cliente {nome} cadastrado com sucesso!")
                    st.cache_data.clear()
                    st.rerun()
                else:
                    st.error("Nome e Telefone são obrigatórios!")

    with tab_cons:
        st.subheader("Lista de Clientes")
        clientes = consultar_clientes()
        if clientes:
            df = pd.DataFrame(clientes)

            busca = st.text_input("Filtrar por nome ou ID:", key="busca_cliente")
            if busca:
                df = df[df.apply(lambda row: busca.lower() in str(row['nome']).lower() or busca in str(row['id_cliente']), axis=1)]

            st.dataframe(df, use_container_width=True)
            st.info(f"Total de clientes encontrados: {len(df)}")
        else:
            st.info("Nenhum cliente cadastrado.")

    with tab_excl:
        st.subheader("Remover Cliente")
        id_cliente = st.number_input("ID do cliente a excluir:", min_value=1, key="excluir_id_cli")
        if st.button("Excluir Permanentemente", type="primary", use_container_width=True):
            excluir_cliente(id_cliente)
            st.success("Cliente removido com sucesso!")
            st.cache_data.clear()
            st.rerun()

    with tab_alt:
        st.subheader("Atualizar Dados")
        clientes = consultar_clientes()
        if clientes:
            id_cliente_alt = st.number_input("ID do cliente para alterar:", min_value=1, key="alt_id_cli")
            cliente_data = next((c for c in clientes if c['id_cliente'] == id_cliente_alt), None)

            if cliente_data:
                with st.form(key="form_alt_cliente"):
                    col1, col2 = st.columns(2)
                    with col1:
                        nome = st.text_input("Nome:", value=cliente_data['nome'])
                        telefone = st.text_input("Telefone:", value=cliente_data['telefone'])
                    with col2:
                        endereco = st.text_input("Endereço:", value=cliente_data['endereco'])
                        qntd_compra_bandeija = st.number_input("Compra (Bandeja):", min_value=0, value=cliente_data['qntd_compra_bandeija'])

                    observacoes = st.text_area("Observações:", value=cliente_data['observacoes'])

                    if st.form_submit_button("Salvar Alterações", use_container_width=True):
                        cliente_alterado = Cliente(id_cliente=id_cliente_alt, nome=nome, telefone=telefone, 
                                                  endereco=endereco, qntd_compra_bandeija=qntd_compra_bandeija, 
                                                  observacoes=observacoes)
                        alterar_cliente(cliente_alterado)
                        st.success("Dados atualizados!")
                        st.cache_data.clear()
                        st.rerun()
            elif id_cliente_alt != 0:
                st.warning("Cliente não encontrado!")
        else:
            st.info("Nenhum cliente cadastrado.")