import streamlit as st
from Views.PageHome import show_home_page
from Views.PageCliente import show_cliente_page
from Views.PageFuncionario import show_funcionario_page
from Views.PageGalinha import show_galinha_page
from Views.PageOvo import show_ovo_page
from Views.PageRancho import show_rancho_page
from Views.PageVenda import show_venda_page
from Views.PageEntrepostoOvos import show_entreposto_page
from setup_database import setup_all_tables

# Configuração da página deve ser a primeira chamada Streamlit
st.set_page_config(page_title="Gerenciamento de Granja", page_icon="🥚", layout="wide")

def main():
    # Inicializa o banco de dados apenas se ainda não foi inicializado nesta sessão
    if "db_initialized" not in st.session_state:
        setup_all_tables()
        st.session_state.db_initialized = True

    # Controle de Tema (Claro/Escuro)
    st.sidebar.title("Granja BMO 🥚")
    dark_mode = st.sidebar.toggle("🌙 Modo Escuro", value=False)
    
    # Definição de Cores baseada no Tema
    if dark_mode:
        bg_color = "#121212"
        sidebar_bg = "#1e1e1e"
        text_color = "#ffffff"
        card_bg = "#2d2d2d"
        border_color = "#404040"
        secondary_text = "#bbbbbb"
    else:
        bg_color = "#f8f9fa"
        sidebar_bg = "#ffffff"
        text_color = "#1f2937"
        card_bg = "#ffffff"
        border_color = "#e5e7eb"
        secondary_text = "#4b5563"

    # Injeção de CSS Dinâmico
    st.markdown(f"""
    <style>
        .stApp {{
            background-color: {bg_color};
            color: {text_color};
        }}
        
        /* Texto da Sidebar (Onde estava o problema do print) */
        [data-testid="stSidebar"] {{
            background-color: {sidebar_bg} !important;
            border-right: 1px solid {border_color};
        }}
        
        /* Seletores específicos para garantir que o texto da navegação apareça */
        [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p,
        [data-testid="stSidebar"] label p,
        [data-testid="stSidebar"] .stMarkdown p,
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] span {{
            color: {text_color} !important;
            font-weight: 600 !important;
        }}
        
        /* Corrigindo especificamente os rótulos do rádio button */
        div[role="radiogroup"] label div[data-testid="stMarkdownContainer"] p {{
            color: {text_color} !important;
        }}
        
        /* Botões */
        .stButton>button {{
            border-radius: 8px;
            border: 1px solid {border_color};
            background-color: {card_bg};
            color: {text_color};
            transition: all 0.2s;
        }}
        
        /* Cards e Métricas */
        div[data-testid="metric-container"] {{
            background-color: {card_bg};
            border: 1px solid {border_color};
            padding: 15px;
            border-radius: 12px;
        }}
        [data-testid="stMetricValue"] {{ color: {text_color} !important; }}
        [data-testid="stMetricLabel"] {{ color: {secondary_text} !important; }}
        
        /* Abas */
        .stTabs [data-baseweb="tab"] {{
            color: {secondary_text};
        }}
        .stTabs [aria-selected="true"] {{
            color: #ff4b4b !important;
            border-bottom-color: #ff4b4b !important;
        }}
        
        /* Ajuste para inputs em modo escuro */
        input, select, textarea {{
            color: {text_color} !important;
        }}
    </style>
    """, unsafe_allow_html=True)

    pages = {
        "🏠 Home": show_home_page,
        "👥 Clientes": show_cliente_page,
        "👷 Funcionários": show_funcionario_page,
        "🐔 Galinhas": show_galinha_page,
        "🏡 Ranchos": show_rancho_page,
        "🥚 Ovos": show_ovo_page,
        "📦 Entrepostos": show_entreposto_page,
        "💰 Vendas": show_venda_page,
    }
    
    if "page" not in st.session_state:
        st.session_state.page = "🏠 Home"

    # Sincroniza o selectbox com o session_state.page
    page_keys = list(pages.keys())
    
    st.sidebar.title("Granja BMO 🥚")
    st.sidebar.markdown("---")
    
    # Encontra o índice da página atual para garantir que o selectbox esteja sincronizado
    # Se a página no session_state não tiver o emoji, tenta encontrar a correspondente
    current_page = st.session_state.page
    if current_page not in page_keys:
        # Tenta encontrar a página que termina com o nome (para compatibilidade com cliques de botões)
        match = [k for k in page_keys if k.endswith(current_page)]
        if match:
            current_page = match[0]
        else:
            current_page = "🏠 Home"

    current_page_index = page_keys.index(current_page)
    
    page_choice = st.sidebar.radio(
        "Navegação", 
        page_keys, 
        index=current_page_index
    )
    
    if page_choice != current_page:
        st.session_state.page = page_choice
        st.rerun()
    
    st.sidebar.markdown("---")
    st.sidebar.info("Sistema de Gestão v2.0")
    
    # Renderiza a página selecionada
    pages[page_choice]()

if __name__ == "__main__":
    main()