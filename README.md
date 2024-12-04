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
- SQLite

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x
- pip (gerenciador de pacotes do Python)

### Passos para Executar

1. Clone o repositório:

    ```sh
    git clone https://github.com/sharktank-tech/Tarefas
    cd /Tarefas ou seu-repositorio
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

4. No arquivo `config.py` na raiz do projeto edite as configurações:

    ```python
    class Config:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        SECRET_KEY = 'sua-chave-secreta'
    ```

5. Execute a aplicação:

    ```sh
    python3 run.py
    ```

6. Acesse a aplicação no seu navegador:

    ```
    http://127.0.0.1:000
    ```
