from tkinter import * 

class Application:
    def __init__(self, master=None):
        self.container1 = Frame(master)
        self.container1.pack()
        
        self.lbl = Label(self.container1, text="12345648789584321321324654", width=75, bg="Blue", fg="White")
        self.lbl.pack(side=LEFT)

        self.lbl1 = Label(self.container1, text="12345648789584321321324654", width=75, bg="Yellow", fg="Black")
        self.lbl1.pack(side=LEFT)

root = Tk()
Application(root)
root.mainloop()