from tkinter import *

#definindo o setup 
setup= Tk()
altura= 139
largura=500
setup.title('Conversor de Celsius em Kelvin')

#centralizando o setup na tela do usuario.
altura_max= setup.winfo_screenheight()
largura_max= setup.winfo_screenwidth()
new_x=(largura_max/2)-(largura/2)
new_y= (altura_max/2)-(altura/2)
setup.geometry("%dx%d+%d+%d"%(largura,altura,new_x,new_y))

#criando o frame que ira armazenar as informações
frame=Frame(setup,bg="navy blue")
def Calculo():
    cal= float(get_cel.get())
    kel= cal + 273.15
    label_resp["text"]=" Temperatura em Kelvin: "+ str(round(kel,2))+ " K"
   
label=Label(frame,text='Conversor de Celsius para Kelvin',font='Times 16',justify=LEFT,bg="navy blue",fg="white")
label.grid(padx=110)
label_Cel=Label(frame,text="Informe Temp em Celsius:",font="Times 14",justify=LEFT,bg="navy blue",fg="white")
label_Cel.grid(sticky=W)
label_resp=Label(frame,font="Times 14",fg="white",bg="Navy Blue")
label_resp.grid()

get_cel=Entry(frame)
get_cel.grid()
    
button=Button(frame,text="Converter",font='times 14',justify=CENTER,command=Calculo).grid()


frame.grid()
setup.mainloop()
