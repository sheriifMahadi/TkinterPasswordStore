
from tkinter import *
from database import Auth
from loginWindow import LoggedIn
import tkinter.messagebox

class MainWindow():
    """"""
    def __init__(self, master):
        self.master = master
        self.master.title("User Login")
        Label(self.master, text='Welcome Back', bg=background,
                 font=("helvetica", 25, 'bold')).pack(pady=20)
        self.master.geometry("600x500")
        self.master.configure(bg=background)
        self.username = StringVar()
        self.password = StringVar()



    def login(self):
        """This method handles login; username and password"""

        # username frame
        self.loginUsername  = Frame(self.master, bg=login_bg)
        self.loginUsername.pack(pady=60)

        Label(self.loginUsername, bg=login_bg, text="Username",
                 font=("helvetica", 12)).grid(row=0, column=0)

        self.usernameEntry = Entry(self.loginUsername, bg=login_bg,
                                      font=("helvetica", 12),
                                      textvariable=self.username)
        self.usernameEntry.grid(row=1, column=0)

        # Password frame
        self.loginPassword = Frame(self.master, bg=login_bg)
        self.loginPassword.pack()

        Label(self.loginPassword, bg=login_bg, text="Password",
                 font=("helvetica", 12)).grid(row=0, column=0)
        self.passwordEntry = Entry(self.loginPassword, show="*", bg=login_bg,
                                      font=("helvetica", 12),
                                      textvariable=self.password)
        self.passwordEntry.grid(row=1, column=0)

        Button(self.master, text="Login", width=10,
               height=1, bg=login_bg, command=self.auth).pack(pady=20)


    def auth(self):
        """This method handles user authentication"""
        # Get username and password
        self.authUsername = self.username.get().title()
        self.authPassword = self.password.get()

        # Database class Check provided username and password
        reg = Auth(self.authUsername, self.authPassword) # master

        # login if username and password matches database
        self.results = reg.connectToDb()
        if self.results:
            self.master.destroy()
            self.newWindow = Tk()
            self.success = LoggedIn(self.newWindow) # Opens a new window
                                                    # containing the records
            self.success.takeEntry()
            self.success.displayAccounts()
            self.success.buttons()
            self.newWindow.mainloop()
        else:
            tkinter.messagebox.showinfo(title="Error", message="Wrong Credentials ")









background = '#452969'
login_bg = '#2c2233'
generatePassword_bg = '#553d75'
registration_bg =  '#5b417d'
