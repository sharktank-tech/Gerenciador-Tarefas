# Projeto de Tarefas

Este é um projeto de gerenciamento de tarefas que permite adicionar, editar, excluir e visualizar tarefas. O projeto também inclui a funcionalidade de enviar um relatório por e-mail.

## Funcionalidades

- Adicionar uma nova tarefa
- Editar uma tarefa existente
- Excluir uma tarefa
- Visualizar todas as tarefas
- Enviar um relatório de tarefas por e-mail

## Tecnologias Utilizadas

- Flask (Python)
- HTML
- CSS
- JavaScript (jQuery)
- SQLite (ou outra base de dados configurada)

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x
- pip (gerenciador de pacotes do Python)

### Passos para Executar

1. Clone o repositório:

    ```sh
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie um ambiente virtual:

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

4. Crie o arquivo `config.py` na raiz do projeto e adicione as seguintes configurações:

    ```python
    SECRET_KEY = 'sua_chave_secreta_aqui'
    MAIL_SERVER = 'smtp.seuprovedor.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'seu_email@dominio.com'
    MAIL_PASSWORD = 'sua_senha'
    ```

5. Execute a aplicação:

    ```sh
    flask run
    ```

6. Acesse a aplicação no seu navegador:

    ```
    http://127.0.0.1:5000
    ```

## Estrutura do Projeto

