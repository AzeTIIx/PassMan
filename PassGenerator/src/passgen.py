import random
import string
from tkinter import *
from tkinter import messagebox



def passw():
    
    ws = Toplevel()
    ws.title("Password Generator")
    ws.geometry("400x250")

    def test(l):
        l = int(l.get())
        char = str()
        
        if var_low.get() == 1:
            char = char + string.ascii_lowercase
        if var_up.get() ==1:
            char = char + string.ascii_uppercase
        if var_num.get() ==1:
            char = char + string.digits
        if var_pun.get() ==1:
            char = char + string.punctuation
        if var_low.get() == 0 and var_up.get() == 0 and var_num.get() == 0 and var_pun.get() == 0:
            messagebox.showwarning("Attention", "Veuillez choisir au moins 1 paramètre !")
    

        mdp = ''.join(random.choice(char) for i in range(l))
        return mdp
        

    def setTextInput(text):
        textEntry.set(text)

    textEntry = StringVar()
    champ_label = Label(ws, text="Générateur de mots de passes")
    champ_label.pack()

    mdp = Entry(ws, textvariable= textEntry, width=40)
    mdp.configure(state="readonly")
    mdp.pack()


    taille = Label(ws, text="Entrez la taille du mot de passe désiré")
    taille.pack(pady=5)
    l =Entry(ws)
    l.insert(0, "8")
    l.pack()

    var_low = IntVar()
    var_up = IntVar()
    var_num = IntVar()
    var_pun = IntVar()
    
    case_low = Checkbutton(ws, text="Caractères minuscules", variable=var_low)
    case_up = Checkbutton(ws, text="Caractères majuscules", variable=var_up)
    case_num = Checkbutton(ws, text="Chiffres (0-9)", variable=var_num)
    case_pun = Checkbutton(ws, text="Caractères spéciaux", variable=var_pun)
    
    case_low.pack()
    case_up.pack()
    case_num.pack()
    case_pun.pack()

    bouton_générer = Button(ws, text="Générer", command = lambda:setTextInput(test(l)))
    bouton_générer.pack(pady=10)
    

    ws.mainloop()

