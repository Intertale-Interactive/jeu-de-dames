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
root.title("Jeu de dames multijoueur - Jouez avec vos amis !") # A GARDER #
root.resizable(width=False, height=False) # A GARDER #
# root.iconbitmap("chinese-checkers.png") # A GARDER #
canva.pack() # A GARDER #

noirRempli = PhotoImage(file="Dames-Noir-Rempli-Fond-Noir.png")
blancRempli = PhotoImage(file="Dames-Blanc-Rempli-Fond-Noir.png")
blanc = PhotoImage(file="Dames-Blanc_Vide.png")
noir = PhotoImage(file="Dames-Noir_Vide.png")
dico_lignee = {}
listee = [blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, 
        noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc,
        blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, 
        noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc]
print(listee)

def affichage():
    x, y = 25, 25
    x2, y2 = 25, 25
    x3, y3 = 25, 25
    x4, y4 = 25, 25
    x5, y5 = 25, 25
    x6, y6 = 25, 25
    x7, y7 = 25, 25
    x8, y8 = 25, 25
    x9, y9 = 25, 25
    x10, y10 = 25, 25
    for i in range(40):
        if i < 10:
            id_pion = canva.create_image(x, y, image=listee[i])
            x += 50
        elif i >= 10 and i < 20:
            id_pion = canva.create_image(x2, y + 50, image=listee[i])
            x2 += 50
        elif i >= 20 and i < 30:
            id_pion = canva.create_image(x3, y + 100, image=listee[i])
            x3 += 50
        elif i >= 30 and i < 40:
            id_pion = canva.create_image(x4, y + 150, image=listee[i])
            x4 += 50

affichage()

# def change_image(event):
#     global x, y
#     x, y = event.x, event.y
#     print(x, y)
#     canva.create_image(x, y, image=noirRempli)

def clique(event):
    global x, y
    x, y = event.x, event.y
    listee[0] = noirRempli
    affichage()
    print(listee)
    print(x, y)
    canva.create_oval(x-3, y-3, x+3, y+3, fill='red', outline='')

canva.bind("<Button-1>", clique)

## END WITH MAINLOOP ##
root.mainloop()