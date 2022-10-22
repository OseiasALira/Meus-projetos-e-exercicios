"""
Este codigo faz parte do meu aprendizado em python, todo material aqui é reproduzido a partir
Curso Python Tkinter - RfZorzi.
Este curso esta disponivel no YouTube e segue o link abaixo.

https://www.youtube.com/watch?v=RtrZcoVD1WM&list=PLqx8fDb-FZDFznZcXb_u_NyiQ7Nai674-&index=1

IMPORTANTE: Este código não é de minha autoria e estou utilizando apenas como proposito de estudo e
desenvolvimento pessoal.

"""

import sqlite3
from tkinter import *
from tkinter import ttk

root = Tk()  # cria tela

class Funcs():
    """Funções do aplicativo"""
    def limpa_tela(self):
        """Limpar dados da tela de cadastro"""
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    def conecta_bd(self):
        """Coneca banco de dados"""
        self.conn = sqlite3.connect("clientes.db")
        self.cursor = self.conn.cursor()
    def desconecta_bd(self):
        """Desconecta bando de dados"""
        self.conn.close()
    def monta_tabelas(self):
        """Cria tabela se ela não existir"""
        self.conecta_bd()
        print("Conectando ao banco de dados")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)        
            );
        """)
        self.conn.commit()
        print("Banco de dados criado")
        self.desconecta_bd()
    def variaveis(self): #Pylint reclama que os "entrys" não são membros
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()
    def add_clientes(self):
        """Adiciona os dados coletados ao banco de dados
        variáveis para armazenar os dados de entrada da tela
        Coleta os dados ao ser chamando pelo metódo na classe Aplication - 
        entendi, mas não sei se meu pensamento esta correto e preciso fixar esse tipo de recurso
        """
        self.variaveis()

        self.conecta_bd()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
             VALUES (?, ?, ?)""", (self.nome, self.telefone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):
        """Limpa a lista da TreeView e adiciona os dados do banco de dados em ordem alfabetica"""

        self.lista_cli.delete(*self.lista_cli.get_children()) # limpando a treeview(lista_cli)
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.lista_cli.insert("", END, values=i)
        self.desconecta_bd()
    def on_double_clic(self, event):
        """Preenche os dados ao dar duplo clique na Treeview"""
        self.limpa_tela()
        self.lista_cli.selection() #Pylint reclama (no-member),
                                   #pois são atributos da classe Aplication

        for n in self.lista_cli.selection():
            col1, col2, col3, col4 = self.lista_cli.item(n, 'values')
            self.codigo_entry.insert(END, col1) 
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)
    def deleta_cliente(self):
        """Deleta do banco de dados a seleção preenchida"""
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" DELETE FROM clientes WHERE cod = ? """, (self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()
    def altera_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
                         WHERE cod = ?""", (self.nome, self.telefone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
class Aplication(Funcs):
    """Classe que contem as configurações do aplicativo"""

    def __init__(self):
        self.root = root  # Criando o acesso da instancia dentro da nossa classe de aplicação
        self.tela()  # Chamando metodo de configuração da tela
        self.frames_da_tela()  # Instanciando frames da janela
        self.widgets_frame1()  # Instanciando botoes dos frames
        self.lista_frame2()
        self.monta_tabelas()
        self.select_lista()
        root.mainloop()  # Mantem nossa tela aberta

    def tela(self):
        """Configuração da tela aprensentada"""

        self.root.title("Cadastro de Clientes")  # Barra de título
        # Configuranção de fundo, cor
        self.root.configure(background='#1e3743')
        self.root.geometry("700x500")  # Tamanho inicial da tela
        self.root.resizable(True, True)  # Responsividade (x,y)
        # Tamanho máximo de redimencionamento
        self.root.maxsize(width=900, height=700)
        # Tamanho minimo de redimencionamento
        self.root.minsize(width=400, height=300)

    # aula 2 2:16 - REVISAR - place pack grid
    def frames_da_tela(self):
        """Configurando o layout da janela"""

        self.frame_1 = Frame(self.root,  # Instanciando uma caixa dentro da janela
                             bd=4,  # Tamanho da borda
                             bg='#dfe4ee',  # Cor do Background
                             highlightbackground='#759fe6',  # Cor da borda interna
                             highlightthickness=3)  # Largura da borda interna
        self.frame_1.place(relx=0.015,
                           rely=0.025,
                           relwidth=0.97,
                           relheight=0.46)  # Posição relativa

        self.frame_2 = Frame(self.root,  # Instanciando uma caixa dentro da janela
                             bd=4,  # Tamanho da borda
                             bg='#dfe4ee',  # Cor do Background
                             highlightbackground='#759fe6',  # Cor da borda interna
                             highlightthickness=3)  # Largura da borda interna
        self.frame_2.place(relx=0.015,
                           rely=0.5,
                           relwidth=0.97,
                           relheight=0.46)  # Posição relativa

    def widgets_frame1(self):
        """Criando os botões do frame 1"""

        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=2.5, bg="#107db2",fg= "white",
                                font= ("verdana", 8, "bold"), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=2.5, bg="#107db2",fg= "white",
                                font= ("verdana", 8, "bold"))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_novo = Button(self.frame_1, text="Novo", bd=2.5, bg="#107db2",fg= "white",
                                font= ("verdana", 8, "bold"), command=self.add_clientes)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_alterar = Button(self.frame_1, text="Alterar", bd=2.5, bg="#107db2",fg= "white",
                                font= ("verdana", 8, "bold"), command=self.altera_cliente)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_apagar = Button(self.frame_1, text="Apagar", bd=2.5, bg="#107db2",fg= "white",
                                font= ("verdana", 8, "bold"), command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
        # Labels e entrys do frame 1
        self.lb_codigo = Label(self.frame_1, text="Código", bg="#dfe4ee", fg="#107db2")
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        self.lb_nome = Label(self.frame_1, text="Nome", bg="#dfe4ee", fg="#107db2")
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.85)

        self.lb_telefone = Label(self.frame_1, text="Telefone", bg="#dfe4ee", fg="#107db2")
        self.lb_telefone.place(relx=0.05, rely=0.60)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.70, relwidth=0.40)

        self.lb_cidade = Label(self.frame_1, text= "Cidade", bg="#dfe4ee", fg="#107db2")
        self.lb_cidade.place(relx=0.5, rely=0.60)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

    def lista_frame2(self):
        """Treeview"""
        #Instanciação e configuração da quantidade de coluna e altura
        self.lista_cli = ttk.Treeview(self.frame_2, height=3, column=("col1, col2, col3, col4"))

        #Definindo cabeçalho das colunas
        self.lista_cli.heading("#0", text="")
        self.lista_cli.heading("#1", text="Codigo")
        self.lista_cli.heading("#2", text="Nome")
        self.lista_cli.heading("#3", text="Telefone")
        self.lista_cli.heading("#4", text="Cidade")

        #Definindo largura das colunas *** procurar um padrão pra isso
        self.lista_cli.column("#0", width=1)
        self.lista_cli.column("#1", width=50)
        self.lista_cli.column("#2", width=200)
        self.lista_cli.column("#3", width=125)
        self.lista_cli.column("#4", width=125)

        #Definindo posicionamento da lista no frame
        self.lista_cli.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.85)

        #Instanciando barra de rolagem
        self.scrool_lista = Scrollbar(self.frame_2, orient='vertical')

        #Atrelando a barra de rolagem a uma lista
        self.lista_cli.configure(yscroll=self.scrool_lista.set)

        #Posicionando a barra de rolagem
        self.scrool_lista.place(relx=0.96, rely=0.0125, relwidth=0.03, relheight=0.8475)

        self.lista_cli.bind("<Double-1>", self.on_double_clic)


Aplication()
