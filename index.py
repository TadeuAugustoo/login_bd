#importando as bibliotecas 
from tkinter import *
from tkinter import messagebox

#criando a janela

root = Tk()
root.title("Login")
root.geometry("600x300")
root.configure(background="white")
root.resizable(width=False, height=False)

#frame da esquerda
leftframe= Frame(root, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
leftframe.pack(side=LEFT)

#frame da direita
rightframe= Frame(root, width=400, height=300, bg="white", relief="raise")
rightframe.pack(side=RIGHT)

root.mainloop()