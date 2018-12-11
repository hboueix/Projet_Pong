from  tkinter import *

# Fenetre principale
fenetre = Tk()
fenetre.title('Pong')
fenetre.attributes('-fullscreen', 1)

# Création des fonctions

    # Menu principal
def ouvrir_menu():
    menu = Frame(fenetre, borderwidth = 2, relief = GROOVE, bg = 'white')
    menu.pack(padx = 10, pady = 10)
    Label(menu, text = 'Menu principal', font = '-size 50', bg = 'white').pack(padx = 100, pady = 50)
    Button(menu, text = 'Start', command = start_pong, font = '-size 22').pack(padx = 20, pady = 20)
    Button(menu, text = 'Quitter', command = fenetre.destroy, font = '-size 22').pack(padx = 20, pady = 20)
    return menu

    # Lancement du Pong
def start_pong():
    menu.destroy()
    canvas = Canvas(fenetre, width = largeur, height = hauteur, bg = 'black')
    ligne = canvas.create_line(largeur / 2, 0, largeur /2, hauteur, fill = 'white', dash = (4,2,4,4))
    balle = canvas.create_oval((largeur / 2 - 10, hauteur / 2 - 10), (largeur / 2 + 10, hauteur / 2 + 10), fill = 'white')
    canvas.pack()

    # Déplacement balle
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
menu = ouvrir_menu()

# Appel des fonctions
#gameTick()
menu

# Dimensions automatique de la fenêtre
fenetre.geometry(dimensions)

# Boucle infinie
fenetre.mainloop()


