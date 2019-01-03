from tkinter import *
import time

#Classes
class MenuPrincipal: # lancement, /parametrage

    def __init__(self):
        self.menu = Frame(fenetre, borderwidth = 2, relief = GROOVE, bg = "white")
        self.menu.pack(expand = TRUE)
        Label(self.menu, text = 'Menu principal', font = '-size 50', bg = 'white').pack(padx = 100, pady = 50)
        Button(self.menu, text = 'Start', command = parametrage, font = '-size 22').pack(ipadx = 20, pady = 20)
        Button(self.menu, text = 'Quitter', command = fenetre.destroy, font = '-size 22').pack(ipadx = 20, pady = 20)

class EcranParametre: # parametrage, /start_pong

    def __init__(self):
        var_win, var_vit = StringVar(), StringVar()
        var_win.set(3)
        var_vit.set(3)

        self.ecran = Frame(fenetre, borderwidth = 2, relief = GROOVE, bg = "white")
        self.ecran.pack(expand = TRUE)
        Label(self.ecran, text = 'Paramètres', font = '-size 50', bg = 'white').grid(row = 0, column = 0, columnspan = 5, padx = 100, pady = 50)

        Label(self.ecran, text = 'Points gagnants :', font = '-size 15', bg = 'white').grid(row = 1, column = 2)
        self.e_win = Entry(self.ecran, textvariable = var_win, width = 10, relief = GROOVE, bd = 3)
        self.e_win.grid(row = 1, column = 3, ipadx = 20, pady = 20)

        Label(self.ecran, text = 'Vitesse de la balle (en px) :', font = '-size 15', bg = 'white').grid(row = 2, column = 2)
        self.e_vit = Entry(self.ecran, textvariable = var_vit, width = 10, relief = GROOVE, bd = 3)
        self.e_vit.grid(row = 2, column = 3, ipadx = 20, pady = 20)

        Label(self.ecran, text = 'Couleur des raquettes :', font = '-size 15', bg = 'white').grid(row = 3, column = 2)
        self.couleurs_raq = Listbox(self.ecran, selectmode = 'single', width = 10, height = 1, exportselection = 0)
        self.couleurs_raq.grid(row = 3, column = 3, ipadx = 20, ipady = 20, padx = 20, pady = 20)
        self.couleurs_raq.insert(END, 'Blanc')
        self.couleurs_raq.insert(END, 'Noir')
        self.couleurs_raq.insert(END, 'Rouge')
        self.couleurs_raq.insert(END, 'Bleu')
        self.couleurs_raq.insert(END, 'Vert')
        self.couleurs_raq.insert(END, 'Jaune')

        Label(self.ecran, text = 'Couleur de la balle :', font = '-size 15', bg = 'white').grid(row = 4, column = 2)
        self.couleurs_ba = Listbox(self.ecran, selectmode = 'single', width = 10, height = 1, exportselection = 0)
        self.couleurs_ba.grid(row = 4, column = 3, ipadx = 20, ipady = 20, padx = 20, pady = 20)
        self.couleurs_ba.insert(END, 'Blanc')
        self.couleurs_ba.insert(END, 'Noir')
        self.couleurs_ba.insert(END, 'Rouge')
        self.couleurs_ba.insert(END, 'Bleu')
        self.couleurs_ba.insert(END, 'Vert')
        self.couleurs_ba.insert(END, 'Jaune')

        Label(self.ecran, text = 'Couleur du background :', font = '-size 15', bg = 'white').grid(row = 5, column = 2)
        self.couleurs_bg = Listbox(self.ecran, selectmode = 'single', width = 10, height = 1, exportselection = 0)
        self.couleurs_bg.grid(row = 5, column = 3, ipadx = 20, ipady = 20, padx = 20, pady = 20)
        self.couleurs_bg.insert(END, 'Noir')
        self.couleurs_bg.insert(END, 'Rouge')
        self.couleurs_bg.insert(END, 'Bleu')
        self.couleurs_bg.insert(END, 'Vert')
        self.couleurs_bg.insert(END, 'Jaune')

        Button(self.ecran, text = 'OK', command = start_pong, font = '-size 22').grid(row = 6, column = 2, columnspan = 2, ipadx = 20, pady = 20)
        

class EcranFin:

    def __init__(self):
        self.ecran = Frame(fenetre, borderwidth = 2, relief = GROOVE, bg = "white")
        self.ecran.pack(expand = TRUE)
        Label(self.ecran, text = gagnant + ' a gagné !', font = '-size 50', bg = 'white').grid(row = 0, column = 0, columnspan = 5, padx = 100, pady = 50)
        Label(self.ecran, text = 'J1 : ' + str(scores['J1']) + ' points', font = '-size 15', bg = 'white').grid(row = 1, column = 1, ipadx = 20, ipady = 20)
        Label(self.ecran, text = 'J2 : ' + str(scores['J2']) + ' points', font = '-size 15', bg = 'white').grid(row = 1, column = 3, ipadx = 20, ipady = 20)
        Label(self.ecran, text = 'Le match a duré : ' + str(durée) + ' secondes.', font = '-size 15', bg = 'white').grid(row = 2, column = 1, columnspan = 3, ipadx = 20, ipady = 20, padx = 20, pady = 20)
        Button(self.ecran, text = 'Rejouer', command = rejouer, font = '-size 22').grid(row = 5, column = 1, padx = 70, ipadx = 20, pady = 20)
        Button(self.ecran, text = 'Menu', command = reboot, font = '-size 22').grid(row = 5, column = 3, padx = 70, ipadx = 20, pady = 20)


