import tkinter as tk


window = tk.Tk()
greeting = tk.Label(text="Python rocks!")
greeting["pady"] = 350
greeting["padx"] = 500
greeting.pack()

window.mainloop()