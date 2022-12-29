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
demi_Blanc = PhotoImage(file="demi_Blanc.png")
demi_Noir = PhotoImage(file="demi_Noir.png")
dico_lignee = {}
listee = [blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, 
        noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc,
        blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, 
        noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc, noirRempli, blanc,
        blanc, noir, blanc, noir, blanc, noir, blanc, noir, blanc, noir,
        noir, blanc, noir, blanc, noir, blanc, noir, blanc, noir, blanc,
        blanc, blancRempli, blanc, blancRempli, blanc, blancRempli, blanc, blancRempli, blanc, blancRempli,
        blancRempli, blanc, blancRempli, blanc, blancRempli, blanc, blancRempli, blanc, blancRempli, blanc,
        blanc, blancRempli, blanc, blancRempli, blanc, blancRempli, blanc, blancRempli, blanc, blancRempli,
        blancRempli, blanc, blancRempli, blanc, blancRempli, blanc, blancRempli, blanc, blancRempli, blanc]
# print(listee)

def affichage():
    canva.delete('all')
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
    for i in range(100):
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
        elif i >= 40 and i < 50:
            id_pion = canva.create_image(x5, y + 200, image=listee[i])
            x5 += 50
        elif i >= 50 and i < 60:
            id_pion = canva.create_image(x6, y + 250, image=listee[i])
            x6 += 50
        elif i >= 60 and i < 70:
            id_pion = canva.create_image(x7, y + 300, image=listee[i])
            x7 += 50
        elif i >= 70 and i < 80:
            id_pion = canva.create_image(x8, y + 350, image=listee[i])
            x8 += 50
        elif i >= 80 and i < 90:
            id_pion = canva.create_image(x9, y + 400, image=listee[i])
            x9 += 50
        elif i >= 90 and i < 100:
            id_pion = canva.create_image(x10, y + 450, image=listee[i])
            x10 += 50

affichage()

white = True
def clique(event):
    global white
    global x, y
    x, y = event.x, event.y
    # listee[randrange(0, 39)] = noirRempli
    affichage()
    x = x // 50 + 1
    y = y // 50 + 1
    numero_case_touched = (10 * (y - 1) + x) - 1
    canMove = False
    first_diagonal = listee[numero_case_touched - 11]
    second_diagonal = listee[numero_case_touched - 9]
    third_diagonal = listee[numero_case_touched + 9]
    fourth_diagonal = listee[numero_case_touched + 11]
    fifth_diagonal = listee[numero_case_touched - 22]
    sixth_diagonal = listee[numero_case_touched - 18]
    seventh_diagonal = listee[numero_case_touched + 18]
    eighth_diagonal = listee[numero_case_touched + 22]

    if first_diagonal == noir or second_diagonal == noir or third_diagonal == noir or fourth_diagonal == noir:
        canMove = True
    else:
        canMove = False
    
    if white == True:
        # print(x, y, canMove, listee[numero_case_touched], white, black)
        if listee[numero_case_touched] == blancRempli:
            global a_supprimer 
            a_supprimer = numero_case_touched
        if first_diagonal == noir and listee[numero_case_touched] == blancRempli:
            listee[numero_case_touched - 11] = demi_Blanc
        if second_diagonal == noir and listee[numero_case_touched] == blancRempli:
            listee[numero_case_touched - 9] = demi_Blanc
        if third_diagonal == noir and listee[numero_case_touched] == blancRempli:
            listee[numero_case_touched + 9] = demi_Blanc
        if fourth_diagonal == noir and listee[numero_case_touched] == blancRempli:
            listee[numero_case_touched + 11] = demi_Blanc
        if first_diagonal == noirRempli and listee[numero_case_touched] == blancRempli:
            listee[numero_case_touched - 22] = demi_Blanc
        if second_diagonal == noirRempli and listee[numero_case_touched] == blancRempli:
            listee[numero_case_touched - 18] = demi_Blanc
        if third_diagonal == noirRempli and listee[numero_case_touched] == blancRempli:
            listee[numero_case_touched + 18] = demi_Blanc
        if fourth_diagonal == noirRempli and listee[numero_case_touched] == blancRempli:
            listee[numero_case_touched + 22] = demi_Blanc
        if listee[numero_case_touched] == demi_Blanc:
            listee[numero_case_touched] = blancRempli
            for i in range(len(listee)):
                if listee[i] == demi_Blanc:
                    listee[i] = noir
            if a_supprimer - numero_case_touched == 18:
                listee[numero_case_touched + 9] = noir
            if a_supprimer - numero_case_touched == 22:
                listee[numero_case_touched + 11] = noir
            if numero_case_touched - a_supprimer == 22:
                listee[numero_case_touched - 11] = noir
            if numero_case_touched - a_supprimer == 18:
                listee[numero_case_touched - 9] = noir
            listee[a_supprimer] = noir
            white = False
        
    else:
        # print(x, y, canMove, listee[numero_case_touched], white, black)
        if listee[numero_case_touched] == noirRempli:
            a_supprimer = numero_case_touched
        if first_diagonal == noir and listee[numero_case_touched] == noirRempli:
            listee[numero_case_touched - 11] = demi_Noir
        if second_diagonal == noir and listee[numero_case_touched] == noirRempli:
            listee[numero_case_touched - 9] = demi_Noir
        if third_diagonal == noir and listee[numero_case_touched] == noirRempli:
            listee[numero_case_touched + 9] = demi_Noir
        if fourth_diagonal == noir and listee[numero_case_touched] == noirRempli:
            listee[numero_case_touched + 11] = demi_Noir
        if first_diagonal == blancRempli and listee[numero_case_touched] == noirRempli:
            listee[numero_case_touched - 22] = demi_Noir
        if second_diagonal == blancRempli and listee[numero_case_touched] == noirRempli:
            listee[numero_case_touched - 18] = demi_Noir
        if third_diagonal == blancRempli and listee[numero_case_touched] == noirRempli:
            listee[numero_case_touched + 18] = demi_Noir
        if fourth_diagonal == blancRempli and listee[numero_case_touched] == noirRempli:
            listee[numero_case_touched + 22] = demi_Noir
        if listee[numero_case_touched] == demi_Noir:
            listee[numero_case_touched] = noirRempli
            for i in range(len(listee)):
                if listee[i] == demi_Noir:
                    listee[i] = noir
            if a_supprimer - numero_case_touched == 18:
                listee[numero_case_touched + 9] = noir
            if a_supprimer - numero_case_touched == 22:
                listee[numero_case_touched + 11] = noir
            if numero_case_touched - a_supprimer == 22:
                listee[numero_case_touched - 11] = noir
            if numero_case_touched - a_supprimer == 18:
                listee[numero_case_touched - 9] = noir
            listee[a_supprimer] = noir
            white = True
    affichage()
    # canva.create_oval(x-3, y-3, x+3, y+3, fill='red', outline='')

canva.bind("<Button-1>", clique)

# def change_image(event):
#     global x, y
#     x, y = event.x, event.y
#     print(x, y)
#     canva.create_image(x, y, image=noirRempli)

## END WITH MAINLOOP ##
root.mainloop()