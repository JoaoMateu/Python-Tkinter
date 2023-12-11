from tkinter import *

janela = Tk()
# Configurando a primeira janela.
janela.title("Teste")
janela.iconbitmap("C:/Users/marco/OneDrive/UFCG/Programação/Ras/Missao/Tkinter/imagens/icon.ico")
janela.resizable(1,1)
janela["bg"] = "#0000ff"
# Centralizando a janela.
largura = 540
altura = 400
x = janela.winfo_screenwidth()
y = janela.winfo_screenheight()
new_x = (x/2) - (largura/2)
new_y = (y/2) - (altura/2)
janela.geometry("%dx%d+%d+%d" %(largura, altura, new_x, new_y))
# Configurando o primeiro botão.
bnt = Button(janela, 
             text = "Sair", 
             bd = 5, 
             relief = "ridge",
             width = 20, 
             height = 1, 
             anchor = SW,
             bg = "white",
             font = "calibri 13 bold",
             fg = "red",
             command = lambda: exit()
             ).grid(row = 0, column = 0, sticky = W)

# Configurando o primeiro label.
label = Label(janela,
              text = ("Testando o primeiro label."),
              font = "times 13 bold italic",
              fg = "#00ff00",
              bg = "#ffffff",
              bd = 3,
              relief = "groove",
              width = 30,
              height = 3,
              anchor = CENTER,
              ).grid(row = 1, column = 1, sticky = E)

label2 = Label(janela,
              text = ("Testando o segundo label.\nSEgunndo texto"),
              font = "times 13 bold italic",
              fg = "#00ff00",
              bg = "#ffffff",
              bd = 3,
              relief = "groove",
              padx = 20,
              pady = 5,
              justify = LEFT
              ).grid(row = 2, column = 0)

texto = StringVar()
texto.set("Testando grid.")

label3 = Label(janela,
               bg = "red",
               fg = "white",
               font = "arial 13 italic",
               textvariable = texto).grid(row = 3, column = 0)

label4 = Label(janela,
               bg = "white",
               fg = "red",
               font = "arial 13 italic",
               textvariable = texto).grid(row = 3, column = 1)

label5 = Label(janela, bg = "black").grid(row = 4, columnspan = 2, sticky = "we")

# Configurando janela para login de usuarios.   

def executar():
    text_user["text"] = get_user.get()
    text_pass["text"] = get_pass.get()
    
frame = Frame(janela)
 
user = Label(janela, text = "Usuário:", font = "Calibri 13 bold", fg = "red", bg = "white").grid(row = 5, columnspan = 1, sticky = "we")
password = Label(janela, text = "Senha:", font = "Calibri 13 bold", fg = "red", bg = "white").grid(row = 6, columnspan = 1, sticky = "we")

get_user = Entry(janela)
get_pass = Entry(janela)
get_user.grid(row = 5, column = 1, columnspan = 1, sticky = "we")
get_pass.grid(row = 6, column = 1, columnspan = 1, sticky = "we")

get_user.focus()
    
text_user = Label(janela)
text_pass = Label(janela)
text_user.grid(row = 8, column = 0, columnspan = 1, sticky = "we")
text_pass.grid(row = 8, column = 1, columnspan = 1, sticky = "we")


login = Button(janela, text = "Login", fg = "black", font = "Calibri 13 bold", width = 20, height = 1, command = executar).grid(row = 7, column = 1, sticky = E)




janela.mainloop()