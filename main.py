from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# importando pillow
from PIL import Image,ImageTk

# importando Tkcalendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# Importando view
from view import *


#cores 
co0 = "#000000" # preto (botoes)
co1 = "#feffff" # branca
co2 = "#4fa882" # verde
co3 = "#38576b" # valor
co4 = "#000000" # azul letra
co5 = "#e86636" # - profit
co6 = "#038cfc" # azul
co7 = "#3fbfb9" # verde
co8 = "#263238" # + verde
co9 = "#e9edf5" # + verde
co10 = '#F0F0F8' # cinza
co11 = '#1F5372'
co12 = '#708090'
# criando janela

janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")


# criando frames

framecima = Frame(janela, width=1043, height=50, bg=co10,relief=FLAT )
framecima.grid(row=0, column=0)

framemeio = Frame(janela, width=1043, height=303, bg=co10, pady=20, relief=FLAT )
framemeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

framebaixo = Frame(janela, width=1043, height=300, bg=co10, relief=FLAT )
framebaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# Criando funcoes -------------------------
global tree
#Funcao Inserir
def inserir():
    global imagem, imagem_string, l_imagem

    nome = e_nome.get()
    local = e_local.get()
    descricao = e_descricao.get()
    model = e_model.get()
    data = e_cal.get()
    valor = e_valor.get()
    serie = e_serie.get()
    imagem = imagem_string

    lista_inserir = [nome, local, descricao, model, data, valor, serie, imagem]

    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos', )
            return
        
    inserir_form(lista_inserir)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso', )
        
    e_nome.delete(0,'end')
    e_local.delete(0,'end')
    e_descricao.delete(0,'end')
    e_model.delete(0,'end')
    e_cal.delete(0,'end')
    e_valor.delete(0,'end')
    e_serie.delete(0,'end')
    

    mostrar()


# Funcao atualizar
def atualizar():
    global imagem, imagem_string, l_imagem
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]
        
        e_nome.delete(0,'end')
        e_local.delete(0,'end')
        e_descricao.delete(0,'end')
        e_model.delete(0,'end')
        e_cal.delete(0,'end')
        e_valor.delete(0,'end')
        e_serie.delete(0,'end')

        id = int(treev_lista[0])
        e_nome.insert(0,treev_lista[1])
        e_local.insert(0,treev_lista[2])
        e_descricao.insert(0,treev_lista[3])
        e_model.insert(0,treev_lista[4])
        e_cal.insert(0,treev_lista[5])
        e_valor.insert(0,treev_lista[6])
        e_serie.insert(0,treev_lista[7])
        imagem_string = treev_lista[8]

        
        
        def update():
            global imagem, imagem_string, l_imagem

            nome = e_nome.get()
            local = e_local.get()
            descricao = e_descricao.get()
            model = e_model.get()
            data = e_cal.get()
            valor = e_valor.get()
            serie = e_serie.get()
            imagem = imagem_string

            if imagem =='':
                imagem = e_serie.insert(0,treev_lista[7])

            lista_atualizar = [nome, local, descricao, model, data, valor, serie, imagem,id]

            for i in lista_atualizar:
                if i=='':
                    messagebox.showerror('Erro', 'Preencha todos os campos', )
                    return
                
            atualizar_form(lista_atualizar)
            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso', )

            e_nome.delete(0,'end')
            e_local.delete(0,'end')
            e_descricao.delete(0,'end')
            e_model.delete(0,'end')
            e_cal.delete(0,'end')
            e_valor.delete(0,'end')
            e_serie.delete(0,'end')

            b_confirmar.destroy()
            mostrar()

        b_confirmar = Button(framemeio,command=update, width=13, text= 'Confirmar'.upper(), overrelief=RIDGE, font=('Ivy 8 bold' ), bg=co11, fg=co1)
        b_confirmar.place(x=330, y=185)

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados nsa tabela', )
        return

# Funcao deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        deletar_form([valor])

        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso', )

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados nsa tabela', )
        return

# Funcao para escolher imagem
global imagem, imagem_string, l_imagem

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    # abrindo imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(framemeio, image=imagem, bg=co10, fg=co4 )
    l_imagem.place(x=450, y=10)    


# Funcao para ver imagem
def ver_imagem():
    global imagem, imagem_string, l_imagem

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']

    valor = [int(treev_lista[0])]

    item = ver_item(valor)

    imagem = item[0][8]

    # abrindo imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(framemeio, image=imagem, bg=co10, fg=co4 )
    l_imagem.place(x=450, y=10)


#trabalhando no frame cima -------------------------

