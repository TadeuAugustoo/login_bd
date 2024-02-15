#importando as bibliotecas 
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import dataBaser

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

#label login
tituloLogin = Label(rightframe,text="LOGIN", font=("Century Gothic", 20), bg="MIDNIGHTBLUE",fg="red")
tituloLogin.place(x=150, y=25)

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
PasswordEntry = Entry(rightframe, width=30, show="x")
PasswordEntry.place(x=145, y=155)

#botoes
#login
LoginButton = tk.Button(rightframe, text="Login", width=20)
LoginButton.place(x=40, y= 220)

def RegisterToDataBase():
    Name = UserEntry.get()
    Pass = PasswordEntry.get() 
    dataBaser.cursor.execute("""
    INSERT INTO Users(User, Password) VALUES (?, ?)
    """, (Name, Pass))
    dataBaser.conn.commit()
    messagebox.showinfo(title="Register Info", message="Register Sucessfull")

#funcao registrar
def Register():
    #removendo os botoes do login
    LoginButton.place(x=601)
    tituloLogin.place(x=601)
    RegisterButton.place(x=601)
    
    #label login
    tituloRegister = Label(rightframe,text="REGISTER", font=("Century Gothic", 20), bg="MIDNIGHTBLUE",fg="red")
    tituloRegister.place(x=150, y=25)

    #Register dentro do Register
    Register_RegisterButton = tk.Button(rightframe, text="Register", width=20, command= RegisterToDataBase)
    Register_RegisterButton.place(x=200, y= 220)
    
    def BackToLogin():
        back.place(x=601)
        tituloRegister.place(x=601)
        Register_RegisterButton.place(x=601)
        LoginButton.place(x=40, y= 220)
        tituloLogin.place(x=150, y=25)
        RegisterButton.place(x=200, y= 220)


    #botao de voltar
    back =tk.Button(rightframe,text="Back", width=20, command=BackToLogin)
    back.place(x=40, y= 220) 

   
#entrar na janela de registrar
RegisterButton = tk.Button(rightframe, text="Register", width=20, command=Register)
RegisterButton.place(x=200, y= 220)




root.mainloop()