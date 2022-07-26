import platform
import os
import csv
import threading
import tkinter as Tk
from edit import edit
from passgen import passw
from about import *
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

pathbase = ''


def browseFiles(): 
    global pathbase
    pathbase =  filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("CSV File", "*.csv*"), ("all files", "*.*"))) 
    return pathbase



def generator():
    if platform.system() == "Windows":
        os.system("py ./PassGenerator/src/passgen.py")
    elif platform.system() == "Linux":
        os.system("python3 ./PassGenerator/src/passgen.py")

def create(name):
    global pathbase
    pathbase = './PassGenerator/src/' +name+'.csv'
    with open(pathbase, 'w', encoding='UTF8', newline='') as f:   
        writer = csv.writer(f)
    

def View():
    global pathbase


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
fenetre.title("PassMan")
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
menu2.add_command(label="Password Generator", command=lambda:threading.Thread(passw()))
menu2.add_command(label="Edit Current base", command=lambda:threading.Thread(edit(pathbase)))
menubar.add_cascade(label="Tools", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="About", command=lambda : info())
menubar.add_cascade(label="Help", menu=menu3)

fenetre.config(menu=menubar)
tree = ttk.Treeview(fenetre, columns=("Service"))
tree.heading('Service', text="Service", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=600)
tree.pack()

button1 = Button(text="Display data", command=View)
button1.place(x=100, y=75)
button1.pack(pady=10)

fenetre.mainloop()