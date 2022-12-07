import time
import os

case = ""

def menu():
    """
    Cette fonction permet d'afficher le menu principal  et de sélectionner le mode de jeu ou de quitter le jeu.
    """
    print("Bienvenue sur le jeu de dames !")
    print()
    time.sleep(2)
    print("Veuillez sélectionner un mode de jeu :")
    print()
    print("        -> 1  Jeu en solo")
    print("        -> 2  Jeu en multi")
    print("        -> 3  Quitter le jeu")
    print()
    case = str(input("Selectionner ici le mode que vous souhaitez : "))
    assert case == "1" or case == "2" or case == "3"
    if case == "1":
        jeu_solo()
    if case == "2":
        jeu_multi()
    if case == "3":
        print()
        print("################################")
        print("# Vous venez de quitter le jeu #")
        print("################################")
        print()
    
def jeu_solo():
    print()
    print("################################")
    print("#      Coming soon (2023)      #")
    print("################################")
    print()
    
def jeu_multi():
    print()
    print("################################")
    print("#      Coming soon (2022)      #")
    print("################################")
    print()

menu()
