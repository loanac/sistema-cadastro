import sqlite3 as lite


#criando conexão
con = lite.connect('dados.db')

# Criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE agenda(id integer primary key autoincrement, nome text, telefone text, email text)")