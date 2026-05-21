import streamlit as st
import pandas as pd
from Controllers.ClienteController import consultar_clientes
from Controllers.GalinhaController import consultar_galinhas
from Controllers.OvoController import consultar_ovos
from Controllers.VendaController import consultar_vendas

def show_home_page():
    st.title("📊 Painel de Controle - Granja BMO")
    
    # Busca de dados para as métricas
    clientes = consultar_clientes()
    galinhas = consultar_galinhas()
    ovos = consultar_ovos()
    vendas = consultar_vendas()
    
    # Cálculo das métricas
    total_clientes = len(clientes)
    total_galinhas = len(galinhas)
    total_ovos = len(ovos)
    faturamento_total = sum((v['qntd_bandeijas_vendidas'] * v['valor_bandeija']) + 
                            (v['qntd_caixas_vendidas'] * v['valor_caixa']) for v in vendas)

    # Exibição das métricas em colunas
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total de Clientes", total_clientes, help="Número de clientes cadastrados")
    m2.metric("Total de Galinhas", total_galinhas, help="Número de galinhas na granja")
    m3.metric("Estoque de Ovos", total_ovos, help="Ovos registrados")
    m4.metric("Faturamento", f"R$ {faturamento_total:,.2f}", help="Soma total das vendas")

    st.markdown("---")

    # Layout em duas colunas para Gráfico e Ações Rápidas
    col_graf, col_acoes = st.columns([2, 1])

    with col_graf:
        st.subheader("Tendência de Vendas")
        if vendas:
            df_vendas = pd.DataFrame(vendas)
            # Agrupar vendas por cliente para um gráfico simples
            vendas_por_cliente = df_vendas.groupby('cliente_telefone').apply(
                lambda x: (x['qntd_bandeijas_vendidas'] * x['valor_bandeija'] + 
                           x['qntd_caixas_vendidas'] * x['valor_caixa']).sum()
            ).reset_index()
            vendas_por_cliente.columns = ['Cliente (Tel)', 'Total (R$)']
            st.bar_chart(vendas_por_cliente.set_index('Cliente (Tel)'))
        else:
            st.info("Ainda não há dados de vendas para exibir gráficos.")

    with col_acoes:
        st.subheader("Acesso Rápido")
        
        if st.button("👥 Clientes", use_container_width=True):
            st.session_state.page = "👥 Clientes"
            st.rerun()
        if st.button("🐔 Galinhas", use_container_width=True):
            st.session_state.page = "🐔 Galinhas"
            st.rerun()
        if st.button("🥚 Ovos", use_container_width=True):
            st.session_state.page = "🥚 Ovos"
            st.rerun()
        if st.button("💰 Vendas", use_container_width=True):
            st.session_state.page = "💰 Vendas"
            st.rerun()

    st.markdown("---")
    st.image("imagens/granja.png", use_container_width=True)
