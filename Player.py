from PlayerTable import PlayerTable


class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.buttons = 5
        self.table = PlayerTable()

    def __str__(self):
        return str(self.table) + "BUTTONS: " + str(self.buttons)

    def to_place(self, piece):
        possible = piece.possible_place(self.table)
        self.table.place(piece, possible[0][0], possible[0][1])

    def pick_place(self, pieces):
        for i in pieces:
            if i.possible_place(self.table) and self.buttons >= i.cost:
                return pieces.index(i)
        return -1