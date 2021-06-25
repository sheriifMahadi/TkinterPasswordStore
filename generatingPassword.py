from tkinter import *
import tkinter.messagebox
from passwordGenerator import passwordGenerator
import pyperclip as pc


class PasswordGeneration():
    def __init__(self, master):
        self.master = master
        self.generatedPassword = IntVar()

    def passwordLink(self):
        """This method handles the generation of password"""
        self.generatePasswordlbl = Label(self.master, bg=generatePassword_bg,
                   text="Click here to generate a password")
        self.generatePasswordlbl.pack(pady=10)
        self.generatePasswordlbl.bind( "<Button>", self.generate_Button)


    # Method bound to generate Method for generation of passwords
    def generate_Button(self, event):
        self.generateWindow = Toplevel(self.master, bg=registration_bg)
        self.generateWindow.title("Generate password")

        Label(self.generateWindow, text='Enter password length between 8 and 20', bg=registration_bg,
                 font=("helvetica", 12)).pack(pady=20)
        self.generateEntry = Entry(self.generateWindow, bg=login_bg,
                                      font=("helvetica", 12),
                                      textvariable=self.generatedPassword)
        self.generateEntry.pack()

        Button(self.generateWindow, text="Generate", width=8,
               height=1, bg=login_bg, command=self.gen).pack(pady=20)



    def gen(self):
        self.printText = self.generatedPassword.get()
        self.genPass = passwordGenerator(self.printText)

        tkinter.messagebox.showinfo(title="Copied to clipboard", message=(self.genPass))
        pc.copy(self.genPass)



background = '#452969'
login_bg = '#2c2233'
generatePassword_bg = '#553d75'
registration_bg =  '#5b417d'
