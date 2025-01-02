from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

# Filtro personalizado para formatar datas no formato brasileiro (DD/MM/YYYY)
@app.template_filter('format_date')
def format_date(value, format='%d/%m/%Y'):
    return value.strftime(format) if isinstance(value, datetime.datetime) else value

# Função para criar a tabela de tarefas no banco de dados
def criar_tabela():
    with sqlite3.connect('tarefas.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS tarefas (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          descricao TEXT NOT NULL,
                          data TEXT NOT NULL,
                          status TEXT NOT NULL)''')
        conn.commit()

# Função para executar queries no banco de dados
def executar_query(query, params=()):
    with sqlite3.connect('tarefas.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor

# Rota inicial para visualizar todas as tarefas
@app.route('/')
def ver_tarefas():
    tarefas = executar_query("SELECT id, descricao, data, status FROM tarefas").fetchall()
    return render_template('index.html', data=tarefas if tarefas else None)

# Rota para excluir uma tarefa
@app.route('/excluir_tarefas/<int:id>', methods=['GET','POST'])
def excluir_tarefa(id):
    executar_query("DELETE FROM tarefas WHERE id=?", (id,))
    return redirect(url_for('ver_tarefas'))

# Função para adicionar uma nova tarefa no banco de dados
def adicionar_tarefa(descricao, data, status):
    executar_query('''INSERT INTO tarefas (descricao, data, status)
                      VALUES (?, ?, ?)''', (descricao, data, status))

# Rota para editar uma tarefa existente
@app.route('/editar_tarefas/<int:id>', methods=['GET', 'POST'])
def editar_tarefa(id):
    if request.method == 'POST':
        descricao = request.form.get('descricao')
        data = request.form.get('data')
        status = request.form.get('status')

        if not descricao or not data or not status:
            return "Erro: Todos os campos são obrigatórios."

        try:
            executar_query('''UPDATE tarefas SET descricao = ?, data = ?, status = ?
                              WHERE id = ?''', (descricao, data, status, id))
            return redirect(url_for('ver_tarefas'))
        except Exception as e:
            return f"Erro ao atualizar a tarefa: {str(e)}"
    else:
        tarefa = executar_query("SELECT * FROM tarefas WHERE id = ?", (id,)).fetchone()
        return render_template('editar_tarefas.html', tarefa=tarefa) if tarefa else "Tarefa não encontrada."

# Rota para adicionar uma nova tarefa
@app.route('/add_tarefas', methods=['GET', 'POST'])
def add_tarefas():
    if request.method == 'POST':
        descricao = request.form.get('descricao')
        data = request.form.get('data')
        status = request.form.get('status')

        if descricao and data and status:
            adicionar_tarefa(descricao, data, status)
            return redirect(url_for('ver_tarefas'))
        else:
            return "Erro: Todos os campos são obrigatórios."
    return render_template('add_tarefas.html')

# Rota para enviar um relatório por e-mail
@app.route('/enviar_email', methods=['GET', 'POST'])
def enviar_email_route():
    tarefas = executar_query("SELECT * FROM tarefas").fetchall()

    if request.method == 'POST':
        destinatario = request.form.get('destinatario')

        if not destinatario:
            return "Erro: destinatário é obrigatório."

        tarefas_formatadas = formatar_tarefas(tarefas)

        try:
            enviar_email(destinatario, 'Relatório de Tarefas', tarefas_formatadas)
            n_tr = len(tarefas_formatadas)
            flash(f"Email com {n_tr} tarefas foi enviado ")
            return redirect(url_for('ver_tarefas'))
        except Exception as e:
            return f"Erro ao enviar e-mail: {str(e)}"
    else:
        return render_template('email.html')

# Função para enviar um e-mail com o relatório de tarefas
def enviar_email(destinatario, assunto, corpo):
    servidor_smtp = "smtp.gmail.com"
    porta_smtp = 587
    remetente = "quicknotes527@gmail.com"
    senha = "qmlf rluh ixum tldt"

    msg = MIMEMultipart()
    msg['From'] = "Quick Notes"
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'plain'))

    with smtplib.SMTP(servidor_smtp, porta_smtp) as server:
        server.starttls()
        server.login(remetente, senha)
        server.send_message(msg)

# Função para formatar as tarefas em uma string apresentável para o e-mail
def formatar_tarefas(tarefas):
    if not tarefas:
        return "Não há tarefas disponíveis."

    tarefas_formatadas = []
    for tarefa in tarefas:
        id, descricao, data, status = tarefa
        tarefa_formatada = f"ID: {id}\nDescrição: {descricao}\nData: {data}\nStatus: {status}\n\n"
        tarefas_formatadas.append(tarefa_formatada)

    return "\n".join(tarefas_formatadas)

if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True, host='0.0.0.0', port=81)