import platform
import os
import sqlite3
import tkinter as Tk
from about import *
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def browseFiles(): 
    global pathbase
    pathbase =  filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Database File", "*.db*"), ("all files", "*.*"))) 
    return pathbase



def generator():
    if platform.system() == "Windows":
        os.system("py ./PassGenerator/src/passgen.py")
    elif platform.system() == "Linux":
        os.system("python3 ./PassGenerator/src/passgen.py")

def create(name):
    global pathbase
    
    pathbase = './PassGenerator/src/' +name+'.db'
    con1 = sqlite3.connect(pathbase)
    cursor = con1.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, mail TEXT, username TEXT, password TEXT)")
    con1.commit()
    con1.close()
    
def edit():
    global pathbase
    con1 = sqlite3.connect(pathbase)
    cursor = con1.cursor()
    cursor.execute("""INSERT INTO users(mail, username, password) VALUES(?, ?, ?)""", ("test", "test", "test"))
    
def View():
    global pathbase
    con1 = sqlite3.connect(pathbase)
    cur1 = con1.cursor()
    cur1.execute("SELECT * FROM users")
    rows = cur1.fetchall()    
    for row in rows:
        print(row) 
        tree.insert("", Tk.END, values=row)        
    con1.close()

def askname():
    sw = Tk()
    
    def close_window():
        sw.destroy()
        
    sw.title("New file")
    sw.geometry("200x75")
    entree = Entry(sw, width=30)
    entree.pack(pady = 10)
    bouton_create = Button(sw, text="Create", command = lambda:[create(name =entree.get()), close_window()])
    bouton_create.pack(pady = 5)
    sw.mainloop()
    



fenetre = Tk()
fenetre.title("Password Keeper")
fenetre.geometry("650x300")


menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="New file", command=lambda:askname())
menu1.add_command(label="Open", command=lambda : browseFiles())
menu1.add_command(label="Save", command="")
menu1.add_command(label="Save as", command="")
menu1.add_separator()
menu1.add_command(label="Exit", command=fenetre.quit)
menubar.add_cascade(label="File", menu=menu1)


menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Password Generator", command= lambda:generator())
menu2.add_command(label="Edit Current base", command=lambda: edit())
menubar.add_cascade(label="Tools", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=lambda : info())
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)

tree = ttk.Treeview(fenetre, column=("c1", "c2", "c3"), show='headings')
tree.column("#1", anchor=CENTER)
tree.heading("#1", text="mail")
tree.column("#2", anchor=CENTER)
tree.heading("#2", text="username")
tree.column("#3", anchor=CENTER)
tree.heading("#3", text="password")
tree.pack()

button1 = Button(text="Display data", command=View)
button1.place(x=100, y=75)
button1.pack(pady=10)

fenetre.mainloop()