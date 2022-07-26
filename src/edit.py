import csv
from csv import *
from tkinter import *
from tkinter import messagebox

main_lst = []

def edit(pathbase):
    window=Tk()
    window.title("Data Entry")
    window.geometry("450x250")
    def add():
        
        lst = [service.get(), mail.get(), username.get(), password.get()]
        main_lst.append(lst)
        messagebox.showinfo("Information","The data has been added successfully")
    def save():
        with open(pathbase, 'a', encoding='UTF8', newline='') as f:   
            Writer=csv.writer(f)
            Writer.writerow(["service","mail","username","password"])
            Writer.writerows(main_lst)
            messagebox.showinfo("Information","Saved succesfully")
    def Clear():
            service.delete(0,END)
            mail.delete(0,END)
            username.delete(0,END)
            password.delete(0,END)
    label1=Label(window,text="service: ",padx=20,pady=10)
    label2=Label(window,text="mail: ",padx=20,pady=10)
    label3=Label(window,text="username: ",padx=20,pady=10)
    label4=Label(window,text="password: ",padx=20,pady=10)

    service=Entry(window,width=30,borderwidth=3)
    mail=Entry(window,width=30,borderwidth=3)
    username=Entry(window,width=30,borderwidth=3)
    password=Entry(window,width=30,borderwidth=3)

    save=Button(window,text="Save",padx=10,pady=10,command=save)
    add=Button(window,text="Add",padx=10,pady=10,command=add)
    Clear=Button(window,text="Clear",padx=10,pady=10,command=Clear)
    Exit=Button(window,text="Exit",padx=10,pady=10,command=window.quit)

    label1.grid(row=0,column=0)
    label2.grid(row=1,column=0)
    label3.grid(row=2,column=0)
    label4.grid(row=3,column=0)

    service.grid(row=0,column=1)
    mail.grid(row=1,column=1)
    username.grid(row=2,column=1)
    password.grid(row=3,column=1)
    
    add.grid(row=4,column=0)
    save.grid(row=4,column=1)
    Clear.grid(row=4,column=2)
    Exit.grid(row=4,column=3)

    window.mainloop()