from tkinter import *
import tkinter.messagebox
from database import Auth
from time import sleep



class Register():
    def __init__(self, master):
        self.master = master

    def createAnAccount(self):
        """This method handles the creation of Accounts"""
        self.createAccount = Frame(self.master)
        self.createAccount.pack()
        self.newAccountLbl = Label(self.master, bg=generatePassword_bg,
                   text="Don't have an account? Click here to create one")
        self.newAccountLbl.pack(pady=10)
        self.newAccountLbl.bind( "<Button>", self.accountLink)


    # Method bound to createAccount Method for events
    def accountLink(self, event):
        self.regWindow = Toplevel(self.master, bg=registration_bg)
        self.regWindow.title("create account")
        self.regWindow.geometry("=600x500")
        Label(self.regWindow, text='Create your Account', bg=registration_bg,
                 font=("helvetica", 25, 'bold')).pack(pady=20)

        #username entry frame
        self.regFrame = Frame(self.regWindow, bg=login_bg)
        self.regFrame.pack(pady=60)

        # text variables
        self.username = StringVar()
        self.password = StringVar()

        #username label and entry
        Label(self.regFrame, bg=login_bg, text="Username",
                 font=("helvetica", 12), width=20).pack()

        self.regUsernameEntry = Entry(self.regFrame, bg=login_bg,
                                      font=("helvetica", 12),
                                      textvariable=self.username)
        self.regUsernameEntry.pack()


        #password label and entry
        Label(self.regWindow, bg=login_bg, text="Password",
                 font=("helvetica", 12), width=20).pack()
        self.regPasswordEntry = Entry(self.regWindow, bg=login_bg,
                                      font=("helvetica", 12), show="*",
                                      textvariable=self.password)
        self.regPasswordEntry.pack()

        # Button to submit the form
        Button(self.regWindow, text="Submit", width=10,
               height=1, bg=login_bg, command=self.submit_button).pack(pady=40)

    def submit_button(self):
        """ Creating an event on the
        submit button to create user account"""
        self.getUsername = self.username.get()
        self.getPassword = self.password.get()

        if self.getUsername == "admin":
            # call database methods
            reg = Auth(self.getUsername, self.getPassword)
            reg.createTable()
            reg.insert()
            self.regUsernameEntry.delete(0, END)
            self.regPasswordEntry.delete(0, END)
            #
            # Label(self.regWindow, text="Account Creation Success!",
            #       fg="green", font=("calibri", 11)).pack()
            self.master.update()
            sleep(0.5)
            self.master.destroy()

        else:
            tkinter.messagebox.showinfo(title="Error", message="Username must be 'admin' ")




background = '#452969'
login_bg = '#2c2233'
generatePassword_bg = '#553d75'
registration_bg =  '#5b417d'