# abrindo imagem
app_img = Image.open('icon.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(framecima, image=app_img, text= ' Inventário de Patrimônio', width=900,compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co10, fg=co11 )
app_logo.place(x=0, y=0)

#trabalhando no frame meio --------------------------

#criando entradas 
l_nome = Label(framemeio, text= 'Nome', height=1, anchor=NW, font=('Ivy 10 bold' ), bg=co10, fg=co4)
l_nome.place(x=10, y=10)

e_nome = Entry(framemeio, width=30, justify='left', relief=SOLID, bg=co10,)
e_nome.place(x=130, y=11)

l_local = Label(framemeio, text= 'Local', height=1, anchor=NW, font=('Ivy 10 bold' ), bg=co10, fg=co4)
l_local.place(x=10, y=40)

e_local = Entry(framemeio, width=30, justify='left', relief=SOLID, bg=co10)
e_local.place(x=130, y=41)

l_descricao = Label(framemeio, text= 'Descrição', height=1, anchor=NW, font=('Ivy 10 bold' ), bg=co10, fg=co4)
l_descricao.place(x=10, y=70)

e_descricao = Entry(framemeio, width=30, justify='left', relief=SOLID, bg=co10)
e_descricao.place(x=130, y=71)

l_model = Label(framemeio, text= 'Marca', height=1, anchor=NW, font=('Ivy 10 bold' ), bg=co10, fg=co4)
l_model.place(x=10, y=100)

e_model = Entry(framemeio, width=30, justify='left', relief=SOLID, bg=co10)
e_model.place(x=130, y=101)


l_cal = Label(framemeio, text= 'Data da compra', height=1, anchor=NW, font=('Ivy 10 bold' ), bg=co10, fg=co4)
l_cal.place(x=10, y=130)
e_cal = DateEntry(framemeio, width=12, background='darkblue', borderwidth=2, year=2023,)
e_cal.place(x=130, y=131)

l_valor = Label(framemeio, text= 'Valor da compra', height=1, anchor=NW, font=('Ivy 10 bold' ), bg=co10, fg=co4)
l_valor.place(x=10, y=160)

e_valor= Entry(framemeio, width=30, justify='left', relief=SOLID, bg=co10)
e_valor.place(x=130, y=161)

l_serial = Label(framemeio, text= 'Número de série', height=1, anchor=NW, font=('Ivy 10 bold' ), bg=co10, fg=co4)
l_serial.place(x=10, y=190)

e_serie= Entry(framemeio, width=30, justify='left', relief=SOLID, bg=co10)
e_serie.place(x=130, y=191)

#Criando botoes--------------------------

# botao carregar
l_carregar = Label(framemeio, text= 'Imagem do item', height=1, anchor=NW, font=('Ivy 10 bold' ), bg=co10, fg=co4,)
l_carregar.place(x=10, y=220)

b_carregar = Button(framemeio, command=escolher_imagem, width=29, text= 'carregar'.upper(), compound= CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8' ), bg=co10, fg=co0)
b_carregar.place(x=130, y=221)

# botao Inserir
img_add = Image.open('add.png')
img_add = img_add .resize((20,20))
img_add = ImageTk.PhotoImage(img_add)

b_inserir = Button(framemeio, command=inserir, image= img_add, width=95, text= '  Adicionar'.upper(), compound= LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8' ), bg=co10, fg=co0)
b_inserir.place(x=330, y=10)


# botao Atualizar
img_update = Image.open('update.png')
img_update = img_update .resize((20,20))
img_update = ImageTk.PhotoImage(img_update)

b_update = Button(framemeio,command=atualizar, image= img_update, width=95, text= '  Atualizar'.upper(), compound= LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8' ), bg=co10, fg=co0)
b_update.place(x=330, y=50)


# botao Deletar
img_delete = Image.open('delete.png')
img_delete = img_delete .resize((20,20))
img_delete = ImageTk.PhotoImage(img_delete)

b_delete = Button(framemeio,command=deletar, image= img_delete, width=95, text= '  Deletar'.upper(), compound= LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8' ), bg=co10, fg=co0)
b_delete.place(x=330, y=90)


# botao Ver imagem
img_item = Image.open('item.png')
img_item = img_item .resize((20,20))
img_item = ImageTk.PhotoImage(img_item)

b_item = Button(framemeio, command=ver_imagem, image= img_item, width=95, text= '  Ver item'.upper(), compound= LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8' ), bg=co10, fg=co0)
b_item.place(x=330, y=221)

# lables Quantidade total e Valores
l_total = Label(framemeio, text= '', width=14, height=2, anchor=CENTER, font=('Ivy 17 bold' ), bg=co11, fg=co1)
l_total.place(x=650, y=17)

l_total_ = Label(framemeio, text= '  Valor Total de todos os itens  ', height=1, anchor=NW, font=('Ivy 10 bold' ), bg=co11, fg=co1)
l_total_.place(x=650, y=12)


l_qtd = Label(framemeio, text= '', width=14, height=2, pady=8, anchor=CENTER, font=('Ivy 17 bold' ), bg=co11, fg=co1)
l_qtd.place(x=650, y=90)

l_qtd_ = Label(framemeio, text= '  Quantidade Total de itens  ', height=1, anchor=NW, font=('Ivy 10 bold' ), bg=co11, fg=co1)
l_qtd_.place(x=650, y=92)



# tabela -----------------------------------------------------------
def mostrar():
    global tree


    tabela_head = ['#Item','Nome',  'Sala/Área','Descrição', 'Marca/Modelo', 'Data da compra','Valor da compra', 'Número de série']

    lista_itens = ver_form()


    tree = ttk.Treeview(framebaixo, selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(framebaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(framebaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    framebaixo.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center", 'center']
    h=[40,150,100,160,130,100,100, 100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)


    quantidade = []

    for iten in lista_itens:
        quantidade.append(iten[6])

    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd['text'] = Total_itens

mostrar()


janela.mainloop()
