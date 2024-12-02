import tkinter as tk
from Login import Login
from AccountCreation import CreateAccount

class DataGUI:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title('Weather Data Program')
        self.mainWin.geometry('400x200')

        #Display Label
        self.headingLabel = tk.Label(text = 'Weather Data Analysis', font = ('Helvetica', 16), fg = 'blue')
        self.headingLabel.place(x=100, y=20)

        #Creating Buttons
        self.cancelButton = tk.Button(self.mainWin, text = 'Cancel', font = ('Helvetica', 12), width = 12, \
                                      command = self.mainWin.destroy)
        self.cancelButton.place(x=30, y=100)

        self.loginButton = tk.Button(self.mainWin, text = 'Login', font = ('Helvetica', 12), width = 12, \
                                     command = self.openLogin)
        self.loginButton.place(x=140, y=100)

        self.acctButton = tk.Button(self.mainWin, text = 'Create Account', font = ('Helvetica', 12), \
                                    width = 12, command = self.openCreateAccount)
        self.acctButton.place(x=250, y=100)

        #calls for mainloop

        self.mainWin.mainloop()


    def openLogin(self):
        self.loginButton.config(state='disabled')
        loginWindow = Login(self.mainWin)

        
    def openCreateAccount(self):
        CreateAccount()


dataAnalysis = DataGUI()

        
        

        
