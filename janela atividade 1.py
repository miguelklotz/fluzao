from tkinter import *

class Application:
    def __init__(self,lista,master=None):
        
        for n in lista:
            print(n)
        #Criando elementos na janela
            self.widget1 = Frame(master)
            self.widget1.pack()
            self.msg = Label(self.widget1,
                            text=n.exibir_info())
            self.msg["font"] = ("Verdana","12","italic")
            self.msg.pack()
        

class Produto:
    nome = ""
    descricao = ""
    preco = 0.0
    
    def __init__(self,nome,descricao,preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
    
    def exibir_info(self):
        return(f"Nome:{self.nome}\ndescrição: {self.descricao}\npreço: {self.preco}")
                


suco_uva = Produto("suco_uva ","bom pra saude ",100)
suco_uva.exibir_info()
lista = []
lista.append(Produto("suco_uva ","bom pra saude ",100))
lista.append(Produto("Tirolzinho ","muito bom  ",2.50))
lista.append(Produto("Água ","hoje em dia ta bom  ",1.50))
lista.append(Produto("knodel doce ","chocolate de qualidade  ",10.50))

root = Tk()
Application(lista,root)
root.mainloop()