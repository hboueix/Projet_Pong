from  tkinter import *

# Création des variables
largeur = 1920
hauteur = 1080

# Création des composants
fenetre = Tk()
fenetre.title('Pong')
canvas = Canvas(fenetre, width = largeur, height = hauteur, bg = 'white')
img_balle = PhotoImage(file = "Projet_Pong/Ressources/balle.png")
balle = canvas.create_image(0, 0, anchor = NW, image = img_balle)

# Placement des composants
canvas.grid(row = 0, column = 0, columnspan = 2)


# Boucle infinie
fenetre.mainloop()