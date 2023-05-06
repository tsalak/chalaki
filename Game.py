import random
import pygame as pg
import os

from Player import Player
from Table import Table
from Piece import Piece
from HumanPlayer import HumanPlayer

class Game:
    def __init__(self, name1, name2):
        self.players = [HumanPlayer(0, name1), HumanPlayer(1, name2)]
        self.board = Table()
        self.pieces = []
        self.win = pg.display.set_mode((1250, 500))
        pg.display.set_caption("Chalaki")
        self.font = pg.font.Font(pg.font.get_default_font(), 15)
        self.bonus = -1
        for line in open("pieces.txt", "r"):
            sample = line.split()
            sample[0] = sample[0].split("$")
            for i in range(0, len(sample[0])):
                sample[0][i] = sample[0][i].split("#")
            self.pieces.append(Piece(sample[0], int(sample[1]), int(sample[2]), int(sample[3]), int(sample[4])))
        random.shuffle(self.pieces)
        for i in range(0, len(self.pieces)):
            if self.pieces[i].length == 2:
                if i + 1 < len(self.pieces):
                    self.pawn = i + 1
                else:
                    self.pawn = 0
                break

    def __str__(self):
        rep = ""
        for i in self.pieces:
            if self.pieces.index(i) == self.pawn:
                rep += "---PAWN---\n\n"
            rep += str(i) + "\n"
        return "\n\n" + "GAME BOARD" + str(self.board) + "\n\n\n" + self.players[0].name + "\n" + str(self.players[0]) \
               + "\n\n" + self.players[1].name + "\n" + str(self.players[1]) + "\n\n\n" + rep

    def check_square(self, move=None):
        if not move:
            if self.board.pawns[0].pos in self.board.button:
                self.players[self.board.pawns[0].id].buttons += \
                    self.players[self.board.pawns[0].id].table.check_buttons()
            elif self.board.pawns[0].pos in self.board.piece_positions:
                self.players[self.board.pawns[0].id].to_place(self.board.piece)
                self.board.piece_positions.remove(self.board.pawns[0].pos)
        else:
            for i in move:
                if i in self.board.button:
                    self.players[self.board.pawns[0].id].buttons += \
                        self.players[self.board.pawns[0].id].table.check_buttons()
                elif i in self.board.piece_positions:
                    self.players[self.board.pawns[0].id].to_place(self.board.piece)
                    self.board.piece_positions.remove(i)

    def skip(self):
        moving = self.board.pawns[0].id
        while self.board.pawns[0].id == moving and self.board.pawns[0].pos < 53:
            self.board.move_pawn(1)
            self.players[moving].buttons += 1
            self.check_square()

    def game_over(self):
        if self.board.pawns[0].pos >= 53:
            return True
        return False

    def next_pieces(self):
        possibles = []
        for i in range(self.pawn, self.pawn + 3):
            possibles.append(self.pieces[i % len(self.pieces)])
        return possibles

    def buy(self, pick):
        to_buy = self.pieces.pop((self.pawn + pick) % len(self.pieces))
        self.players[self.board.pawns[0].id].to_place(to_buy)
        self.players[self.board.pawns[0].id].buttons -= to_buy.cost
        self.check_square(range(self.board.pawns[0].pos, self.board.pawns[0].pos + to_buy.time))
        self.board.move_pawn(to_buy.time)
        self.pawn = (self.pawn + pick) % (len(self.pieces) + 1)

    def play(self):
        while not self.game_over():
            pg.event.pump()
            self.graph()
            possibles = self.next_pieces()
            x = 750
            y = 250
            for i in possibles:
                i.graph(self.win, x, y, None, 20)
                label1 = self.font.render(f"Cost: {str(i.cost)}", True, 'black')
                label2 = self.font.render(f"Buttons: {str(i.buttons)}", True, 'black')
                label3 = self.font.render(f"Time: {str(i.time)}", True, 'black')
                label1_rect = label1.get_rect(topleft = (x, y + 20 * 6))
                label2_rect = label2.get_rect(topleft = (x, y + 20 * 6 + 20))
                label3_rect = label3.get_rect(topleft = (x, y + 20 * 6 + 40))
                self.win.blit(label1, label1_rect)
                self.win.blit(label2, label2_rect)
                self.win.blit(label3, label3_rect)
                x += 20 * 6
            playing = self.players[self.board.pawns[0].id]
            label = self.font.render(("You have " + str(playing.buttons) + " buttons"), True, 'black')
            label_rect = label.get_rect(topleft = (850, 450))
            self.win.blit(label, label_rect)
            pg.display.flip()
            print(str(self.board) + "\n\n" + str(playing.table))
            action = playing.pick_place(possibles)
            if action >= 0:
                self.buy(action)
            else:
                self.skip()
            if self.bonus < 0 and playing.table.check_bonus():
                self.bonus = playing.id
            print(self)
        return self.calculate_scores()

    def calculate_scores(self):
        scores = [0, 0]
        for i in range(0, 2):
            scores[i] = self.players[i].buttons - self.players[i].table.empty * 2
        if self.bonus == i:
            scores[i] += 7
        return scores

    def graph(self):
        self.win.fill('white')
        x = 10 * 6 * 6 + 10
        y = 200 - 10 * 5
        color = None
        for i in range(0, len(self.pieces)):
            if i % 6 == 0:
                x -= 10 * 6 * 6
                y += 10 * 5
            if i == self.pawn:
                color = "white"
            self.win = self.pieces[i].graph(self.win, x, y, color, 10)
            color = None
            x += 10 * 6
        wait = 0
        for i in self.players:
            if i.id == 0:
                i.table.graph(self.win, 400 + wait, 0, "Green")
            else:
                i.table.graph(self.win, 400 + wait, 0, "Red")
            wait = 200
        self.board.graph(self.win, 75, 25)

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,30)
pg.init()
game = Game("Player1", "Player2")
print(game.play())
pg.quit()
