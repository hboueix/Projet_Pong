from  tkinter import *

# Définition des fonctions

def ouvrir_menu():
    menu = Frame(fenetre, borderwidth = 2, relief = GROOVE, bg = "white")
    menu.pack(expand = TRUE)
    Label(menu, text = 'Menu principal', font = '-size 50', bg = 'white').pack(padx = 100, pady = 50)
    Button(menu, text = 'Start', command = start_pong, font = '-size 22').pack(ipadx = 20, pady = 20)
    Button(menu, text = 'Quitter', command = fenetre.destroy, font = '-size 22').pack(ipadx = 20, pady = 20)
    return menu

def start_pong():
    global canvas, ligne, balle
    canvas, ligne, balle = ouvrir_canvas()
    gameTick()

def ouvrir_canvas():
    menu.destroy()
    canvas = Canvas(fenetre, width = largeur, height = hauteur, bg = 'black')
    ligne = canvas.create_line(largeur / 2, 0, largeur /2, hauteur, fill = 'white', dash = (4,2,4,4))
    balle = canvas.create_oval((largeur / 2 - 10, hauteur / 2 - 10), (largeur / 2 + 10, hauteur / 2 + 10), fill = 'white')
    canvas.pack()
    return canvas, ligne, balle

def gameTick():
    global dx, dy
    coords = canvas.coords(balle) # coords = (x1, y1, x2, y2)
    if coords[0] <= 0 or coords[2] >= largeur:
        dx *= -1
    if coords[1] <= 0 or coords[3] >= hauteur:
        dy *= -1
    canvas.move(balle, dx, dy)
    fenetre.after(5, gameTick) 

# Fenêtre principale
fenetre = Tk()
fenetre.title('Pong')
fenetre.attributes('-fullscreen', 1)

# Création des variables
canvas, ligne, balle = None, None, None
largeur = fenetre.winfo_screenwidth()
hauteur = fenetre.winfo_screenheight()
dx, dy = 3, 3

# Appel des fonctions
menu = ouvrir_menu()

# Boucle infinie
fenetre.mainloop()