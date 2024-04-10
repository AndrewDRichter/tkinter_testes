from usuarios import Usuarios
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["pady"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["pady"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["pady"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["pady"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["pady"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container5.pack()

        self.container8 = Frame(master)
        self.container8["pady"] = 20
        self.container8["pady"] = 10
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lbl_id = Label(self.container2,
                            text="idUsuario:", font=self.fonte, width=10)
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

    def buscarUsuario(self):
        pass


root = Tk()
Application(root)
root.mainloop()