import tkinter as tk
from tkinter import PhotoImage

# Funções
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
    informacoes = tk.Toplevel() 
    informacoes.title("Informações sobre SP300LAB001") 
    informacoes.geometry("400x300") 
    tk.Label(informacoes, text="Informações sobre o dispositivo:").pack()
    center(informacoes)

def lab4():
    window = tk.Tk()
    window.title("ORGLAB - ORGANIZAÇÃO DE LABORATÓRIOS")
    window.geometry("1150x600")
    window.minsize(1150, 400)
    window.maxsize(1150, 400)
    frame = tk.Frame(master=window, width=1150, height=600)
    frame.grid()
    descricao = tk.Label(master=frame, text="LABORATÓRIO DE INFORMÁTICA 4")
    descricao.place(x=500, y=10)
    ladoEsquerdo = tk.Frame(master=frame, width=600, height=600)
    ladoEsquerdo.place(x=60, y=30)
    ladoDireito = tk.Frame(master=frame, width=600, height=600)
    ladoDireito.place(x=600, y=30)

    # layout dos computadores
    for i in range(8):
        for j in range(5):
            # ESQUERDA:
            fileiraesq = tk.Frame(master=ladoEsquerdo, relief=tk.RAISED, borderwidth=1)
            fileiraesq.grid(row=i, column=j, padx=5, pady=5)
            computeresq = tk.Button(master=fileiraesq, text="SP300LAB001", command=infos, compound=tk.TOP, border=0)
            computeresq.pack(padx=5, pady=5)
            fileiradir = tk.Frame(master=ladoDireito, relief=tk.RAISED, borderwidth=1)
            fileiradir.grid(row=i, column=j, padx=5, pady=5)
            computerdir = tk.Button(master=fileiradir, text="SP300LAB001", command=infos, compound=tk.TOP, border=0)
            computerdir.pack(padx=5, pady=5)

    center(window)
    window.mainloop()

def homepage():
    home = tk.Tk()
    home.title("ORGLAB - LABORATÓRIOS")
    home.geometry("600x200")
    home.minsize(600, 200)
    home.maxsize(600, 200)

    # Carrega a imagem globalmente
    global photoimage
    note_photo = PhotoImage(file="images/note.png")
    photoimage = note_photo.subsample(2, 2)

    frame1 = tk.Frame(master=home, width=200, height=400)
    frame1.place(x=0, y=0)
    notebook1 = tk.Button(master=frame1, text="LABORATÓRIO 4", image=photoimage, compound=tk.TOP, width=150, height=150, command=lab4)
    notebook1.place(x=20, y=20)
    frame2 = tk.Frame(master=home, width=200, height=400)
    frame2.place(x=200, y=0)
    notebook2 = tk.Button(master=frame2, text="LABORATÓRIO 5", image=photoimage, compound=tk.TOP, width=150, height=150)
    notebook2.place(x=20, y=20)
    frame3 = tk.Frame(master=home, width=200, height=400)
    frame3.place(x=400, y=0)
    notebook3 = tk.Button(master=frame3, text="LABORATÓRIO MÓVEL", image=photoimage, compound=tk.TOP, width=150, height=150)
    notebook3.place(x=20, y=20)
    center(home)
    home.mainloop()

homepage()