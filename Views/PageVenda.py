import streamlit as st
import pandas as pd
from Controllers.VendaController import *
from Controllers.ClienteController import consultar_clientes
from Controllers.EntrepostoOvosController import consultar_entrepostos_ovos
from Controllers.OvoController import consultar_ovos
from Models.Venda import Venda

def show_venda_page():
    st.title('Gestão de Vendas 💰')

    # Abas para organizar as operações
    tab_cons, tab_incl, tab_alt, tab_excl = st.tabs(["📋 Consultar", "➕ Registrar", "✏️ Alterar", "🗑️ Excluir"])

    clientes = consultar_clientes()
    cliente_options = {f"{c['nome']} (ID: {c['id_cliente']})": c['id_cliente'] for c in clientes}

    entrepostos = consultar_entrepostos_ovos()
    entreposto_options = {f"{e['CNPJ']} (ID: {e['id_entreposto']})": e['id_entreposto'] for e in entrepostos}

    ovos = consultar_ovos()
    ovo_options = {f"{o['tipo_ovo']} - {o['categoria']} (ID: {o['id_ovo']})": o['id_ovo'] for o in ovos}

    with tab_incl:
        st.subheader("Registrar Nova Venda")
        col1, col2 = st.columns(2)
        with col1:
            codigo = st.text_input("Código da Venda:")
            data_venda = st.date_input("Data da Venda:")
        with col2:
            cliente_selecionado = st.selectbox("Cliente:", list(cliente_options.keys()))
            entreposto_selecionado = st.selectbox("Entreposto:", list(entreposto_options.keys()))

        col3, col4 = st.columns(2)
        with col3:
            qntd_bandejas = st.number_input("Qtd Bandejas:", min_value=0)
            valor_bandeja = st.number_input("Valor Unit. Bandeja:", min_value=0.0, format="%.2f")
        with col4:
            qntd_caixas = st.number_input("Qtd Caixas:", min_value=0)
            valor_caixa = st.number_input("Valor Unit. Caixa:", min_value=0.0, format="%.2f")

        ovo_selecionado = st.selectbox("Tipo de Ovo:", list(ovo_options.keys()))

        if st.button("Confirmar Registro", use_container_width=True):
            if not all([cliente_selecionado, entreposto_selecionado, ovo_selecionado]):
                st.error("Erro: Verifique se existem clientes, entrepostos e ovos cadastrados.")
            else:
                id_cliente = cliente_options[cliente_selecionado]
                id_entreposto = entreposto_options[entreposto_selecionado]
                id_ovo = ovo_options[ovo_selecionado]

                nova_venda = Venda(id_venda=None, codigo=codigo, data_venda=str(data_venda), 
                                  qntd_bandeijas_vendidas=qntd_bandejas, qntd_caixas_vendidas=qntd_caixas, 
                                  valor_bandeija=valor_bandeja, valor_caixa=valor_caixa, 
                                  id_cliente=id_cliente, id_entreposto=id_entreposto, id_ovo=id_ovo)
                incluir_venda(nova_venda)
                st.success("Venda registrada com sucesso!")
                st.rerun()

    with tab_cons:
        st.subheader("Consultar Vendas")
        vendas = consultar_vendas()
        if vendas:
            df = pd.DataFrame(vendas)

            # Filtro de busca
            busca = st.text_input("Filtrar por Código ou ID:")
            if busca:
                df = df[df.apply(lambda row: busca in str(row['codigo']) or busca in str(row['id_venda']), axis=1)]

            # Exibir dataframe formatado
            st.dataframe(df, use_container_width=True)

            # Resumo financeiro
            total_venda = (df['qntd_bandeijas_vendidas'] * df['valor_bandeija'] + 
                          df['qntd_caixas_vendidas'] * df['valor_caixa']).sum()
            st.info(f"💰 **Total das vendas listadas:** R$ {total_venda:,.2f}")
        else:
            st.info("Nenhuma venda registrada.")

    with tab_excl:
        st.subheader("Excluir Registro")
        vendas = consultar_vendas()
        if vendas:
            id_venda = st.number_input("Informe o ID da venda para excluir:", min_value=1)
            if st.button("Excluir Definitivamente", type="primary"):
                excluir_venda(id_venda)
                st.success("Venda excluída!")
                st.rerun()
        else:
            st.info("Nenhuma venda registrada.")

    with tab_alt:
        st.subheader("Alterar Registro")
        vendas = consultar_vendas()
        if vendas:
            id_venda_alt = st.number_input("ID da venda a alterar:", min_value=1, key="alt_venda_id")
            venda_data = next((v for v in vendas if v['id_venda'] == id_venda_alt), None)

            if venda_data:
                with st.form(key="form_altera_venda"):
                    col1, col2 = st.columns(2)
                    with col1:
                        codigo = st.text_input("Código:", value=venda_data['codigo'])
                        data_venda = st.text_input("Data (YYYY-MM-DD):", value=venda_data['data_venda'])

                    with col2:
                        qntd_bandejas = st.number_input("Qtd Bandejas:", min_value=0, value=venda_data['qntd_bandeijas_vendidas'])
                        qntd_caixas = st.number_input("Qtd Caixas:", min_value=0, value=venda_data['qntd_caixas_vendidas'])

                    if st.form_submit_button("Salvar Alterações", use_container_width=True):
                        # Simplicado para o exemplo, mantendo IDs originais se não mudados
                        venda_alterada = Venda(id_venda=id_venda_alt, codigo=codigo, data_venda=data_venda, 
                                              qntd_bandeijas_vendidas=qntd_bandejas, qntd_caixas_vendidas=qntd_caixas, 
                                              valor_bandeija=venda_data['valor_bandeija'], valor_caixa=venda_data['valor_caixa'], 
                                              id_cliente=venda_data['id_cliente'], id_entreposto=venda_data['id_entreposto'], 
                                              id_ovo=venda_data['id_ovo'])
                        alterar_venda(venda_alterada)
                        st.success("Venda atualizada!")
                        st.rerun()
            elif id_venda_alt != 0:
                st.warning("Venda não encontrada!")