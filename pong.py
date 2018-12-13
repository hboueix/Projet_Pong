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
    global canvas, ligne, balle, raq1, raq2
    canvas, ligne, balle, raq1, raq2 = ouvrir_canvas()
    canvas.focus_set()
    clavier()
    move_balle()

def ouvrir_canvas():
    menu.destroy()
    canvas = Canvas(fenetre, width = largeur, height = hauteur, bg = 'black')
    ligne = canvas.create_line(largeur / 2, 0, largeur /2, hauteur, fill = 'white', dash = (4,2,4,4))
    balle = canvas.create_oval((largeur / 2 - 10, hauteur / 2 - 10), (largeur / 2 + 10, hauteur / 2 + 10), fill = 'white')
    raq1 = canvas.create_rectangle(20, (hauteur / 2 - hauteur /10), 40, (hauteur / 2 + hauteur / 10), fill = 'white')
    raq2 = canvas.create_rectangle(largeur - 40, (hauteur / 2 - hauteur /10), largeur - 20, (hauteur / 2 + hauteur / 10), fill = 'white')
    canvas.pack()
    return canvas, ligne, balle, raq1, raq2

def clavier():
    canvas.bind_all('x', move_down_J1)
    canvas.bind_all('z', move_up_J1)
    canvas.bind_all('<Down>', move_down_J2)
    canvas.bind_all('<Up>', move_up_J2)
    tour_J()

def move_balle():
    global dx, dy
    coords = canvas.coords(balle) # coords = (x1, y1, x2, y2)
    if coords[0] <= 0 or coords[2] >= largeur:
        dx *= -1
    if coords[1] <= 0 or coords[3] >= hauteur:
        dy *= -1
    canvas.move(balle, dx, dy)
    fenetre.after(5, move_balle) 

def tour_J():
    if dx > 0:
        canvas.unbind_all('x')
        canvas.unbind_all('z')
        canvas.bind_all('<Down>', move_down_J2)
        canvas.bind_all('<Up>', move_up_J2)
    if dx < 0:
        canvas.unbind_all('<Down>')
        canvas.unbind_all('<Up>')
        canvas.bind_all('x', move_down_J1)
        canvas.bind_all('z', move_up_J1)
    fenetre.after(5, tour_J)

def move_up_J1(event):
    canvas.move(raq1, 0, -30)

def move_down_J1(event):
    canvas.move(raq1, 0, 30)

def move_up_J2(event):
    canvas.move(raq2, 0, -30)

def move_down_J2(event):
    canvas.move(raq2, 0, 30)

def balle_raq():
    pass

# Fenêtre principale
fenetre = Tk()
fenetre.title('Pong')
fenetre.attributes('-fullscreen', 1)

# Création des variables
canvas, ligne, balle, raq1, raq2 = 0, 0, 0, 0, 0
largeur = fenetre.winfo_screenwidth()
hauteur = fenetre.winfo_screenheight()
dx, dy = 3, 3

# Appel des fonctions
menu = ouvrir_menu()


# Boucle infinie
fenetre.mainloop()