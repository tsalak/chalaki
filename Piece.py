# from graphics import *
import pygame as pg
import random

colors = ["red", "yellow", "green", "blue", "purple", "orange"]

class Piece:

    def __init__(self, representation, length, cost, time, buttons):
        self.repr = representation
        self.length = length
        self.cost = cost
        self.time = time
        self.buttons = buttons
        self.color = random.choice(colors)

    def __str__(self):
        string = ""
        for i in self.repr:
            for j in i:
                if int(j) == 1:
                    string += "O  "
                else:
                    string += ".  "
            string += "\n"
        return string + "Cost: " + str(self.cost) + ", Time: " + str(self.time) + ", Buttons: " + str(self.buttons) + "\n"

    def possible_place(self, table):
        possibles = []
        for i in range(len(table.repr)):
            for j in range(len(table.repr[i])):
                if table.can_place(self, i, j):
                    possibles.append([i, j])
        return possibles

    def rotate(self):
        self.repr = [[self.repr[j][i] for j in range(len(self.repr))] for i in range(len(self.repr[0]))]
        self.flip()

    def flip(self):
        flipped = [[self.repr[len(self.repr) - 1 - i][j] for j in range(len(self.repr[0]))] for i in range(len(self.repr))]
        self.repr = flipped

    def graph(self, window, startx, starty, color, scale):
        for i in self.repr:
            for j in i:
                if int(j) == 1:
                    # rect = Rectangle(Point(startx, starty), Point(startx + scale, starty + scale))
                    # surf = pg.Surface((scale, scale))
                    rect = pg.Rect(startx, starty, scale, scale)
                    if not color:
                        # rect.setFill(self.color)
                        color = self.color
                    # rect.draw(window)
                    pg.draw.rect(window, color, rect)
                    pg.draw.rect(window, "black", rect, 1)
                startx += scale
            startx -= scale * len(i)
            starty += scale
        return window