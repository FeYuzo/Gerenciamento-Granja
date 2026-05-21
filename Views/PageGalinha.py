import streamlit as st
import pandas as pd
from Controllers.GalinhaController import *
from Models.Galinha import Galinha

def show_galinha_page():
    st.title('Gestão de Galinhas 🐔')

    tab_cons, tab_incl, tab_alt, tab_excl = st.tabs(["📋 Consultar", "➕ Nova Galinha", "✏️ Alterar", "🗑️ Excluir"])

    with tab_incl:
        st.subheader("Cadastrar Nova Galinha")
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                tipo_galinha = st.text_input("Tipo/Raça:")
                idade = st.number_input("Idade (semanas):", min_value=0)
            with col2:
                data_vacinacao = st.date_input("Última Vacinação:")

            if st.button("Cadastrar Galinha", use_container_width=True):
                if tipo_galinha:
                    nova_galinha = Galinha(tipo_galinha=tipo_galinha, idade=idade, data_vacinacao=str(data_vacinacao))
                    incluir_galinha(nova_galinha)
                    st.success(f"Galinha {tipo_galinha} cadastrada!")
                    st.rerun()
                else:
                    st.error("O tipo da galinha é obrigatório!")

    with tab_cons:
        st.subheader("Aves Cadastradas")
        galinhas = consultar_galinhas()
        if galinhas:
            df = pd.DataFrame(galinhas)
            busca = st.text_input("Buscar por ID ou Tipo:", key="busca_gal")
            if busca:
                df = df[df.apply(lambda row: busca.lower() in str(row['tipo_galinha']).lower() or busca in str(row['id_galinha']), axis=1)]
            st.dataframe(df, use_container_width=True)
        else:
            st.info("Nenhuma galinha cadastrada.")

    with tab_excl:
        st.subheader("Remover Registro")
        id_gal = st.number_input("ID da galinha a excluir:", min_value=1, key="excluir_id_gal")
        if st.button("Remover Permanentemente", type="primary", use_container_width=True):
            excluir_galinha(id_gal)
            st.success("Registro removido!")
            st.rerun()

    with tab_alt:
        st.subheader("Atualizar Dados")
        galinhas = consultar_galinhas()
        if galinhas:
            id_gal_alt = st.number_input("ID da galinha:", min_value=1, key="alt_id_gal")
            gal_data = next((g for g in galinhas if g['id_galinha'] == id_gal_alt), None)

            if gal_data:
                with st.form(key="form_alt_gal"):
                    col1, col2 = st.columns(2)
                    with col1:
                        tipo = st.text_input("Tipo/Raça:", value=gal_data['tipo_galinha'])
                        idade_sem = st.number_input("Idade (semanas):", min_value=0, value=gal_data['idade'])
                    with col2:
                        vacina = st.text_input("Vacinação (YYYY-MM-DD):", value=gal_data['data_vacinacao'])

                    if st.form_submit_button("Salvar Alterações", use_container_width=True):
                        gal_alt = Galinha(id_galinha=id_gal_alt, tipo_galinha=tipo, idade=idade_sem, data_vacinacao=vacina)
                        alterar_galinha(gal_alt)
                        st.success("Registro atualizado!")
                        st.rerun()
            elif id_gal_alt != 0:
                st.warning("Galinha não encontrada!")