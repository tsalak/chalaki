from Piece import Piece
import pygame as pg


class Pawn:
    def __init__(self, id):
        self.pos = 0
        self.id = id

    def __str__(self):
        return str(self.pos)


class Table:
    def __init__(self):
        self.pawns = [Pawn(0), Pawn(1)]
        self.length = 53
        self.button = [5, 11, 17, 23, 29, 35, 41, 47, 53]
        self.piece = Piece([[1]], 1, 0, 0, 0)
        self.piece_positions = [26, 32, 38, 44, 50]

    def __str__(self):
        rep = ""
        for i in range(0, self.length + 1):
            if i % 9 == 0:
                rep += "\n"
            if i == self.pawns[0].pos or i == self.pawns[1].pos:
                if i == self.pawns[1].pos:
                    rep += "P" + str(self.pawns[1].id + 1)
                if i == self.pawns[0].pos:
                    rep += "P" + str(self.pawns[0].id + 1)
            else:
                if i in self.button:
                    rep += "B"
                elif i in self.piece_positions:
                    rep += "P"
                else:
                    rep += "o"
            rep += "  "
        return rep

    def move_pawn(self, steps):
        if self.pawns[0].pos + steps <= self.length:
            self.pawns[0].pos += steps
        else:
            self.pawns[0].pos = self.length
        if self.pawns[0].pos > self.pawns[1].pos:
            self.pawns.reverse()

    def graph(self, window, startx, starty):
        starty -= 20
        startx += 20 * 9
        for i in range(0, self.length + 1):
            if i % 9 == 0:
                starty += 20
                startx -= 20 * 9
            if i == self.pawns[0].pos and i == self.pawns[1].pos:
                rect1 = pg.Rect(startx, starty, 10, 20)
                if self.pawns[1].id == 0:
                    rect1color = "green"
                else:
                    rect1color = "red"
                pg.draw.rect(window, rect1color, rect1)
                pg.draw.rect(window, 'black', rect1, 1)
                rect2 = pg.Rect(startx+10, starty, 20, 20)
                if self.pawns[0].id == 0:
                    rect2color = "green"
                else:
                    rect2color = "red"
                pg.draw.rect(window, rect2color, rect2)
                pg.draw.rect(window, 'black', rect2, 1)
            elif i == self.pawns[0].pos or i == self.pawns[1].pos:
                if i == self.pawns[1].pos:
                    rect = pg.Rect(startx, starty, 20, 20)
                    if self.pawns[1].id == 0:
                        rectcolor = "green"
                    else:
                        rectcolor = "red"
                    pg.draw.rect(window, rectcolor, rect)
                    pg.draw.rect(window, 'black', rect, 1)
                if i == self.pawns[0].pos:
                    rect = pg.Rect(startx, starty, 20, 20)
                    if self.pawns[0].id == 0:
                        rectcolor = "green"
                    else:
                        rectcolor = "red"
                    pg.draw.rect(window, rectcolor, rect)
                    pg.draw.rect(window, 'black', rect, 1)
            else:
                rect = pg.Rect(startx, starty, 20, 20)
                rectcolor = "white"
                if i in self.button:
                    rectcolor = "blue"
                elif i in self.piece_positions:
                    rectcolor = "brown"
                pg.draw.rect(window, rectcolor, rect)
                pg.draw.rect(window, 'black',rect, 1)
            startx += 20
