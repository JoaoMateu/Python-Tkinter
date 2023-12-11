from cProfile import label
from tkinter import *

#criando a classe frame que ira ser base para 
class frame1 (Frame):
    def __init__(self,widget):
        
        super().__init__(widget)
        self["width"] = 400
        self["height"] = 300
        self["bd"] = 5
        self["relief"] = SOLID
        
        self.user = StringVar()
        self.nome = StringVar()
        
        nome = Label(self, text= 'Nome: ',justify= LEFT)
        box_nome=Entry(self,textvariable=self.nome)
        nome.grid(row = 0,column = 0)
        box_nome.grid(row=0, column=1)
        
        senha = Label(self, text = "Senha: ",justify= LEFT)
        box_senha = Entry(self)
        senha.grid(row = 1, column= 0)
        box_senha.grid(row=1,column=1)
       
        
        label_text=Label(self,textvariable=self.user,font='times 13')
        label_text.grid()
        
        botao = Button(self,text='Entre',font= "times 14",command= self.entrar)
        botao.grid(row=2,column=1,sticky=S)
        
    def entrar(self):
        self.user.set('Olá ' + self.nome.get())
        







window = Tk()
window.title('Projeto')

frame=frame1(window).grid()
window.mainloop()
