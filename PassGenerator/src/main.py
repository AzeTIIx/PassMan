import csv
import threading
import tkinter as Tk
from edit import edit
from passgen import *
from about import *
from tkinter import *
from tkinter import filedialog
import pandas as pd
import glob
import os.path


pathbase = ''
list_of_services = []

def read():
    global data, pathbase, list_of_services
    file = open(pathbase)
    reader = csv.reader(file)
    data = list(reader)

    for x in list(range(0, len(data))):
        list_of_services.append(data[x][0])
    
    return list_of_services
        
def saved():
    global pathbase
    pathbase = './PassGenerator/src/'
    file_type = r'\*csv'
    files = glob.glob(pathbase + file_type)
    pathbase = max(files, key=os.path.getctime)
    print(pathbase)
    return pathbase

def save():
    with open ("./PassGenerator/src/lastfile.txt", "w") as f:
        f.write(pathbase)
    with open ("./PassGenerator/src/lastfile.txt", "r") as f:   
        if pathbase in f.read():
            messagebox.showwarning("Success", "File Saved")

def browseFiles(): 
    global pathbase, data
    pathbase =  filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("CSV File", "*.csv*"), ("all files", "*.*"))) 
    with open ("./PassGenerator/src/lastfile.txt", "w") as f:
        f.write(pathbase)
    listbox1.delete(0,END)
    list_of_services = []
    file = open(pathbase)
    reader = csv.reader(file)
    data = list(reader)
    for x in list(range(0, len(data))):    
        list_of_services.append(data[x][0])
        listbox1.insert(END, list_of_services[-1])
        print(list_of_services)
  

def delete_item():
    index = listbox1.curselection()
    listbox1.delete(index)
    
    def delete_empty_rows(pathbase):
        data = pd.read_csv(pathbase, skip_blank_lines=True)
        data.dropna()
        data.to_csv(pathbase, header=True)

    def delete_col(pathbase):
        data = pd.read_csv(pathbase, skip_blank_lines=True)
        first_column = data.columns[0]
        data = data.drop([first_column], axis=1)
        data.to_csv(pathbase, header=True, index = False)   
        
        
    lines = list()
    rownumbers_to_remove= index

    with open(pathbase, 'r') as read_file:
        reader = csv.reader(read_file)
        for row_number, row in enumerate(reader, start=0):
            if(row_number not in rownumbers_to_remove):
                lines.append(row)

    with open(pathbase, 'w') as write_file:
        writer = csv.writer(write_file)
        writer.writerows(lines)
        
    delete_empty_rows(pathbase)
    delete_col(pathbase)

def create(name):
    global pathbase, data
    pathbase = './PassGenerator/src/' + name +'.csv'
    with open ("./PassGenerator/src/lastfile.txt", "w") as f:
        f.write(pathbase)
    with open(pathbase, 'w', encoding='UTF8', newline='') as f:   
        writer = csv.writer(f)
    listbox1.delete(0,END)
    list_of_services = []
    file = open(pathbase)
    reader = csv.reader(file)
    data = list(reader)
    for x in list(range(0, len(data))):    
        list_of_services.append(data[x][0])
        listbox1.insert(END, list_of_services)

def Update():
    global index
    file = open(pathbase)
    reader = csv.reader(file)
    data = list(reader)
    index = listbox1.curselection()[0]
    Mail2.config(text = data[index][1])
    Username2.config(text = data[index][2])
    Password2.config(text = data[index][3])

def copy_mail(): 
    global index
    Mail2.clipboard_clear()
    Mail2.clipboard_append(data[index][1])
    
def copy_user(): 
    global index
    Username2.clipboard_clear()
    Username2.clipboard_append(data[index][2])

def copy_pass(): 
    global index
    Password2.clipboard_clear()
    Password2.clipboard_append(data[index][3])
    

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
fenetre.geometry("455x310")
fenetre.resizable(False, False)
fenetre.wm_iconbitmap('./PassGenerator/src/ic.ico')

frame1 = Frame(fenetre)
frame1.grid(row=0,column=0)

frame2 = Frame(fenetre)
frame2.grid(row=1,column=0)

frame3 = Frame(fenetre)
frame3.grid(row=2,column=0)

menubar = Menu(fenetre)

saved()
read()

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="New file", command=lambda:askname())
menu1.add_command(label="Open", command=lambda : browseFiles())
menu1.add_command(label="Save", command=save)
menu1.add_separator()
menu1.add_command(label="Exit", command=fenetre.destroy)
menubar.add_cascade(label="File", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Password Generator", command=lambda:threading.Thread(passw()))
menu2.add_command(label="Edit Current base", command=lambda:threading.Thread(edit(pathbase, listbox1, list_of_services)))

menubar.add_cascade(label="Tools", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="About", command=lambda : info())
menubar.add_cascade(label="Help", menu=menu3)

fenetre.config(menu=menubar)

button1 = Button(frame2, text="Display data", command=Update)
button1.grid(row=4, column=1, pady=10)

button2 = Button(frame2, text="Delete row", command=delete_item)
button2.grid(row=4, column=2, pady=10, padx=10)

var = StringVar(value=list_of_services)
listbox1 = Listbox(frame1, listvariable=var, width= 75)
listbox1.grid(row=1, column=2)

Mail = Label(frame3, text="Mail : ").grid(row= 6, column=0, sticky="w")
Username = Label(frame3, text="Username : ").grid(row= 7, column=0, sticky="w")
Password = Label(frame3, text="Password : ").grid(row= 8, column=0, sticky="w")

Mail2 = Label(frame3, text="")
Mail2.grid(row= 6, column=2, sticky="w")
Mb_2=Button(frame3,text='Copy',command=lambda:copy_mail())
Mb_2.grid(row= 6, column=3, sticky="w", padx=10)

Username2 = Label(frame3, text="")
Username2.grid(row= 7, column=2, sticky="w")
Ub_2=Button(frame3,text='Copy',command=lambda:copy_user())
Ub_2.grid(row= 7, column=3, sticky="w", padx=10)

Password2 = Label(frame3, text="")
Password2.grid(row= 8, column=2, sticky="w")
Pb_2=Button(frame3,text='Copy',command=lambda:copy_pass())
Pb_2.grid(row= 8, column=3, sticky="w", padx=10)

if __name__ =='__main__':

    fenetre.mainloop()
    