import sqlite3

entrada = input(" ")

def tudo():
    conn = sqlite3.connect("tarefas.db")
    sql = "SELECT * FROM tarefas"
    cursor = conn.execute(sql)
    for row in cursor:
        print(row)
    conn.close()

def deletar():
    conn = sqlite3.connect("tarefas.db")
    sql = "DELETE * FROM tarefas"
    cursor = conn.execute(sql)
    conn.commit()
    conn.close()


if entrada == "tudo":
    tudo()


if entrada == "deletar":
    deletar()

else:
    print("Comando inválido")