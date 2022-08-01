import csv
from csv import *
from tkinter import *
from passgen import *
from tkinter import messagebox

main_lst = []

def edit(pathbase, listbox1, list_of_services):
    window=Toplevel()
    window.title("Data Entry")
    window.geometry("380x210")
    def add():
        global lst
        lst = [service.get(), mail.get(), username.get(), password.get()]
        main_lst.append(lst)
        messagebox.showinfo("Information","The data has been added successfully")
    def save():
        with open(pathbase, 'a', encoding='UTF8', newline='') as f:   
            Writer=csv.writer(f)
            Writer.writerows(main_lst)
            messagebox.showinfo("Information","Saved succesfully")
        list_of_services.append(lst[0])
        listbox1.insert(END, lst[0])

    def Clear():
            service.delete(0,END)
            mail.delete(0,END)
            username.delete(0,END)
            password.delete(0,END)
            
    def setTextInput(text):
        textEntry.set(text)
    
    textEntry = StringVar()
    textEntry.set("")
    
    label1=Label(window,text="service: ",padx=20,pady=10)
    label2=Label(window,text="mail: ",padx=20,pady=10)
    label3=Label(window,text="username: ",padx=20,pady=10)
    label4=Label(window,text="password: ",padx=20,pady=10)

    service=Entry(window,width=30,borderwidth=3)
    mail=Entry(window,width=30,borderwidth=3)
    username=Entry(window,width=30,borderwidth=3)
    password=Entry(window,textvariable= textEntry, width=30,borderwidth=3)

    save=Button(window,text="Save",padx=10,pady=10,command=save)
    passgen=Button(window,text="Generate mdp", command=lambda:setTextInput(passw()))
    add=Button(window,text="Add",padx=10,pady=10,command=add)
    Clear=Button(window,text="Clear",padx=10,pady=10,command=Clear)

    label1.grid(row=0,column=0)
    label2.grid(row=1,column=0)
    label3.grid(row=2,column=0)
    label4.grid(row=3,column=0)

    service.grid(row=0,column=1)
    mail.grid(row=1,column=1)
    username.grid(row=2,column=1)
    password.grid(row=3,column=1)
    
    passgen.grid(row = 3, column=2)
    add.grid(row=4,column=0)
    save.grid(row=4,column=1)
    Clear.grid(row=4,column=2)


    window.mainloop()