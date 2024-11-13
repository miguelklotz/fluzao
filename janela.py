
'''from tkinter import *
class Application:
    def __init__(self,master=None):
        self.widget1 = Frame(master)
        self.widget1.pack(side=RIGHT)
        self.msg = Label(self.widget1,
                         text="Primeiro widget")
        self.msg["font"] = ("Verdana","10","italic","bold")
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Verdana","10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack (side=RIGHT)


root = Tk()
Application(root)
root.mainloop()'''

from tkinter import *
class Application:
    def __init__(self,master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1,
                         text="Primeiro widget")
        self.msg["font"] = ("Calibri","9","italic")
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique Aqui"
        self.sair["font"] = ("Calibri","9")
        self.sair["width"] = 10
        self.sair["command"] = self.mudarTexto
        self.sair.pack ()

    def mudarTexto(self):
        if self.msg["text"] == "Primeiro widget" : 
            self.msg["text"] = "O botão recebeu um clique \nAAAAAAAAAAA\mAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAA\nAAAAAAAAAAA\nAAAAAAAA\nAAAAAAAAAAA\nAAAAAAAAAA\nAAAAAAAAAAA\nAAAAAAAAA"
        else:
            self.msg["text"] = "Primeiro widget"


root = Tk()
Application(root)
root.mainloop()