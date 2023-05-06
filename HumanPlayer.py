from Player import Player


class HumanPlayer(Player):
    def __init__(self, id, name):
        super().__init__(id, name)

    def pick_place(self, pieces):
        print("Available Pieces:\n1)\n" + str(pieces[0]) + "2)\n" + str(pieces[1]) + "3)\n" + str(pieces[2]))
        print("\nYou have " + str(self.buttons) + " buttons\n")
        pick = input("\nInput 1, 2 or 3 to Buy Piece or P for Pass\n")
        if pick == "P" or pick == "p":
            validate = input("\nAre you sure? (y/n)\n")
            if validate == "y":
                return -1
            elif validate == "n":
                return self.pick_place(pieces)
            else:
                print("\nInvalid input\n")
                return self.pick_place(pieces)
        elif pick in "123":
            if pieces[int(pick) - 1].cost > self.buttons:
                print("Not enough buttons")
                return self.pick_place(pieces)
            if not pieces[int(pick) - 1].possible_place(self.table):
                print("Not enough space on board")
                return self.pick_place(pieces)
            validate = input("\nAre you sure? (y/n)\n")
            if validate == "y":
                return int(pick) - 1
            elif validate == "n":
                return self.pick_place(pieces)
            else:
                print("\nInvalid input\n")
                return self.pick_place(pieces)
        else:
            print("\nInvalid Input\n")
            return self.pick_place(pieces)

    def to_place(self, piece):
        print("\nWhere to place: \n" + str(piece))
        action = input("\nDo you wanna flip or rotate? (f/r/n)\n")
        if action not in "frnFRN":
            print("\nInvalid Input\n")
            return self.to_place(piece)
        elif action in "fF":
            piece.flip()
            return self.to_place(piece)
        elif action in "rR":
            piece.rotate()
            return self.to_place(piece)
        else:
            place = input("\nBoard coordinates (xy)\n")
            if len(place) == 2:
                for i in place:
                    if i not in "123456789":
                        print("\nInvalid Input\n")
                        return self.to_place(piece)
                coords = [int(place[0]), int(place[1])]
                if self.table.can_place(piece, coords[0] - 1, coords[1] - 1):
                    validate = input("\nAre you sure? (y/n)\n")
                    if validate == "y":
                        self.table.place(piece, coords[0] - 1, coords[1] - 1)
                    elif validate == "n":
                        return self.to_place(piece)
                    else:
                        print("\nInvalid input\n")
                        return self.to_place(piece)
                else:
                    print("Can't place there")
                    return self.to_place(piece)
            else:
                print("\nInvalid Input\n")
                return self.to_place(piece)