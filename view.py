import sqlite3 as lite

# Criando conexão
con = lite.connect('dados.db')

# Criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS agenda(id integer primary key autoincrement, nome text, telefone text, email text)")

# inserir informações
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO agenda (nome, telefone, email) VALUES (?,?,?)"
        cur.execute(query, i)

def mostrar_info():
    lista=[]
    with con:
        cur = con.cursor()
        query= "SELECT * FROM agenda"
        info= cur.fetchall()
        
        for i in info:
            lista.append(i)
    return lista
        
# Deletar 
def deletar_form(i):
   
    with con:
        cur = con.cursor()
        query = "DELETE FROM agenda WHERE id=?"
        cur.execute(query, i)
        
# Atualizar/alterar 
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE agenda SET nome=?, telefone=?, email=? WHERE id=?"
        cur.execute(query, i)

# Ver estoque
def ver_form():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM agenda")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens

# Ver Item no estoque
def ver_iten(id):
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM agenda WHERE id=?",(id))
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens


def select_list(tree):
    tree.delete(*tree.get_children())
    
    with con:
        cur = con.cursor()
        lista = cur.execute("SELECT * FROM agenda ORDER BY id ASC;")
        for i in lista:
            tree.insert("", 'END', values=i)
        cur.close()