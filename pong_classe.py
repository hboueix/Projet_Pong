from tkinter import *

#Classes
class MenuPrincipal: # lancement, /start_pong

    def __init__(self):
        self.menu = Frame(fenetre, borderwidth = 2, relief = GROOVE, bg = "white")
        self.menu.pack(expand = TRUE)
        Label(self.menu, text = 'Menu principal', font = '-size 50', bg = 'white').pack(padx = 100, pady = 50)
        Button(self.menu, text = 'Start', command = start_pong, font = '-size 22').pack(ipadx = 20, pady = 20)
        Button(self.menu, text = 'Quitter', command = fenetre.destroy, font = '-size 22').pack(ipadx = 20, pady = 20)


class Canevas: # start_pong

    def __init__(self):
        self.largeur = fenetre.winfo_screenwidth()
        self.hauteur = fenetre.winfo_screenheight()
        self.centre_x = self.largeur / 2
        self.centre_y = self.hauteur / 2
        self.canvas = Canvas(fenetre, width = self.largeur, height = self.hauteur, bg = 'black')
        self.ligne = self.canvas.create_line(self.centre_x, 0, self.centre_x, self.hauteur, fill = 'white', dash = (4,2,4,4))
        self.canvas.pack()


class Balle: # start_pong

    def __init__(self):
        self.balle = canvas.create_oval((can.centre_x - 10, can.centre_y - 10), (can.centre_x + 10, can.centre_y + 10), fill = 'white')

    dx, dy = 3, 3

    def gameTick(self):
        coo = canvas.coords(self.balle)
        coo1 = canvas.coords(raq1)
        coo2 = canvas.coords(raq2)
        if coo[0] <= coo1[0] or coo[2] >= coo2[2]:
            if Balle.dx < 0:
                scores['J2'] += 1
            else:
                scores['J1'] += 1
            canvas.itemconfigure(score.J1, text = scores['J1'])
            canvas.itemconfigure(score.J2, text = scores['J2'])
            canvas.coords(balle, can.centre_x - 10, can.centre_y - 10, can.centre_x + 10, can.centre_y + 10)
            fenetre.after(1000, self.gameTick)
        elif scores['J1'] == 3 or scores['J2'] == 3:
            victoire()
        else:
            if len(canvas.find_overlapping(coo1[0], coo1[1], coo1[2], coo1[3])) > 1 \
            or len(canvas.find_overlapping(coo2[0], coo2[1], coo2[2], coo2[3])) > 1:
                Balle.dx *= -1
            elif coo[1] <= 0 or coo[3] >= can.hauteur:
                Balle.dy *= -1
            canvas.move(balle, self.dx, self.dy)
            fenetre.after(10, self.gameTick)


class Raquettes: # start_pong

    def __init__(self):
        self.raq1 = canvas.create_rectangle(20, (can.centre_y - can.hauteur /10), 40, (can.centre_y + can.hauteur / 10), fill = 'white')
        self.raq2 = canvas.create_rectangle(can.largeur - 40, (can.centre_y - can.hauteur /10), can.largeur - 20, (can.centre_y + can.hauteur / 10), fill = 'white')
        canvas.focus_set()
        canvas.bind('<KeyPress>', move)


class Score(): # start_pong

    def __init__(self):
        self.J1 = canvas.create_text( (can.largeur / 2 - 50), 50, text = '0', fill = 'white', font = '-size 30')
        self.J2 = canvas.create_text( (can.largeur / 2 + 50), 50, text = '0', fill = 'white', font = '-size 30')


# Fonctions
def start_pong(): # menu
        global can, canvas, bal, balle, raq, raq1, raq2, score, scores
        menu.destroy()
        can = Canevas()
        canvas = can.canvas
        bal = Balle()
        balle = bal.balle
        raq = Raquettes()
        raq1, raq2 = raq.raq1, raq.raq2
        score = Score()
        scores = {'J1' : 0, 'J2' : 0}
        bal.gameTick()

def move(event): # clavier
    coo1 = canvas.coords(raq1)
    coo2 = canvas.coords(raq2)
    if event.keysym == 'z' and coo1[1] >= 25:
        canvas.move(raq1, 0, -25)
    elif event.keysym == 'x' and (can.hauteur - coo1[3]) >= 25:
        canvas.move(raq1, 0, 25)
    elif event.keysym == 'Up' and coo2[1] >= 25:
        canvas.move(raq2, 0, -25)
    elif event.keysym == 'Down' and (can.hauteur - coo2[3]) >= 25:
        canvas.move(raq2, 0, 25)

def victoire(): # gameTick
    global menu
    canvas.destroy()
    menu = MenuPrincipal().menu


# Fenêtre principale
fenetre = Tk()
fenetre.title('Pong')
fenetre.attributes('-fullscreen', 1)

# Création du menu au lancement
menu = MenuPrincipal().menu

# Boucle infinie
fenetre.mainloop()