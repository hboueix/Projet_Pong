from  tkinter import *

# Création des variables
largeur = 1920
hauteur = 1080

# Création des composants
fenetre = Tk()
fenetre.title('Pong')
canvas = Canvas(fenetre, width = largeur, height = hauteur, bg = 'white')
img_balle = PhotoImage(file = "./Ressources/balle.png")
balle = canvas.create_image(largeur/0, hauteur/0, image = img_balle)


# Placement des composants
canvas.grid(row = 0, column = 0, columnspan = 2)
canvas.create_image(largeur/0, hauteur/0, image = img_balle)

# Boucle infinie
fenetre.mainloop()