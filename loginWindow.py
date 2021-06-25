from tkinter import *
from database import UserData
import tkinter.messagebox
class LoggedIn():
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x500")
        self.root.columnconfigure(0, weight=1)
        self.root.title("tkPassword Safe")
        self.root.configure(bg="White")
        self.root.minsize(600, 500)
        self.root.maxsize(600, 500)

        self.username = StringVar()
        self.password = StringVar()
        self.email = StringVar()
        self.account = StringVar()

    def takeEntry(self):
        # Frame to hold the entry fields
        self.takeEntryFrame = Frame(self.root)
        self.takeEntryFrame.grid(row=0, column=0, sticky=(N, W), padx=10, pady=10)

        #Label and Entry field for UserName
        self.rootNameLabel = Label(self.takeEntryFrame, text="UserName: ")
        self.rootNameLabel.grid(row=0, column=0)

        self.rootNameEntry = Entry(self.takeEntryFrame, width=30, textvariable=self.username)
        self.rootNameEntry.grid(row=0, column=1)

        #Label and Entry field for Password
        self.rootPasswordLabel = Label(self.takeEntryFrame, text="Password: ")
        self.rootPasswordLabel.grid(row=1, column=0)

        self.rootPasswordEntry = Entry(self.takeEntryFrame, width=30, textvariable=self.password)
        self.rootPasswordEntry.grid(row=1, column=1)

        #Label and Entry field for Email
        self.rootEmailLabel = Label(self.takeEntryFrame, text="Email: ")
        self.rootEmailLabel.grid(row=2, column=0,)

        self.rootEmailEntry = Entry(self.takeEntryFrame, width=30, textvariable=self.email)
        self.rootEmailEntry.grid(row=2, column=1)

        #Label and Entry field for Account field
        self.rootAccountLabel = Label(self.takeEntryFrame, text="Account ")
        self.rootAccountLabel.grid(row=3, column=0)

        self.rootAccountEntry = Entry(self.takeEntryFrame, width=30, textvariable=self.account)
        self.rootAccountEntry.grid(row=3, column=1)


        self.takeEntryFrame.rowconfigure(0, weight=1)
        self.takeEntryFrame.columnconfigure(0, weight=1)


    def displayAccounts(self):
        self.listBoxFrame = Frame(self.root)
        self.listBoxFrame.grid(row=2, column=0, sticky=(N, S, E, W), padx=5, pady=5)

        self.tasks_listBox = Listbox(self.listBoxFrame, height=10, width=100, bg="white")
        self.tasks_listBox.grid(row=0, column=0, sticky=(N, S, E, W), padx=10, pady=10)

        # create a scroll bar
        self.tasksScrollBar = Scrollbar(self.listBoxFrame)
        self.tasksScrollBar.grid(row=0, column=1, sticky=(N, S))

        self.tasks_listBox.config(yscrollcommand=self.tasksScrollBar.set)
        self.tasksScrollBar.config(command=self.tasks_listBox.yview)


        self.listBoxFrame.rowconfigure(0, weight=1)
        self.listBoxFrame.columnconfigure(0, weight=1)

    def buttons(self):
        self.buttonsFrame = Frame(self.root)
        self.buttonsFrame.grid(row=3, column=0, sticky=(N), pady=10)
        self.buttonsFrame.configure(bg="White")

        self.create = Button(self.buttonsFrame, text='Create', bg="#46a822", width=20, command=self.createRecord)
        self.create.grid(pady=5)

        self.read = Button(self.buttonsFrame, text='Read', bg="#dcde5b", width=15, command=self.readRecords)
        self.read.grid(pady=5)

        self.update = Button(self.buttonsFrame, text='Update', bg="Orange", width=10)
        self.update.grid(pady=5)

        self.delete = Button(self.buttonsFrame, text='Delete', bg="#d63624", width=5, command=self.deleteRecord)
        self.delete.grid(padx=5)

    def createRecord(self):
        # send record to database
        self.namefield = self.username.get()
        self.passwordfield = self.password.get()
        self.emailfield = self.email.get()
        self.accountfield = self.account.get()

        self.userdata = UserData(self.namefield, self.passwordfield, self.emailfield, self.accountfield)
        self.userdata.createTable()
        self.userdata.insert()
        self.rootNameEntry.delete(0, END)
        self.rootPasswordEntry.delete(0, END)
        self.rootEmailEntry.delete(0, END)
        self.rootAccountEntry.delete(0, END)

    def readRecords(self):
        try:
            self.userdata = UserData(self.username, self.password, self.email, self.account)
            self.userdata.read()
            self.tasks_listBox.delete(0, END)
            self.tasks_listBox.insert(END, "-Current Record:")
            for self.data in self.userdata.read():
                self.tasks_listBox.insert(END, self.data)
        except:
            tkinter.messagebox.showwarning(title="Warning!", message="No task found")


    def updateRecord(self):
        pass

    def deleteRecord(self):
        try:
            self.delete = self.tasks_listBox.curselection()[0]
            self.tasks_listBox.delete(self.delete)
            self.userdata = UserData(self.username, self.password, self.email, self.account)
            self.userdata.delete(self.delete)
        except:
             tkinter.messagebox.showwarning(title="Warning!", message="Task not selected")
