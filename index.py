#importando as bibliotecas 
from tkinter import *
from tkinter import messagebox
import tkinter as tk

#criando a janela

root = Tk()
root.title("Login")
root.geometry("600x300")
root.configure(background="white")
root.resizable(width=False, height=False)

#carregando imagens
logo = PhotoImage(file="imagens/logo.png")

#frame da esquerda
leftframe= Frame(root, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
leftframe.pack(side=LEFT)

#frame da direita
rightframe= Frame(root, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
rightframe.pack(side=RIGHT)

#colocando a imagem na esquerda
logolabel =Label(leftframe, image=logo,bg="MIDNIGHTBLUE")
logolabel.place(x=10, y=35)

#label do user
UserLabel = Label(rightframe,text="Username: ", font=("Century Gothic", 15), bg="MIDNIGHTBLUE",fg="white")
UserLabel.place(x=40, y=75)

#entrada do usuario
UserEntry = Entry(rightframe, width=30)
UserEntry.place(x=145, y=82)

#label da senha
PasswordLabel = Label(rightframe,text="Password: ", font=("Century Gothic", 15), bg="MIDNIGHTBLUE",fg="white")
PasswordLabel.place(x=40, y=150)

#entrada da senha
PasswordEntry = Entry(rightframe, width=30)
PasswordEntry.place(x=145, y=155)

#botoes
LoginButton = tk.Button(rightframe, text="Login", width=20)
LoginButton.place(x=40, y= 220)

RegisterButton = tk.Button(rightframe, text="Register", width=20)
RegisterButton.place(x=200, y= 220)




root.mainloop()