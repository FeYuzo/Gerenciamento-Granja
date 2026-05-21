import streamlit as st
import pandas as pd
from Controllers.EntrepostoOvosController import *
from Models.Entreposto_de_ovos import EntrePostoOvos

def show_entreposto_page():
    st.title('Gestão de Entrepostos 📦')

    tab_cons, tab_incl, tab_alt, tab_excl = st.tabs(["📋 Consultar", "➕ Novo Entreposto", "✏️ Alterar", "🗑️ Excluir"])

    with tab_incl:
        st.subheader("Cadastrar Novo Entreposto")
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                cnpj = st.text_input("CNPJ da Unidade:")
                endereco = st.text_input("Localização/Endereço:")
            with col2:
                capacidade = st.number_input("Capacidade de Estocagem (Caixas):", min_value=0)
                qtd_compra = st.number_input("Volume de Compra Atual:", min_value=0)

            if st.button("Salvar Entreposto", use_container_width=True):
                if cnpj:
                    novo_entreposto = EntrePostoOvos(id_entreposto=None, cnpj=cnpj, endereco=endereco, 
                                                    capacidade_armazenamento=capacidade, quantidade_compra=qtd_compra)
                    incluir_entreposto_ovos(novo_entreposto)
                    st.success(f"Entreposto {cnpj} registrado!")
                    st.rerun()
                else:
                    st.error("O CNPJ é obrigatório!")

    with tab_cons:
        st.subheader("Unidades Registradas")
        entrepostos = consultar_entrepostos_ovos()
        if entrepostos:
            df = pd.DataFrame(entrepostos)
            busca = st.text_input("Filtrar por CNPJ ou ID:", key="busca_ent")
            if busca:
                df = df[df.apply(lambda row: busca in str(row['CNPJ']) or busca in str(row['id_entreposto']), axis=1)]
            st.dataframe(df, use_container_width=True)
        else:
            st.info("Nenhum entreposto cadastrado.")

    with tab_excl:
        st.subheader("Remover Entreposto")
        id_ent = st.number_input("ID do entreposto a excluir:", min_value=1, key="excluir_id_ent")
        if st.button("Excluir Permanentemente", type="primary", use_container_width=True):
            excluir_entreposto_ovos(id_ent)
            st.success("Unidade removida!")
            st.rerun()

    with tab_alt:
        st.subheader("Atualizar Unidade")
        entrepostos = consultar_entrepostos_ovos()
        if entrepostos:
            id_ent_alt = st.number_input("ID do entreposto:", min_value=1, key="alt_id_ent")
            ent_data = next((e for e in entrepostos if e['id_entreposto'] == id_ent_alt), None)

            if ent_data:
                with st.form(key="form_alt_ent"):
                    col1, col2 = st.columns(2)
                    with col1:
                        cnpj_val = st.text_input("CNPJ:", value=ent_data['CNPJ'])
                        end_val = st.text_input("Endereço:", value=ent_data['endereco'])
                    with col2:
                        cap_val = st.number_input("Capacidade:", min_value=0, value=int(ent_data['capacidade_armz']))
                        com_val = st.number_input("Qtd Compra:", min_value=0, value=int(ent_data['qtd_compra']))

                    if st.form_submit_button("Salvar Alterações", use_container_width=True):
                        ent_alt = EntrePostoOvos(id_entreposto=id_ent_alt, cnpj=cnpj_val, endereco=end_val, 
                                                capacidade_armazenamento=cap_val, quantidade_compra=com_val)
                        alterar_entreposto_ovos(ent_alt)
                        st.success("Dados da unidade atualizados!")
                        st.rerun()
            elif id_ent_alt != 0:
                st.warning("Entreposto não encontrado!")