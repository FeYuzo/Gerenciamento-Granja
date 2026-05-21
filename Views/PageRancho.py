import streamlit as st
import pandas as pd
from Controllers.RanchoController import *
from Controllers.GalinhaController import consultar_galinhas
from Models.Rancho import Rancho

def show_rancho_page():
    st.title('Gestão de Ranchos 🏡')

    tab_cons, tab_incl, tab_alt, tab_excl = st.tabs(["📋 Consultar", "➕ Novo Rancho", "✏️ Alterar", "🗑️ Excluir"])

    galinhas = consultar_galinhas()
    galinha_map = {f"{g['tipo_galinha']} (ID: {g['id_galinha']})": g['id_galinha'] for g in galinhas}

    with tab_incl:
        st.subheader("Cadastrar Novo Rancho")
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                tipo_galinha_selecionado = st.selectbox("Lote de Galinhas:", list(galinha_map.keys()))
                numeracao = st.number_input("Número do Rancho:", min_value=0)
            with col2:
                gastos = st.number_input("Gastos Mensais (R$):", min_value=0.0, format="%.2f")
                producao = st.number_input("Produção Diária (Ovos):", min_value=0)

            if st.button("Salvar Rancho", use_container_width=True):
                id_galinha = galinha_map.get(tipo_galinha_selecionado)
                novo_rancho = Rancho(id_rancho=None, id_galinha=id_galinha, numeracao=numeracao, gastos=gastos, producao=producao)
                incluir_rancho(novo_rancho)
                st.success(f"Rancho {numeracao} cadastrado!")
                st.rerun()

    with tab_cons:
        st.subheader("Ranchos Ativos")
        ranchos = consultar_ranchos()
        if ranchos:
            df = pd.DataFrame(ranchos)
            busca = st.text_input("Buscar por ID ou Número:", key="busca_rancho")
            if busca:
                df = df[df.apply(lambda row: busca in str(row['numeracao']) or busca in str(row['id_rancho']), axis=1)]
            st.dataframe(df, use_container_width=True)
        else:
            st.info("Nenhum rancho cadastrado.")

    with tab_excl:
        st.subheader("Remover Rancho")
        id_rancho = st.number_input("ID do rancho a excluir:", min_value=1, key="excluir_id_rancho")
        if st.button("Excluir Definitivamente", type="primary", use_container_width=True):
            excluir_rancho(id_rancho)
            st.success("Rancho removido!")
            st.rerun()

    with tab_alt:
        st.subheader("Atualizar Informações")
        ranchos = consultar_ranchos()
        if ranchos:
            id_rancho_alt = st.number_input("ID do rancho:", min_value=1, key="alt_id_rancho")
            rancho_data = next((r for r in ranchos if r['id_rancho'] == id_rancho_alt), None)

            if rancho_data:
                with st.form(key="form_alt_rancho"):
                    col1, col2 = st.columns(2)
                    with col1:
                        num = st.number_input("Numeração:", min_value=0, value=rancho_data['numeracao'])
                        gas = st.number_input("Gastos (R$):", min_value=0.0, format="%.2f", value=rancho_data['gastos'])
                    with col2:
                        prod = st.number_input("Produção:", min_value=0, value=rancho_data['producao'])

                    if st.form_submit_button("Salvar Alterações", use_container_width=True):
                        rancho_alt = Rancho(id_rancho=id_rancho_alt, id_galinha=rancho_data['id_galinha'], 
                                           numeracao=num, gastos=gas, producao=prod)
                        alterar_rancho(rancho_alt)
                        st.success("Dados do rancho atualizados!")
                        st.rerun()
            elif id_rancho_alt != 0:
                st.warning("Rancho não encontrado!")