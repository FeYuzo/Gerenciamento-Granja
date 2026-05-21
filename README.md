# 🥚 Sistema de Gerenciamento de Granja BMO

Um sistema moderno e intuitivo desenvolvido em Python para o controle total de uma granja, desde o cadastro de aves e funcionários até o monitoramento de vendas e faturamento através de um Dashboard interativo.

## 🚀 Funcionalidades

- **📊 Dashboard Inteligente**: Visualize o faturamento total, estoque de ovos e total de aves em tempo real com gráficos dinâmicos.
- **🌗 Modo Escuro**: Suporte a temas claro e escuro para melhor conforto visual.
- **👥 Gestão de Clientes**: Cadastro completo com histórico de compras e observações.
- **👷 Controle de Funcionários**: Gestão de dados da equipe e informações de contato.
- **🐔 Controle de Aves (Galinhas)**: Monitoramento de tipos, idades e datas de vacinação.
- **🥚 Produção de Ovos**: Registro categorizado por tipo e tamanho.
- **🏡 Gestão de Ranchos**: Acompanhamento de custos e produção por unidade.
- **💰 Módulo de Vendas**: Registro e consulta de transações financeiras com resumo automático.

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: [Python](https://www.python.org/)
- **Interface Web**: [Streamlit](https://streamlit.io/)
- **Banco de Dados**: SQLite
- **Manipulação de Dados**: Pandas
- **Design**: CSS Customizado

## 📦 Como Instalar e Rodar

### Pré-requisitos
- Python 3.10 ou superior instalado.

### Passo a Passo

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/FeYuzo/Gerenciamento-Granja.git
   cd Gerenciamento-Granja
   ```

2. **Crie um ambiente virtual**:
   ```bash
   python -m venv venv
   # No Windows:
   .\venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install streamlit pandas
   ```

4. **Inicie a aplicação**:
   ```bash
   streamlit run main.py
   ```

## 📂 Estrutura do Projeto

- `main.py`: Ponto de entrada da aplicação e configurações de tema.
- `Views/`: Telas da interface do usuário.
- `Controllers/`: Lógica de negócio e comunicação entre View e Model.
- `Models/`: Classes que representam as entidades do sistema.
- `Services/`: Scripts de conexão e criação das tabelas do banco de dados.
- `imagens/`: Ativos visuais do sistema.

## ✒️ Autor

- **FeYuzo** - [GitHub](https://github.com/FeYuzo)


