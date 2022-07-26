import random
import string
from tkinter import *
import tkinter as tk
from tkinter import messagebox



def passw():
    
    fenetre = tk.Tk()
    fenetre.title("Password Generator")
    fenetre.geometry("400x250")

    def test(l):
        l = int(l.get())
        char = str()
        print(var_low.get())
        
        if var_low.get() == 1:
            char = char + string.ascii_lowercase
        if var_up.get() ==1:
            char = char + string.ascii_uppercase
        if var_num.get() ==1:
            char = char + string.digits
        if var_pun.get() ==1:
            char = char + string.punctuation
        if var_low.get() == 0 and var_up.get() == 0 and var_num.get() == 0 and var_pun.get() == 0:
            warning()
        print(char)

        mdp = ''.join(random.choice(char) for i in range(l))
        return mdp


    def warning():
        messagebox.showwarning("Attention", "Veuillez choisir au moins 1 paramètre !")

    def setTextInput(text):
        textEntry.set(text)

    textEntry = tk.StringVar()


    champ_label = Label(fenetre, text="Générateur de mots de passes")

    champ_label.pack()

    mdp = tk.Entry(fenetre, textvariable= textEntry, width=40)
    mdp.configure(state="readonly")
    mdp.pack()


    taille = Label(fenetre, text="Entrez la taille du mot de passe désiré")
    taille.pack(pady=5)
    l =Entry(fenetre)
    l.insert(0, "8")
    l.pack()

    var_low = IntVar()
    case_low = Checkbutton(fenetre, text="Caractères minuscules", variable=var_low)
    case_low.pack()

    var_up = IntVar()
    case_up = Checkbutton(fenetre, text="Caractères majuscules", variable=var_up)
    case_up.pack()

    var_num = IntVar()
    case_num = Checkbutton(fenetre, text="Chiffres (0-9)", variable=var_num)
    case_num.pack()

    var_pun = IntVar()
    case_pun = Checkbutton(fenetre, text="Caractères spéciaux", variable=var_pun)
    case_pun.pack()

    bouton_générer = Button(fenetre, text="Générer", command = lambda:setTextInput(test(l)))
    bouton_générer.pack(pady=10)

    fenetre.mainloop()

