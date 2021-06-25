from mainwindow import MainWindow
from register import Register
from generatingPassword import PasswordGeneration
from loginWindow import LoggedIn
from tkinter import *


def run():
    window = Tk()
    app = MainWindow(window)
    app.login()

    account_registration = Register(window)
    account_registration.createAnAccount()

    password = PasswordGeneration(window)
    password.passwordLink()
    window.mainloop()

    # a new master for the logged in page


run()
