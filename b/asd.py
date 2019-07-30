print("Be careful not to fall off!")

import tkinter as tk
from tkinter import messagebox as master

class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Action"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="bottom")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        self.master.

root = tk.Tk()

app = Application(master=root)
root.title("Application")
root.resizable(width=False, height=False)
app.master.minsize(width=666, height=666)
app.master.maxsize(width=666, height=666)

app.mainloop()
