from tkinter import *
#from argon2 import PasswordHasher
import base64

def res():
    f = Toplevel()
    f.title("Login/Register")
    f.geometry("400x230")
    f.resizable(False, False)

    frame1 = Frame(f)
    frame1.grid(row=0,column=0)

    frame2 = Frame(f)
    frame2.grid(row=1,column=0)

    textEntry = StringVar()
    champ_label = Label(frame1, text="login or register if you don't have an account")
    champ_label.grid(row=1,column=2)

    username = Entry(frame1, text='', width=40)
    username.grid(row=2,column=2)
    label1=Label(frame1,text="Username",padx=20,pady=10)
    label1.grid(row=2,column=1)

    password = Entry(frame1, text='', width=40, show='*')
    password.grid(row=3,column=2)
    label2=Label(frame1,text="Old password",padx=20,pady=10)
    label2.grid(row=3,column=1)

    npassword = Entry(frame1, text='', width=40, show='*')
    npassword.grid(row=4,column=2)
    label3=Label(frame1,text="New password",padx=20,pady=10)
    label3.grid(row=4,column=1)

    confirm = Entry(frame1, text='', width=40, show='*')
    confirm.grid(row=5,column=2)
    label4=Label(frame1,text="Confirm password",padx=20,pady=10)
    label4.grid(row=5,column=1)

    valid=Button(frame2,text="Confirm",padx=10,pady=10,command=f.destroy)
    valid.grid(row=1,column=1,padx=(10, 10))
