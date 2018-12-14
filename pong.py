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
    global canvas, ligne, balle, raq1, raq2, J1, J2
    canvas, ligne, balle, raq1, raq2, J1, J2 = ouvrir_canvas()
    clavier()
    score()
    move_balle()


def ouvrir_canvas():
    menu.pack_forget()
    canvas = Canvas(fenetre, width = largeur, height = hauteur, bg = 'black')
    ligne = canvas.create_line(centre_x, 0, centre_x, hauteur, fill = 'white', dash = (4,2,4,4))
    balle = canvas.create_oval((centre_x - 10, centre_y - 10), (centre_x + 10, centre_y + 10), fill = 'white')
    raq1 = canvas.create_rectangle(20, (centre_y - hauteur /10), 40, (centre_y + hauteur / 10), fill = 'white')
    raq2 = canvas.create_rectangle(largeur - 40, (centre_y - hauteur /10), largeur - 20, (centre_y + hauteur / 10), fill = 'white')
    J1 = canvas.create_text( (largeur / 2 - 50), 50, text = '0', fill = 'white', font = '-size 30')
    J2 = canvas.create_text( (largeur / 2 + 50), 50, text = '0', fill = 'white', font = '-size 30')
    canvas.pack()
    return canvas, ligne, balle, raq1, raq2, J1, J2


def clavier():
    canvas.bind_all('x', move_down_J1)
    canvas.bind_all('z', move_up_J1)
    canvas.bind_all('<Down>', move_down_J2)
    canvas.bind_all('<Up>', move_up_J2)
    tour_J()


def move_balle():
    global dx, dy, menu, score
    coo_b = canvas.coords(balle) # coo_b = (x1, y1, x2, y2)
    coo1 = canvas.coords(raq1)
    coo2 = canvas.coords(raq2)
    if coo_b[0] <= coo1[0] or coo_b[2] >= coo2[2]:
        if dx < 0:
            scores['J2'] += 1
        elif dx > 0:
            scores['J1'] += 1
        score()
        canvas.coords(balle, centre_x - 10, centre_y - 10, centre_x + 10, centre_y + 10)
        fenetre.after(1000, move_balle)
    elif scores['J1'] == 3 or scores['J2'] == 3:
        canvas.pack_forget()
        menu.pack(expand = TRUE)
    else:    
        if coo_b[1] <= 0 or coo_b[3] >= hauteur:
            dy *= -1
        if len(canvas.find_overlapping(coo1[0], coo1[1], coo1[2], coo1[3])) > 1 or len(canvas.find_overlapping(coo2[0], coo2[1], coo2[2], coo2[3])) > 1:
            dx *= -1
        canvas.move(balle, dx, dy)
        fenetre.after(10, move_balle)


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
    fenetre.after(1, tour_J)


def move_up_J1(event):
    coo = canvas.coords(raq1)
    if coo[1] >= 25:
        canvas.move(raq1, 0, -25)

def move_down_J1(event):
    coo = canvas.coords(raq1)
    if (hauteur - coo[3]) >= 25:
        canvas.move(raq1, 0, 25)

def move_up_J2(event):
    coo = canvas.coords(raq2)
    if coo[1] >= 25:
        canvas.move(raq2, 0, -25)

def move_down_J2(event):
    coo = canvas.coords(raq2)
    if (hauteur - coo[3]) >= 25:
        canvas.move(raq2, 0, 25)


def score():
    canvas.itemconfigure(J1, text = scores['J1'])
    canvas.itemconfigure(J2, text = scores['J2'])



# Fenêtre principale
fenetre = Tk()
fenetre.title('Pong')
fenetre.attributes('-fullscreen', 1)



# Création des variables
canvas, ligne, balle, raq1, raq2, J1, J2 = (0 for i in range(7))
largeur = fenetre.winfo_screenwidth()
hauteur = fenetre.winfo_screenheight()
centre_x = largeur / 2
centre_y = hauteur / 2
dx, dy = 3, 3
scores = {'J1' : 0, 'J2' : 0}


# Appel des fonctions
menu = ouvrir_menu()


# Boucle infinie
fenetre.mainloop()