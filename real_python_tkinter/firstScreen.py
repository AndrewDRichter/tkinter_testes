import tkinter as tk


window = tk.Tk()
window.title("Bg setting")
img = tk.PhotoImage(file="bg.png")
tk.Label(window, image= img).pack()
greeting = tk.Label(text="Python rocks!")
greeting["pady"] = 350
greeting["padx"] = 500
greeting.pack()

window.mainloop()