from tkinter import *
import mysql.connector
import random
import string



db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'jomar23',
    database = 'projects'
)
dbc = db.cursor()
def ifExisting(x):
    dbc.execute("SELECT * FROM users WHERE id = %s",(x,))
    result = dbc.fetchone()
    if result:
        return True
    else:
        return False

def keyGenerator():
    a = string.ascii_letters + string.digits
    b = ''
    for _ in range (10):
        b += random.choice(a).upper()
    if ifExisting(b):
        return
    else:
        dbc.execute("SELECT * FROM users")
        ff = dbc.fetchall()
        for f in ff:
            continue
        us = unm.get()
        pw = pd.get()
        if us in f:
            unt.config(text='username already used!')
        else:
            unt.config(text='Account Created Successfully!')
            mainpage()
            dbc.execute("INSERT INTO users(id, user, pass)\
                VALUES(%s,%s,%s)",(b,us,pw))
            db.commit()
            
gui = Tk()
class navs:
    @staticmethod
    def guiFrame(x):
        gui.geometry(x)
    @staticmethod
    def newWindow():
        for window in gui.winfo_children():
            window.destroy()
    def textLabel(self, x):
        self.txt = Label(gui,text = x)
        self.txt.pack()
    def textBox(self):
        self.tb = Entry(gui)
        self.tb.pack()
    def buttons(self,x,y):
        self.btn = Button(gui,text=x,command=y)
        self.btn.pack() 
ui = navs()
def logc():
    dbc.execute("SELECT * FROM users")
    ff = dbc.fetchall()
    for f in ff:
        continue
    if un.get() in f and pw.get() in f:
        tx.config(text="Logged In!")
        mainpage()
def login():
    global un, pw, tx
    ui.guiFrame("400x600")
    ui.textLabel("Username")
    un = Entry(gui)
    un.pack()
    ui.textLabel("Password")
    pw = Entry(gui)
    pw.pack()
    ui.buttons("Login",logc)
    tx = Label(gui,text='')
    tx.pack()
    ui.buttons("Create Account",cAcc)
def cAcc():
    global unm, unt,pd,cs
    ui.newWindow()
    ui.textLabel("Create Username")
    unm = Entry(gui)
    unm.pack()
    unt = Label(gui,text='')
    unt.pack()
    ui.textLabel("Create Password")
    pd = Entry(gui)
    pd.pack()
    ui.buttons("Create Account", keyGenerator)
    cs = Label(gui,text='')
def mainpage():
    ui.newWindow()
    ui.buttons("Add Task",'')
    ui.buttons("Check Task",'')
    ui.buttons("Mark Task",'')
    ui.buttons("Logout",login)

login()
gui.mainloop()