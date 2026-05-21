import streamlit as st
import pandas as pd
from Controllers.OvoController import *
from Controllers.GalinhaController import consultar_galinhas
from Models.Ovo import Ovo

def show_ovo_page():
    st.title('Gestão de Produção de Ovos 🥚')
    
    tab_cons, tab_incl, tab_alt, tab_excl = st.tabs(["📋 Consultar", "➕ Novo Registro", "✏️ Alterar", "🗑️ Excluir"])

    galinhas = consultar_galinhas()
    galinha_map = {f"{g['tipo_galinha']} (ID: {g['id_galinha']})": g['id_galinha'] for g in galinhas}
    
    with tab_incl:
        st.subheader("Registrar Produção")
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                tipo_galinha_selecionado = st.selectbox("Origem (Galinha):", list(galinha_map.keys()))
                categoria = st.selectbox("Categoria:", ["A", "B", "Extra", "Industrial"])
            with col2:
                tamanho = st.selectbox("Tamanho:", ["Pequeno", "Médio", "Grande", "Jumbo"])
                tipo_ovo = st.text_input("Tipo (Ex: Caipira, Branco):")
            
            if st.button("Salvar Registro", use_container_width=True):
                id_galinha = galinha_map.get(tipo_galinha_selecionado)
                novo_ovo = Ovo(id_ovo=None, id_galinha=id_galinha, categoria=categoria, tamanho=tamanho, tipo_ovo=tipo_ovo)
                incluir_ovo(novo_ovo)
                st.success("Ovo registrado com sucesso!")
                st.rerun()

    with tab_cons:
        st.subheader("Estoque de Ovos")
        ovos = consultar_ovos()
        if ovos:
            df = pd.DataFrame(ovos)
            busca = st.text_input("Filtrar por ID ou Tipo de Ovo:", key="busca_ovo")
            if busca:
                df = df[df.apply(lambda row: busca.lower() in str(row['tipo_ovo']).lower() or busca in str(row['id_ovo']), axis=1)]
            st.dataframe(df, use_container_width=True)
        else:
            st.info("Nenhum ovo registrado.")

    with tab_excl:
        st.subheader("Remover Registro")
        id_ovo = st.number_input("ID do registro a excluir:", min_value=1, key="excluir_id_ovo")
        if st.button("Excluir Permanentemente", type="primary", use_container_width=True):
            excluir_ovo(id_ovo)
            st.success("Registro removido!")
            st.rerun()

    with tab_alt:
        st.subheader("Alterar Registro")
        ovos = consultar_ovos()
        if ovos:
            id_ovo_alt = st.number_input("ID do registro:", min_value=1, key="alt_id_ovo")
            ovo_data = next((o for o in ovos if o['id_ovo'] == id_ovo_alt), None)
            
            if ovo_data:
                with st.form(key="form_alt_ovo"):
                    col1, col2 = st.columns(2)
                    with col1:
                        cat = st.text_input("Categoria:", value=ovo_data['categoria'])
                        tam = st.text_input("Tamanho:", value=ovo_data['tamanho'])
                    with col2:
                        tipo = st.text_input("Tipo:", value=ovo_data['tipo_ovo'])
                    
                    if st.form_submit_button("Salvar Alterações", use_container_width=True):
                        ovo_alt = Ovo(id_ovo=id_ovo_alt, id_galinha=ovo_data['id_galinha'], 
                                     categoria=cat, tamanho=tam, tipo_ovo=tipo)
                        alterar_ovo(ovo_alt)
                        st.success("Registro atualizado!")
                        st.rerun()
            elif id_ovo_alt != 0:
                st.warning("Registro não encontrado!")
