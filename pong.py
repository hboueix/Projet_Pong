from  tkinter import *

fenetre = Tk()
fenetre.title('Pong')
fenetre.attributes('-fullscreen', 1)

# Création des fonctions
def gameTick():
    global dx, dy
    coords = canvas.coords(balle)
    if coords[0] <= 0 or coords[2] >= largeur:
        dx *= -1
    if coords[1] <= 0 or coords[3] >= hauteur:
        dy *= -1
    canvas.move(balle, dx, dy)
    fenetre.after(5, gameTick)

# Création des variables
largeur = fenetre.winfo_screenwidth()
hauteur = fenetre.winfo_screenheight()
dimensions = str(largeur) + 'x' + str(hauteur)
dx = 3
dy = 3

# Création des composants
fenetre.geometry(dimensions)

    # Canvas
canvas = Canvas(fenetre, width = largeur, height = hauteur, bg = 'black')
ligne = canvas.create_line(largeur / 2, 0, largeur /2, hauteur, fill = 'white', dash = (4,2,4,4))
balle = canvas.create_oval((largeur / 2 - 10, hauteur / 2 - 10), (largeur / 2 + 10, hauteur / 2 + 10), fill = 'white')

    # Menu principal
menu = Frame(fenetre, )


# Placement des composants
canvas.pack()

# Appel des fonctions
gameTick()

# Boucle infinie
fenetre.mainloop()


