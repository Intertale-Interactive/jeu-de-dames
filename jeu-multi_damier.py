import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randrange

# DEFINITION DE LA FENETRE TKINTER #

WIDTH = 500
HEIGHT = 750
root = Tk()
canva = Canvas(root, width=WIDTH, height=HEIGHT)
root.configure(padx=25, pady=25) # A GARDER #
root.title("Jeu de dames multijoueur - Jouer avec vos amis !") # A GARDER #
root.resizable(width=False, height=False) # A GARDER #
# root.iconbitmap("chinese-checkers.png") # A GARDER #
canva.pack() # A GARDER #

noirRempli = PhotoImage(file="Dames-Noir-Rempli-Fond-Noir.png")
blancRempli = PhotoImage(file="Dames-Blanc-Rempli-Fond-Noir.png")
blanc = PhotoImage(file="Dames-Blanc_Vide.png")
noir = PhotoImage(file="Dames-Noir_Vide.png")
x, y = 25, 25
dico_lignee = {}
listee = []
for i in range(10):
    l = i+1
    if i < 4 and i >= 0 and i% 2 == 0:
        for o in range(5):
            id_pion_blanc = canva.create_image(x, y, image=blanc)
            id_pion_noir_rempli = canva.create_image(x + 50, y, image=noirRempli)
            listee.append(id_pion_blanc)
            listee.append(id_pion_noir_rempli)
            x += 100
    elif i < 4 and i >= 0 and i% 2 != 0:
        for o in range(5):
            id_pion_blanc = canva.create_image(x, y, image=noirRempli)
            id_pion_noir_rempli = canva.create_image(x + 50, y, image=blanc)
            listee.append(id_pion_blanc)
            listee.append(id_pion_noir_rempli)
            x += 100
    elif i == 4:
        for o in range(5):
            id_pion_blanc = canva.create_image(x, y, image=blanc)
            id_pion_noir_rempli = canva.create_image(x + 50, y, image=noir)
            listee.append(id_pion_blanc)
            listee.append(id_pion_noir_rempli)
            x += 100
    elif i == 5 :
        for o in range(5):
            id_pion_blanc = canva.create_image(x, y, image=noir)
            id_pion_noir_rempli = canva.create_image(x + 50, y, image=blanc)
            listee.append(id_pion_blanc)
            listee.append(id_pion_noir_rempli)
            x += 100
    elif i > 5 and i < 10 and i%2 == 0 :
        for o in range(5):
            id_pion_blanc = canva.create_image(x, y, image=blanc)
            id_pion_noir_rempli = canva.create_image(x + 50, y, image=blancRempli)
            listee.append(id_pion_blanc)
            listee.append(id_pion_noir_rempli)
            x += 100      
    else :
        for o in range(5):
            id_pion_blanc = canva.create_image(x, y, image=blancRempli)
            id_pion_noir_rempli = canva.create_image(x + 50, y, image=blanc)
            listee.append(id_pion_blanc)
            listee.append(id_pion_noir_rempli)
            x += 100  
        copy = listee.copy()
        dico_lignee[l] = listee
        #print(dico_lignee)
    y += 50
    x = 25


enter = canva.create_text(250, 630, text="Entrer les noms des joueurs puis cliquer 'Valider'...", fill="black", font=('Helvetica 13'))
canva.pack()
joueur1 = Entry(root)
joueur1.pack(side=BOTTOM)
joueur2 = Entry(root)
joueur2.pack(side=BOTTOM)

def valider_joueurs():
    nom_du_joueur_1 = joueur1.get()
    nom_du_joueur_2 = joueur2.get()
    canva.create_text(250, 700, text="Joueur 1 : " + nom_du_joueur_2, fill="black", font=('Helvetica 13'))
    canva.create_text(250, 720, text="Joueur 2 : " + nom_du_joueur_1, fill="black", font=('Helvetica 13'))
    canva.delete(enter)

def game():
    if joueur1.get() == "" or joueur2.get() == "":
        messagebox.showerror("Erreur", "Veuillez entrer les noms des joueurs !")
    else:
        pass
        


boutton_valider_joueur_2 = Button(root, text="VALIDER", font=('Helvetica 10'), command=valider_joueurs)
boutton_valider_joueur_2.pack(side=BOTTOM)
bouton_quitter = Button(root, text="QUITTER LA PARTIE", font=('Helvetica 10'), command=root.destroy)
bouton_quitter.pack(side=LEFT)
bouton_quitter = Button(root, text="JOUER", font=('Helvetica 10'), command=game)
bouton_quitter.pack(side=RIGHT)

def clique(event):
    x, y = event.x, event.y
    canva.delete(listee[randrange(0, 99)])
    print(x, y)
    canva.create_oval(x-3, y-3, x+3, y+3, fill='red', outline='')

canva.bind("<Button-1>", clique)

## END WITH MAINLOOP ##
root.mainloop()