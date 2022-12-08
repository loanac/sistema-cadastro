from tkinter import *
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox

from view import *

janela = Tk()
janela.title("Cadastro de clientes")
janela.geometry("800x500")
janela.iconbitmap('ico.ico')
janela.configure(bg="#d8dde9")

quadroGrid= LabelFrame(janela)
quadroGrid.pack(fill="both",expand="yes",padx=5,pady=5)
    

        
#FRAME COM FORMULARIO      
quadroPesquisar= Frame(janela, bg="#d8dde9")
quadroPesquisar.pack(fill="both", expand="yes",padx=10,pady=10)
# NOME
Ibid= Label(quadroPesquisar,text="Nome: ", bg="#d8dde9")
Ibid.place(x=90,y=0)
e_id= Entry(quadroPesquisar, relief="solid", width=40)
e_id.place(x=150,y=0)
# FONE
Ibfon= Label(quadroPesquisar,text="Fone: ", bg="#d8dde9")
Ibfon.place(x=90,y=40)
e_fon= Entry(quadroPesquisar, relief="solid", width=40)
e_fon.place(x=150,y=40)
# EMAIL
Ibemail= Label(quadroPesquisar,text="E-mail: ", bg="#d8dde9")
Ibemail.place(x=90,y=80)
e_mail= Entry(quadroPesquisar, relief="solid", width=40)
e_mail.place(x=150,y=80)


# FUNÇÕES DOS BOTÕES 
global tree 
    # FUNCOES DO BOTAO
def adicionar():
    nome = e_id.get()
    fone= e_fon.get()
    email= e_mail.get() 
       
    lista_inserir= [nome, fone, email]
        
    if e_id.get()=='':
        messagebox.showerror('Erro',message='Preencha todos os campos')
    else:
        inserir_form(lista_inserir)
        messagebox.showinfo('Sucesso', message='Os dados foram inseridos')
       
        e_id.delete(0,'end')
        e_fon.delete(0,'end')
        e_mail.delete(0,'end')
        e_id.focus()
        
        #for widget in frame_c.winfo_children():
            #widget.destroy()
        
        mostrar()
        
        # ATUALIZAR
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]
        
        e_id.delete(0,'end')
        e_fon.delete(0,'end')
        e_mail.delete(0,'end')
        e_id.focus()
            
        id= int(treev_lista[0])
        e_id.insert(0,treev_lista[1])
        e_fon.insert(0,treev_lista[2])
        e_mail.insert(0,treev_lista[3])
        ######## ATUALIZAR
        def update():
            nome = e_id.get()
            fone= e_fon.get()
            email= e_mail.get()
        
                    
            lista_atualizar= [nome, fone, email, id]
                    
            if e_id.get()=='':
                messagebox.showerror('Erro',message='Preencha todos os campos')
            else:
                atualizar_form(lista_atualizar)
                messagebox.showinfo('Sucesso',message='Dados atualizados')
                    
                e_id.delete(0,'end')
                e_fon.delete(0,'end')
                e_mail.delete(0,'end')
                
                    
                botao_confirmar.destroy()
                #for widget in frame_c.winfo_children():
                #widget.destroy()
                        
                mostrar()
        botao_confirmar= Button(quadroPesquisar,command=update,text="Confirmar",width=10,height=1,bg="#4B79A1",fg="white",font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE)
        botao_confirmar.place(x=700,y=46)
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')
            
    # FUNCAO DELETAR    
def deleta():
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            treev_lista = treev_dicionario['values']
            valor = treev_lista[0]
            
            deletar_form([valor])
            print(valor)
            
            messagebox.showinfo(message='Os dados foram apagados')
            
            #for widget in frame_c.winfo_children():
                #widget.destroy()
            
            mostrar()
        except IndexError:
            messagebox.showerror('Erro',message='selecione um dos dados na tabela')






# BOTOES CRUD ----
btn_adc= Button(quadroPesquisar,command=adicionar,text="ADICIONAR", bg= "#4B79A1", fg="white", width=30,cursor="hand2")
btn_adc.place(x=470,y=0)

btn_alte= Button(quadroPesquisar,command=atualizar,text="ALTERAR", bg= "#4B79A1", fg="white", width=30,cursor="hand2")
btn_alte.place(x=470,y=40)

btn_del= Button(quadroPesquisar,command=deleta,text="DELETAR", bg= "#4B79A1", fg="white", width=30,cursor="hand2")
btn_del.place(x=470,y=80)

# TREEVIEW
def mostrar():
    global tree 
# creating a treeview with dual scrollbars
    list_header = ['ID','Nome', 'Telefone','email']

    #df_list = selecionar_form()
    
    global tree

    tree = ttk.Treeview(quadroGrid, selectmode="extended",columns=list_header, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(
        quadroGrid, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(
        quadroGrid, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='ns')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    quadroGrid.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center"]
    h=[50,250,250,220]
    n=0

    for col in list_header:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1
    tree.delete(*tree.get_children())
    
    with con:
        cur = con.cursor()
        lista = cur.execute("SELECT * FROM agenda ORDER BY id ASC;")
        for i in lista:
            tree.insert("", END, values=i)
        cur.close()

        
mostrar() 
janela.mainloop()
