from tkinter import *

fenetre = Tk()
fenetre.title('Pong')
fenetre.attributes('-fullscreen', 1)

class Canevas:

    def __init__(self):
        self.largeur = fenetre.winfo_screenwidth()
        self.hauteur = fenetre.winfo_screenheight()
        self.centre_x = self.largeur / 2
        self.centre_y = self.hauteur / 2
        self.canvas = Canvas(fenetre, width = self.largeur, height = self.hauteur, bg = 'black')
        self.ligne = self.canvas.create_line(self.centre_x, 0, self.centre_x, self.hauteur, fill = 'white', dash = (4,2,4,4))
        self.canvas.pack()

class Balle:

    def __init__(self):
        self.balle = canvas.create_oval((can.centre_x - 10, can.centre_y - 10), (can.centre_x + 10, can.centre_y + 10), fill = 'white')

    dx, dy = 3, 3

    def gameTick(self):
        coo = canvas.coords(self.balle)
        if coo[0] <= 0 or coo[2] >= can.largeur:
            Balle.dx *= -1
        if coo[1] <= 0 or coo[3] >= can.hauteur:
            Balle.dy *= -1
        canvas.move(balle, self.dx, self.dy)
        fenetre.after(10, self.gameTick)

can = Canevas()
canvas = can.canvas
bal = Balle()
balle = bal.balle

bal.gameTick()

fenetre.mainloop()