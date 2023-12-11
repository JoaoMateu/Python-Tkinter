import tkinter as tk

def on_button1_click():
    print("Botão 1 clicado!")

def on_button2_click():
    print("Botão 2 clicado!")

# Criar a janela principal
root = tk.Tk()
root.title("Dois Botões")

# Criar um frame para conter os botões
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Criar o primeiro botão
button1 = tk.Button(frame, text="Botão 1", command=on_button1_click)
button1.pack(side=tk.LEFT, padx=5)

# Criar o segundo botão
button2 = tk.Button(frame, text="Botão 2", command=on_button2_click)
button2.pack(side=tk.LEFT, padx=5)

# Iniciar o loop principal da interface gráfica
root.mainloop()
