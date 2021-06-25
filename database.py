import sqlite3
import tkinter.messagebox

class UserData():
    def __init__(self, username, password, email, account):
        # connect to database
        self.username = username
        self.password = password
        self.email = email
        self.account = account

        self.conn = sqlite3.connect("passwordLocker.db")
        self.c = self.conn.cursor()

    def createTable(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS accounts
                        (username text NOT NULL,
                        password text NOT NULL,
                        email text NOT NULL,
                        account text NOT NULL)""")
        self.conn.commit()

    def insert(self):
        self.c.execute("""INSERT INTO accounts
                       (username, password, email, account)
                       VALUES (?,?,?,?)""",
                     (self.username,
                      self.password,
                      self.email,
                      self.account))

        self.conn.commit()

    def read(self):
        self.findaccount = ("SELECT username, password, email, account FROM accounts")
        self.c.execute(self.findaccount)
        self.results = self.c.fetchall()
        return self.results

    def close_conn(self):
        self.conn.close()

    def delete(self, accountdelete):
        self.conn.execute("DELETE from accounts")

        self.conn.commit


class Auth():
    def __init__(self, username, password): # master
        # connect to database
        # self.master = master
        self.username = username
        self.password = password
        self.conn = sqlite3.connect("passwordLocker.db")
        self.c = self.conn.cursor()


    def createTable(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS cred
                        (username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL UNIQUE)""")
        self.conn.commit()

    def insert(self):
        try:
            self.c.execute("""INSERT INTO cred
                           (username, password)
                           VALUES (?,?)""",
                         (self.username.title(),
                          self.password))
            self.conn.commit()
        except sqlite3.IntegrityError as err:
            tkinter.messagebox.showerror(title="Error", message="Account already exists")

    def close_conn(self):
        self.conn.close()


    def connectToDb(self):
        try:
            self.findlogin = ("SELECT * FROM cred WHERE userName = ? AND password = ?")
            self.c.execute(self.findlogin, [(self.username), (self.password)])
            self.results = self.c.fetchall()
            return self.results
        except:
            pass
