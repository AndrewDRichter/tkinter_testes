from usuarios import Usuarios
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.app_version = 1.0
        self.fonte = ("Verdana", "8")

        self.ver_container = Frame(master)
        self.ver_container.pack()

        self.lbl_version = Label(self.ver_container, text=self.app_version, padx=100)
        self.lbl_version.pack(side=LEFT)

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 100
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 100
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 100
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 100
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["padx"] = 100
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["padx"] = 100
        self.container7["pady"] = 5
        self.container7.pack()
        self.container5.pack()

        self.container8 = Frame(master)
        self.container8["padx"] = 100
        self.container8["pady"] = 10
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["padx"] = 100
        self.container9["pady"] = 10
        self.container9.pack()

        self.container10 = Frame(master)
        self.container10["padx"] = 100
        self.container10["pady"] = 10
        self.container10.pack()

        self.container11 = Frame(master)
        self.container11["pady"] = 15
        self.container11.pack()

        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lbl_id = Label(self.container2,
                            text="id:", font=self.fonte, width=10)
        self.lbl_id.pack(side=LEFT)

        self.txt_id = Entry(self.container2)
        self.txt_id["width"] = 10
        self.txt_id["font"] = self.fonte
        self.txt_id.pack(side=LEFT)

        self.btn_buscar = Button(self.container2, text="Buscar", font=self.fonte, width=10, padx=10)
        self.btn_buscar["command"] = self.buscarUsuario
        self.btn_buscar.pack(side=RIGHT)

        self.lbl_nome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lbl_nome.pack(side=LEFT)

        self.txt_nome = Entry(self.container3)
        self.txt_nome["width"] = 25
        self.txt_nome["font"] = self.fonte
        self.txt_nome.pack(side=LEFT)

        self.lbl_telefone = Label(self.container4, text="Telefone:",
        font=self.fonte, width=10)
        self.lbl_telefone.pack(side=LEFT)

        self.txt_telefone = Entry(self.container4)
        self.txt_telefone["width"] = 25
        self.txt_telefone["font"] = self.fonte
        self.txt_telefone.pack(side=LEFT)

        self.lbl_email= Label(self.container5, text="E-mail:",
        font=self.fonte, width=10)
        self.lbl_email.pack(side=LEFT)

        self.txt_email = Entry(self.container5)
        self.txt_email["width"] = 25
        self.txt_email["font"] = self.fonte
        self.txt_email.pack(side=LEFT)

        self.lbl_usuario= Label(self.container6, text="Usuário:",
        font=self.fonte, width=10)
        self.lbl_usuario.pack(side=LEFT)

        self.txt_usuario = Entry(self.container6)
        self.txt_usuario["width"] = 25
        self.txt_usuario["font"] = self.fonte
        self.txt_usuario.pack(side=LEFT)

        self.lbl_senha= Label(self.container7, text="Senha:",
        font=self.fonte, width=10)
        self.lbl_senha.pack(side=LEFT)

        self.txt_senha = Entry(self.container7)
        self.txt_senha["width"] = 25
        self.txt_senha["show"] = "*"
        self.txt_senha["font"] = self.fonte
        self.txt_senha.pack(side=LEFT)

        self.lbl_confirma_senha= Label(self.container8, text="Confirmar senha:",
        font=self.fonte, width=15)
        self.lbl_confirma_senha.pack(side=LEFT)

        self.txt_confirma_senha = Entry(self.container8)
        self.txt_confirma_senha["width"] = 20
        self.txt_confirma_senha["show"] = "*"
        self.txt_confirma_senha["font"] = self.fonte
        self.txt_confirma_senha.pack(side=LEFT)

        self.btn_Insert = Button(self.container9, text="Inserir",
        font=self.fonte, width=12)
        self.btn_Insert["command"] = self.inserirUsuario
        self.btn_Insert.pack (side=LEFT)

        self.btn_Alterar = Button(self.container9, text="Alterar",
        font=self.fonte, width=12)
        self.btn_Alterar["command"] = self.alterarUsuario
        self.btn_Alterar.pack (side=LEFT)

        self.btn_Excluir = Button(self.container9, text="Excluir",
        font=self.fonte, width=12)
        self.btn_Excluir["command"] = self.excluirUsuario
        self.btn_Excluir.pack(side=LEFT)

        self.lbl_msg = Label(self.container10, text="")
        self.lbl_msg["font"] = ("Verdana", "9", "italic")
        self.lbl_msg.pack()

        self.lbl_lista = Label(self.container11, text="")
        self.lbl_lista.pack()

    def inserirUsuario(self):
        user = Usuarios()

        user.nome = self.txt_nome.get()
        user.telefone = self.txt_telefone.get()
        user.email = self.txt_email.get()
        user.usuario = self.txt_usuario.get()
        user.senha = self.txt_senha.get()
        confirma_senha = self.txt_confirma_senha.get()
        
        if user.senha == confirma_senha:
            self.lbl_msg["text"] = user.insertUser()

        self.txt_id.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_telefone.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_usuario.delete(0, END)
        self.txt_senha.delete(0, END)
        self.txt_confirma_senha.delete(0, END)

    def alterarUsuario(self):
        user = Usuarios()

        user.id = self.txt_id.get()
        user.nome = self.txt_nome.get()
        user.telefone = self.txt_telefone.get()
        user.email = self.txt_email.get()
        user.usuario = self.txt_usuario.get()
        user.senha = self.txt_senha.get()

        self.lbl_msg["text"] = user.updateUser()

        self.txt_id.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_telefone.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_usuario.delete(0, END)
        self.txt_senha.delete(0, END)
        self.txt_confirma_senha.delete(0, END)

    def excluirUsuario(self):
        user = Usuarios()

        user.id = self.txt_id.get()

        self.lbl_msg["text"] = user.deleteUser()

        self.txt_id.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_telefone.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_usuario.delete(0, END)
        self.txt_senha.delete(0, END)
        self.txt_confirma_senha.delete(0, END)

    def buscarUsuario(self):
        user = Usuarios()

        id = self.txt_id.get()

        if id == "":
            self.lbl_msg["text"] = "Digite o id a ser buscado"
        elif id.isalpha:
            self.lbl_msg["text"] = "Digite um número"
        else:

            self.lbl_msg["text"] = user.selectUser(id)

            self.txt_id.delete(0, END)
            self.txt_id.insert(INSERT, user.id)

            self.txt_nome.delete(0, END)
            self.txt_nome.insert(INSERT, user.nome)

            self.txt_telefone.delete(0, END)
            self.txt_telefone.insert(INSERT,user.telefone)

            self.txt_email.delete(0, END)
            self.txt_email.insert(INSERT, user.email)

            self.txt_usuario.delete(0, END)
            self.txt_usuario.insert(INSERT, user.usuario)

            self.txt_senha.delete(0, END)
            self.txt_senha.insert(INSERT,user.senha)
            self.txt_confirma_senha.delete(0, END)

            
    def mostrarUsuarios(self):
        pass


root = Tk()
Application(root)
root.mainloop()