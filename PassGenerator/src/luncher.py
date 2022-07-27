from tkinter import *
#from argon2 import PasswordHasher
import base64


win = Tk()
win.title("Login/Register")
win.geometry("400x150")

frame1 = Frame(win)
frame1.grid(row=0,column=0)

frame2 = Frame(win)
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
label2=Label(frame1,text="Password",padx=20,pady=10)
label2.grid(row=3,column=1)

Login=Button(frame2,text="Login",padx=10,pady=10,command='')
Register=Button(frame2,text="Register",padx=10,pady=10,command='')
Login.grid(row=1,column=0)
Register.grid(row=1,column=1)


win.mainloop()