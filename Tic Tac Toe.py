from tkinter import *
from tkinter import messagebox
from winsound import *

fenetre = Tk()
fenetre.title("Tic-Tac-Toe")
fenetre.maxsize(300, 310)
fenetre.minsize(300, 310)

cliqué = True
compte = 0

def desactiver():
    bouton1.config(state=DISABLED)
    bouton2.config(state=DISABLED)
    bouton3.config(state=DISABLED)
    bouton4.config(state=DISABLED)
    bouton5.config(state=DISABLED)
    bouton6.config(state=DISABLED)
    bouton7.config(state=DISABLED)
    bouton8.config(state=DISABLED)
    bouton9.config(state=DISABLED)
        

def verifgagner():
    global gagnant
    gagnant = False
    if bouton1["text"] == "X" and bouton2["text"] == "X" and bouton3["text"] == "X":
        bouton1.config(bg="green")
        bouton2.config(bg="green")
        bouton3.config(bg="green")
        gagnant = True
        messagebox.showinfo("Tic Tac Toe", "Les X gagnent !")
        desactiver()

    elif bouton4["text"] == "X" and bouton5["text"] == "X" and bouton6["text"] == "X":
        bouton4.config(bg="green")
        bouton5.config(bg="green")
        bouton6.config(bg="green")
        gagnant = True
        messagebox.showinfo("Tic Tac Toe", "Les X gagnent !")
        desactiver()

    elif bouton7["text"] == "X" and bouton8["text"] == "X" and bouton9["text"] == "X":
        bouton7.config(bg="green")
        bouton8.config(bg="green")
        bouton9.config(bg="green")
        gagnant = True
        messagebox.showinfo("Tic Tac Toe", "Les X gagnent !")
        desactiver()

    elif bouton1["text"] == "X" and bouton4["text"] == "X" and bouton7["text"] == "X":
        bouton1.config(bg="green")
        bouton4.config(bg="green")
        bouton7.config(bg="green")
        gagnant = True
        messagebox.showinfo("Tic Tac Toe", "Les X gagnent !")
        desactiver()

    elif bouton2["text"] == "X" and bouton5["text"] == "X" and bouton8["text"] == "X":
        bouton2.config(bg="green")
        bouton5.config(bg="green")
        bouton8.config(bg="green")
        gagnant = True
        messagebox.showinfo("Tic Tac Toe", "Les X gagnent !")
        desactiver()

    elif bouton3["text"] == "X" and bouton6["text"] == "X" and bouton9["text"] == "X":
        bouton3.config(bg="green")
        bouton6.config(bg="green")
        bouton9.config(bg="green")
        gagnant = True
        messagebox.showinfo("Tic Tac Toe", "Les X gagnent !")
        desactiver()

    elif bouton1["text"] == "X" and bouton5["text"] == "X" and bouton9["text"] == "X":
        bouton1.config(bg="green")
        bouton5.config(bg="green")
        bouton9.config(bg="green")
        gagnant = True
        messagebox.showinfo("Tic Tac Toe", "Les X gagnent !")
        desactiver()

    elif bouton3["text"] == "X" and bouton5["text"] == "X" and bouton7["text"] == "X":
        bouton3.config(bg="green")
        bouton5.config(bg="green")
        bouton7.config(bg="green")
        gagnant = True
        messagebox.showinfo("Tic Tac Toe", "Les X gagnent !")
        desactiver()


    if bouton1["text"] == "O" and bouton2["text"] == "O" and bouton3["text"] == "O":
        bouton1.config(bg="green")
        bouton2.config(bg="green")
        bouton3.config(bg="green")
        gagnant = True
        messagebox.showinfo("Tic Tac Toe", "Les O gagnent !")
        desactiver()

    elif bouton4["text"] == "O" and bouton5["text"] == "O" and bouton6["text"] == "O":
        bouton4.config(bg="green")
        bouton5.config(bg="green")
        bouton6.config(bg="green")
        gagnant = True
        messagebox.showinfo("Tic Tac Toe", "Les O gagnent !")
        desactiver()

    elif bouton7["text"] == "O" and bouton8["text"] == "O" and bouton9["text"] == "O":
        bouton7.config(bg="green")
        bouton8.config(bg="green")
        bouton9.config(bg="green")
        gagnant = True
        messagebox.showinfo("Tic Tac Toe", "Les O gagnent !")
        desactiver()

    elif bouton1["text"] == "O" and bouton4["text"] == "O" and bouton7["text"] == "O":
        bouton1.config(bg="green")
        bouton4.config(bg="green")
        bouton7.config(bg="green")
        gagnant = True
        messagebox.showinfo("Tic Tac Toe", "Les O gagnent !")
        desactiver()

    elif bouton2["text"] == "O" and bouton5["text"] == "O" and bouton8["text"] == "O":
        bouton2.config(bg="green")
        bouton5.config(bg="green")
        bouton8.config(bg="green")
        gagnant = True
        messagebox.showinfo("Tic Tac Toe", "Les O gagnent !")
        desactiver()

    elif bouton3["text"] == "O" and bouton6["text"] == "O" and bouton9["text"] == "O":
        bouton3.config(bg="green")
        bouton6.config(bg="green")
        bouton9.config(bg="green")
        gagnant = True
        messagebox.showinfo("Tic Tac Toe", "Les O gagnent !")
        desactiver()

    elif bouton1["text"] == "O" and bouton5["text"] == "O" and bouton9["text"] == "O":
        bouton1.config(bg="green")
        bouton5.config(bg="green")
        bouton9.config(bg="green")
        gagnant = True
        messagebox.showinfo("Tic Tac Toe", "Les O gagnent !")
        desactiver()

    elif bouton3["text"] == "O" and bouton5["text"] == "O" and bouton7["text"] == "O":
        bouton3.config(bg="green")
        bouton5.config(bg="green")
        bouton7.config(bg="green")
        gagnant = True
        messagebox.showinfo("Tic Tac Toe", "Les O gagnent !")
        desactiver()
        
    if compte ==9 and gagnant == False:
        bouton1.config(bg="red")
        bouton2.config(bg="red")
        bouton3.config(bg="red")
        bouton4.config(bg="red")
        bouton5.config(bg="red")
        bouton6.config(bg="red")
        bouton7.config(bg="red")
        bouton8.config(bg="red")
        bouton9.config(bg="red")
    
        messagebox.showinfo("Tic Tac Toe", "Égalité parfaite !")
        desactiver()

