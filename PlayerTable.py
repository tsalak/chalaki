from Piece import Piece
# from graphics import *
import pygame as pg


class PlayerTable:

    def __init__(self):
        self.repr = [[0 for x in range(9)] for y in range(9)]
        self.empty = 9 * 9
        self.pieces = []
        self.square = self.check_bonus()

    def __str__(self):
        string = ""
        for i in self.repr:
            for j in i:
                if int(j) == 1:
                    string += "O  "
                else:
                    string += ".  "
            string += "\n"
        return string + "Board Buttons: " + str(self.check_buttons()) + "\n"

    def place(self, piece, x, y):
        # if possible
        for i in piece.repr:
            for j in i:
                if int(j) == 1:
                    self.repr[x][y] = 1
                y += 1
            y -= len(i)
            x += 1
        self.pieces.append(piece)
        self.empty -= piece.length

    def can_place(self, piece, x, y):
        for i in piece.repr:
            for j in i:
                if int(j) == 1:
                    if x not in range(0, len(self.repr)) or y not in range(0, len(self.repr[x])):
                        return False
                    elif int(self.repr[x][y]) == 1:
                        return False

                y += 1
            y -= len(i)
            x += 1
        return True

    def check_bonus(self):
        consecutive = [[0 for x in range(9)] for y in range(9)]
        for i in range(0, len(self.repr)):
            for j in range(0, len(self.repr)):
                for k in range(0, j + 1):
                    if self.repr[i][k]:
                        consecutive[i][j] += 1
                    else:
                        consecutive[i][j] = 0
        for i in range(0, len(consecutive)):
            for j in range(0, len(consecutive)):
                if consecutive[i][j] >= 7 and i + 6 < len(consecutive):
                    for k in range(0, 7):
                        if consecutive[i + k][j] < 7:
                            break
                        if k == 6:
                            return True
        return False

    def check_buttons(self):
        but = 0
        for i in self.pieces:
            but += i.buttons
        return but

    def graph(self, window, startx, starty, color):
        for i in self.repr:
            for j in i:
                if int(j) == 1:
                    rect = pg.Rect(startx, starty, 20, 20)
                    pg.draw.rect(window, color, rect)
                else:
                    rect = pg.Rect(startx, starty, 20, 20)
                    pg.draw.rect(window, 'white', rect, 1)
                pg.draw.rect(window, 'black', rect, 1)
                startx += 20
            startx -= 20 * len(i)
            starty += 20
