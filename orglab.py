
import tkinter as tk
from tkinter import *

#funcoes 
def center(win):
    win.update_idletasks() 
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def infos(): 
    informacoes = Toplevel(window) 
    informacoes.title("Informações sobre SP300LAB001") 
    informacoes.geometry("400x300") 
    Label(informacoes,text ="Informações sobre o dispositivo:").pack()
    center(informacoes)

#layout janela
window = tk.Tk()
frame = tk.Frame(master=window, width=1150, height=600, bg= 'white')
frame.grid()
descricao =tk.Label(master=frame, text="Laboratório de Informática")
descricao.place(x=0, y=0)
sair = tk.Button(master=frame, text="Fechar", command=window.destroy, bg='red')
sair.place(x=1150, y=0)

ladoEsquerdo = tk.Frame(master=frame, width=600, height=600, bg='green')
ladoEsquerdo.place(x=0,y=40)
ladoDireito = tk.Frame(master=frame, width=600, height=600, bg='blue')
ladoDireito.place(x=600,y=40)
porta = tk.Frame(master=frame, width=20, height=80, bg='brown')
porta.place(x=0, y=480)


#layout dos computadores
for i in range(8):
    for j in range(5):
        fileiraesq = tk.Frame(master=ladoEsquerdo,relief=tk.RAISED,borderwidth=1)
        fileiraesq.grid(row=i, column=j, padx=5, pady=5)
        fileiradir = tk.Frame(master=ladoDireito,relief=tk.RAISED,borderwidth=1)
        fileiradir.grid(row=i, column=j, padx=5, pady=5)
        
        
        computeresq = tk.Button(master=fileiraesq, text="SP300LAB001",command=infos)
        computeresq.pack(padx=5, pady=5)
        computerdir = tk.Button(master=fileiradir, text="SP300LAB001",command=infos)
        computerdir.pack(padx=5, pady=5)
        
center(window)
window.mainloop()
