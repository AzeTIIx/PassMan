import csv
import threading
import tkinter as Tk
from edit import edit
from passgen import *
from about import *
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

pathbase = ''
list_of_services = []

def read():
    global data, pathbase, list_of_services
    print(pathbase)
    file = open(pathbase)
    reader = csv.reader(file)
    data = list(reader)

    for x in list(range(0, len(data))):
        list_of_services.append(data[x][0])
    
    return list_of_services
        
def saved():
    global pathbase
    f = open("./PassGenerator/src/lastfile.txt", "r")
    if not './PassGeneraor/src' in f.read():
        pathbase = './PassGenerator/src/test.csv'
        return pathbase 
    else :
        print(f.readline())
        pathbase = f.readline()
        return pathbase

def save():
    with open ("./PassGenerator/src/lastfile.txt", "w") as f:
        f.write(pathbase)
    with open ("./PassGenerator/src/lastfile.txt", "r") as f:   
        if pathbase in f.read():
            messagebox.showwarning("Succeed", "File Saved")

    
def browseFiles(): 
    global pathbase
    pathbase =  filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("CSV File", "*.csv*"), ("all files", "*.*"))) 
    with open ("./PassGenerator/src/lastfile.txt", "w") as f:
        f.write(pathbase)
    read()
    return pathbase


def create(name):
    global pathbase
    pathbase = './PassGenerator/src/' + name +'.csv'
    with open ("./PassGenerator/src/lastfile.txt", "w") as f:
        f.write(pathbase)
    with open(pathbase, 'w', encoding='UTF8', newline='') as f:   
        writer = csv.writer(f)
    read()
    

def Update():
    read()
    index = listbox1.curselection()[0]
    Mail2.config(text = data[index][1])
    Username2.config(text = data[index][2])
    Password2.config(text = data[index][3])
    

def askname():
    sw = Tk()
    
    def close_window():
        sw.destroy()
        
    sw.title("New file")
    sw.geometry("197x75")
    entree = Entry(sw, width=32)
    entree.grid(row=0, column=2)
    bouton_create = Button(sw, text="Create", command = lambda:[create(name =entree.get()), close_window()])
    bouton_create.grid(row=1, column=2)
    sw.mainloop()
    



fenetre = Tk()
fenetre.title("PassMan")
fenetre.geometry("600x300")


menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="New file", command=lambda:askname())
menu1.add_command(label="Open", command=lambda : browseFiles())
menu1.add_command(label="Save", command=save)
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


saved()
read()
print(list_of_services)
var = StringVar(value=list_of_services)
listbox1 = Listbox(fenetre, listvariable=var, width= 75)
listbox1.grid(row=1, column=2)


button1 = Button(text="Display data", command=Update)
button1.place(x=100, y=75)
button1.grid(row=4, column=2, pady=10)

Mail = Label(fenetre, text="Mail").grid(row= 6, column=0, sticky="w")
Username = Label(fenetre, text="Username").grid(row= 7, column=0, sticky="w")
Password = Label(fenetre, text="Password").grid(row= 8, column=0, sticky="w")

Mail2 = Label(fenetre, text="")
Mail2.grid(row= 6, column=3, sticky="w")
Username2 = Label(fenetre, text="")
Username2.grid(row= 7, column=3, sticky="w")
Password2 = Label(fenetre, text="")
Password2.grid(row= 8, column=3, sticky="w")

if __name__ =='__main__':
    fenetre.mainloop()