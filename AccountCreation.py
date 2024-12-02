import tkinter as tk
from tkinter import messagebox
import os


class CreateAccount:
    def __init__(self):
        self.acctWin = tk.Toplevel()
        self.acctWin.title('Account Creation')
        self.acctWin.geometry('400x300')

        #Display username label and input
        self.createUserName = tk.Label(self.acctWin, text = 'Create a user name')
        self.createUserName.place(x=140, y=30)

        self.inputUserName = tk.Entry(self.acctWin, justify='right')
        self.inputUserName.place(x=130, y=60, width=150)


        #Display Password instructions label and input
        self.createPassword = tk.Label(self.acctWin, text = 'Create a password at least nine (9) characters,\n'
                                       '\nthat contains at least one digit, one uppercase,\n'
                                       '\nand one lowercase letter. Then press <enter>')
        self.createPassword.place(x=80, y=100)

        self.inputPassword = tk.Entry(self.acctWin, show='*', justify='right')
        self.inputPassword.place(x=130, y=200, width=150)

        self.acctWin.bind('<Return>', self.createAccount)

    def createAccount(self, event):
        username = self.inputUserName.get()
        password = self.inputPassword.get()

        self.validateUsername(username, password)
        self.validatePassword(password)
            

    def validateUsername(self, username, password):
        if len(username) == 0:
            messagebox.showerror('Invalid Username', 'Username cannot be left blank')
            self.inputUserName.delete(0, tk.END)
            return
        

        with open('savedaccounts.txt', 'r') as file:
            for line in file:
                storedUsername, _ = line.strip().split(':')
                if username == storedUsername:
                    messagebox.showerror('Error', 'Username already exists')
                    self.inputUserName.delete(0, tk.END)
                    return


    def validatePassword(self, password):

        if len(password) < 9:
            messagebox.showerror('Invalid Password', 'Password must be longer than nine (9) characters.')
            self.inputPassword.delete(0, tk.END)
            return

        if not any(c.isupper() for c in password):
                   messagebox.showerror('Invalid Password', 'Password must have at least one digit, one uppercase, and one lowercase letter.')
                   self.inputPassword.delete(0, tk.END)
                   return
                
        if not any(c.islower() for c in password):
                   messagebox.showerror('Invalid Password', 'Password must have at least one digit, one uppercase, and one lowercase letter.')
                   self.inputPassword.delete(0, tk.END)
                   return
                
        if not any(c.isdigit() for c in password):
                   messagebox.showerror('Invalid Password', 'Password must have at least one digit, one uppercase, and one lowercase letter.')
                   self.inputPassword.delete(0, tk.END)
                   return
        
        self.saveAccount(self.inputUserName.get(), password)
        self.acctWin.destroy()



    def saveAccount(self, username, password):

        with open('savedaccounts.txt', 'a') as file:
            file.write(f'{username}:{password}\n')

        
