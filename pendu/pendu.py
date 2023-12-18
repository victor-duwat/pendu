import tkinter as tk
import random

def charger_mots():
    with open("mots.txt", "r") as fichier:
        return fichier.read().splitlines()

def mot_aleatoire(mots):
    return random.choice(mots)

def afficher_mot():
    affichage = []
    for lettre in mot_actuel:
        if lettre.lower() in lettres_trouvees or lettre.upper() in lettres_trouvees:
            affichage.append(lettre)
        else:
            affichage.append('_')
    affichage_str = " ".join(affichage)
    label_mot.config(text=affichage_str)
    verifier_gagne(affichage_str)
    afficher_lettres_utilisees()    


def verifier_gagne(affichage):
    if '_' not in affichage:
        label_resultat.config(text="Bravo! Vous avez gagné!")


def afficher_lettres_utilisees():
    lettres_utilisees_label.config(text="Lettres utilisées: " + ", ".join(sorted(lettres_trouvees)))


def deviner(lettre):
    if lettre not in lettres_trouvees:
        lettres_trouvees.add(lettre)
        if lettre not in mot_actuel:
            dessiner_pendu()
    afficher_mot()


def dessiner_pendu():
    global erreurs
    erreurs += 1
    parties_pendu = [
        lambda: canvas.create_line(100, 300, 200, 300),  # Base
        lambda: canvas.create_line(150, 300, 150, 100),  # Poteau
        lambda: canvas.create_line(150, 100, 250, 100),  # Traverse
        lambda: canvas.create_line(250, 100, 250, 150),  # Corde
        lambda: canvas.create_oval(240, 150, 260, 170),  # Tête
        lambda: canvas.create_line(250, 170, 250, 220),  # Corps
        lambda: canvas.create_line(250, 180, 230, 200),  # Bras gauche
        lambda: canvas.create_line(250, 180, 270, 200),  # Bras droit
        lambda: canvas.create_line(250, 220, 230, 240),  # Jambe gauche
        lambda: canvas.create_line(250, 220, 270, 240)   # Jambe droite
    ]
    if erreurs <= len(parties_pendu):
        parties_pendu[erreurs - 1]()
    if erreurs == len(parties_pendu):
        label_resultat.config(text="Perdu! Le mot était: " + mot_actuel)


def deviner(lettre):
    lettre = lettre.lower()  
    if lettre not in lettres_trouvees:
        lettres_trouvees.add(lettre)
        if lettre not in mot_actuel.lower(): 
            dessiner_pendu()
    afficher_mot()


def nouvelle_partie():
    global mot_actuel, lettres_trouvees, erreurs
    mot_actuel = mot_aleatoire(mots)
    lettres_trouvees = set()
    erreurs = 0
    label_resultat.config(text="")
    afficher_mot()
    canvas.delete("all")
    lettres_utilisees_label.config(text="Lettres utilisées: ")

fenetre = tk.Tk()
fenetre.title("Jeu du Pendu")

mots = charger_mots()
mot_actuel = ""
lettres_trouvees = set()
erreurs = 0

canvas = tk.Canvas(fenetre, width=400, height=400)
canvas.pack()

label_mot = tk.Label(fenetre, font=('Helvetica', 24))
label_mot.pack()

label_resultat = tk.Label(fenetre, font=('Helvetica', 20))
label_resultat.pack()

lettres_utilisees_label = tk.Label(fenetre, font=('Helvetica', 16))
lettres_utilisees_label.pack()

frame_lettres = tk.Frame(fenetre)
frame_lettres.pack()

for lettre in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    tk.Button(frame_lettres, text=lettre, command=lambda l=lettre: deviner(l)).pack(side='left')

nouvelle_partie_btn = tk.Button(fenetre, text="Nouvelle Partie", command=nouvelle_partie)
nouvelle_partie_btn.pack()

nouvelle_partie()
fenetre.mainloop()
