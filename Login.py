import tkinter as tk
from tkinter import messagebox
from MainInterface import MainInterface

class Login:
    def __init__(self, mainWin):
        self.mainWin = mainWin
        self.loginWin = tk.Toplevel()
        self.loginWin.title('Account Login')
        self.loginWin.geometry('320x250')

        #Display Username label and input
        self.UserName = tk.Label(self.loginWin, text = 'User Name')
        self.UserName.place(x=40, y=50)

        self.inputUserName = tk.Entry(self.loginWin, justify='right')
        self.inputUserName.place(x=120, y=50, width=150)

        #Display Password label and input
        self.Password = tk.Label(self.loginWin, text = 'Password')
        self.Password.place(x=40, y=100)

        self.inputPassword = tk.Entry(self.loginWin, show='*', justify='right')
        self.inputPassword.place(x=120, y=100, width=150)
        
        #Display instructions
        self.instructions = tk.Label(self.loginWin, text = 'Enter a username and password and press <enter>')
        self.instructions.place(x=40, y=180)

        self.loginWin.bind('<Return>', self.login)

    def login(self, event):
        username = self.inputUserName.get()
        password = self.inputPassword.get()

        self.validateLogin(username, password)

    def validateLogin(self, username, password):

        login = False

        with open('savedaccounts.txt', 'r') as file:
            for line in file:
                storedUsername, storedPassword = line.strip().split(':')
                if username == storedUsername and password == storedPassword:
                    login = True

        if login:
            self.loginWin.destroy()
            self.mainWin.destroy()
            MainInterface()
        else:
            messagebox.showerror('Login Failed', 'Invalid username or password.')
            self.inputUserName.delete(0, tk.END)
            self.inputPassword.delete(0, tk.END)


        
    
        