class Canevas: # start_pong

    def __init__(self):
        self.largeur = fenetre.winfo_screenwidth()
        self.hauteur = fenetre.winfo_screenheight()
        self.centre_x = self.largeur / 2
        self.centre_y = self.hauteur / 2
        self.canvas = Canvas(fenetre, width = self.largeur, height = self.hauteur, bg = coul_bg)
        self.ligne = self.canvas.create_line(self.centre_x, 0, self.centre_x, self.hauteur, fill = 'white', dash = (4,2,4,4))
        self.canvas.pack()


class Balle: # start_pong

    def __init__(self):
        self.balle = canvas.create_oval((can.centre_x - 10, can.centre_y - 10), (can.centre_x + 10, can.centre_y + 10), fill = coul_ba)

    def gameTick(self):
        global dx, dy
        coo = canvas.coords(self.balle)
        coo1 = canvas.coords(raq1)
        coo2 = canvas.coords(raq2)
        dx = int(dx)
        dy = int(dy)
        if coo[0] <= coo1[0] or coo[2] >= coo2[2]:
            if dx < 0:
                scores['J2'] += 1
            else:
                scores['J1'] += 1
            canvas.itemconfigure(score.J1, text = scores['J1'])
            canvas.itemconfigure(score.J2, text = scores['J2'])
            canvas.coords(balle, can.centre_x - 10, can.centre_y - 10, can.centre_x + 10, can.centre_y + 10)
            fenetre.after(1000, self.gameTick)
        elif scores['J1'] == int(win) or scores['J2'] == int(win):
            victoire()
        else:
            if len(canvas.find_overlapping(coo1[0], coo1[1], coo1[2], coo1[3])) > 1 \
            or len(canvas.find_overlapping(coo2[0], coo2[1], coo2[2], coo2[3])) > 1:
                dx *= -1
            elif coo[1] <= 0 or coo[3] >= can.hauteur:
                dy *= -1
            canvas.move(balle, dx, dy)
            fenetre.after(10, self.gameTick)


class Raquettes: # start_pong

    def __init__(self):
        self.raq1 = canvas.create_rectangle(20, (can.centre_y - can.hauteur /10), 40, (can.centre_y + can.hauteur / 10), fill = coul_raq)
        self.raq2 = canvas.create_rectangle(can.largeur - 40, (can.centre_y - can.hauteur /10), can.largeur - 20, (can.centre_y + can.hauteur / 10), fill = coul_raq)
        canvas.focus_set()
        canvas.bind('<KeyPress>', move)


class Score(): # start_pong

    def __init__(self):
        self.J1 = canvas.create_text( (can.largeur / 2 - 50), 50, text = '0', fill = 'white', font = '-size 30')
        self.J2 = canvas.create_text( (can.largeur / 2 + 50), 50, text = '0', fill = 'white', font = '-size 30')


# Fonctions
def parametrage(): # menu
    global ecr, ecran
    menu.destroy()
    ecr = EcranParametre()
    ecran = ecr.ecran 

def start_pong(): # ecran_para
    global can, canvas, bal, balle, raq, raq1, raq2, score, scores, win, dx, dy, coul_raq, coul_ba, coul_bg, t_debut
    win = ecr.e_win.get()
    if win == '':
        win = 3
    dx = ecr.e_vit.get()
    if dx == '':
        dx = 3
    dy = dx
    coul_raq = couleurs(ecr.couleurs_raq.curselection(), 0)
    coul_ba = couleurs(ecr.couleurs_ba.curselection(), 0)
    coul_bg = couleurs(ecr.couleurs_bg.curselection(), 1)
    ecran.destroy()
    can = Canevas()
    canvas = can.canvas
    bal = Balle()
    balle = bal.balle
    raq = Raquettes()
    raq1, raq2 = raq.raq1, raq.raq2
    score = Score()
    scores = {'J1' : 0, 'J2' : 0}
    bal.gameTick()
    t_debut = time.time()

def couleurs(ind, bg): # start_pong
    colors = {0 : 'white', 1 : 'black', 2 : 'red', 3 : 'blue', 4 : 'green', 5 : 'yellow'}
    if ind == ():
        if bg == 0:
            color = 'white'
        elif bg == 1:
            color = 'black'
    else:
        if bg == 0:
            for i in ind:
                color = colors[i]
        elif bg == 1:
            for i in ind:
                color = colors[i + 1]
    return color


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
    global gagnant, fin, durée
    t_fin = time.time()
    t = t_fin - t_debut
    durée = round(t, 1)
    if scores['J1'] == int(win):
        gagnant = 'J1'
    elif scores['J2'] == int(win):
        gagnant = 'J2'
    canvas.destroy()
    fin = EcranFin().ecran

def reboot(): # ecran_fin
    global menu
    fin.destroy()
    menu = MenuPrincipal().menu

def rejouer(): # ecran_fin
    global ecr, ecran
    fin.destroy()
    ecr = EcranParametre()
    ecran = ecr.ecran 


# Fenêtre principale
fenetre = Tk()
fenetre.title('Pong')
fenetre.attributes('-fullscreen', 1)

# Création du menu au lancement
menu = MenuPrincipal().menu

# Boucle infinie
fenetre.mainloop()