def cliquedebouton(bouton):
    global cliqué, compte
    if bouton["text"] == " " and cliqué == True:
        bouton["text"] =  "X"
        cliqué = False
        compte += 1
        verifgagner()
    elif bouton["text"] == " " and cliqué == False:
        bouton["text"] = "O"
        cliqué = True
        compte += 1
        verifgagner()
    else:
        messagebox.showerror("Tic Tac Toe","Cette case est déjà sélectionné !")

def confirmation():
    
    if messagebox.askokcancel("Tic Tac Toe","Voulez vous vraiment quitter ?",icon='warning'):
        quit(fenetre)

def reset():
    global bouton1, bouton2, bouton3, bouton4, bouton5, bouton6, bouton7, bouton8, bouton9
    global cliqué, compte
    cliqué = True
    compte = 0
    
    bouton1 = Button(fenetre, text=" ", font=10, height = 5, width = 10, bg="white", command = lambda: cliquedebouton(bouton1))
    bouton2 = Button(fenetre, text=" ", font=10, height = 5, width = 10, bg="white", command = lambda: cliquedebouton(bouton2))
    bouton3 = Button(fenetre, text=" ", font=10, height = 5, width = 10, bg="white", command = lambda: cliquedebouton(bouton3))

    bouton4 = Button(fenetre, text=" ", font=10, height = 5, width = 10, bg="white", command = lambda: cliquedebouton(bouton4))
    bouton5 = Button(fenetre, text=" ", font=10, height = 5, width = 10, bg="white", command = lambda: cliquedebouton(bouton5))
    bouton6 = Button(fenetre, text=" ", font=10, height = 5, width = 10, bg="white", command = lambda: cliquedebouton(bouton6))

    bouton7 = Button(fenetre, text=" ", font=10, height = 5, width = 10, bg="white", command = lambda: cliquedebouton(bouton7))
    bouton8 = Button(fenetre, text=" ", font=10, height = 5, width = 10, bg="white", command = lambda: cliquedebouton(bouton8))
    bouton9 = Button(fenetre, text=" ", font=10, height = 5, width = 10, bg="white", command = lambda: cliquedebouton(bouton9))

    bouton1.grid(row=0, column=0)
    bouton2.grid(row=0, column=1)
    bouton3.grid(row=0, column=2)

    bouton4.grid(row=1, column=0)
    bouton5.grid(row=1, column=1)
    bouton6.grid(row=1, column=2)

    bouton7.grid(row=2, column=0)
    bouton8.grid(row=2, column=1)
    bouton9.grid(row=2, column=2)

menu = Menu(fenetre)
fenetre.config(menu=menu)

options_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Menu", menu= options_menu)
options_menu.add_command(label = "Recommencer la Partie", command = reset)
options_menu.add_command(label = "Aide", command = lambda: messagebox.showinfo("Tic Tac Toe","Le but du jeu est d'aligner 3 X ou 3 O à la suite pour remporter la partie, les deux joueurs jouent chaucun leurs tours."))
options_menu.add_command(label = "A Propos", command = lambda: messagebox.showinfo("Tic Tac Toe","Jeu réalisé par Gauthier GALON et Rafael CORREIA DA SILVA en classe de 102."))
options_menu.add_command(label = "Quitter", command = lambda:confirmation())

reset()
fenetre.iconbitmap("morpion.ico")
fenetre.mainloop()