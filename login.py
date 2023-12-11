from tkinter import *#Biblioteca do Tkinter
#Criando um menu grafico 

janela = Tk() 
altura = 150
largura = 300
frame = Frame(janela,bg="Navy blue")

largura_max = janela.winfo_screenwidth()
altura_max = janela.winfo_screenheight()
new_x = (largura_max/2) - (largura/2)
new_y =  (altura_max/2) - (altura/2)

#irá criar um titulo para o programa 
janela.title('Teste do Programa')
#coloca uma foto mini para o programa
janela.iconbitmap("E:/Programas/ft.ico")
janela.geometry("%dx%d+%d+%d"%(largura,altura,new_x,new_y))

label = Label(frame,text='Usuario:',font='times 14',padx= 5,pady=5,justify= LEFT,bg="Navy Blue")
label.grid(row=0, column=0,sticky=W)
label2 =Label(frame,text='Password:',font='times 14',padx=5,pady=5,justify=LEFT).grid(row=1, column=0,sticky= W)

def executar():
    label_user['text']= User.get()
    label_pass['text']=Password.get()
    
botao=Button(frame,text="entrar",font="times 14",justify=CENTER,command=executar).grid(row=2,column=1)

User= Entry(frame)
Password=Entry(frame)
User.grid(row=0,column=1)
Password.grid(row=1,column=1)
User.focus()


#print(largura_max,altura_max)
label_user=Label(frame)
label_user.grid()
label_pass=Label(frame)
label_pass.grid()


frame.grid()
janela.mainloop()