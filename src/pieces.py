from dataclasses import dataclass
from typing import List

conversions = {"a": 0, "b": 1,
               "c": 2, "d": 3,
               "e": 4, "f": 5,
               "g": 6, "h": 7}


@dataclass
class Piece:
    color: str
    #position: tuple[int, int]

    # Utile?
    def legal_move(self):
        pass

@dataclass
class Pawn(Piece):
    energy: int

    def move(self, start_position: tuple[int, int], new_position: tuple[int, int]):
        if self.energy > 1:
            self.position = new_position
        else:
            self.position = self.position
        return self.position

@dataclass
class Knight(Piece):

    def move(self):
        try:
            self.position = (0,0)
        except IndexError as e:
            print(e)
        return self.position

@dataclass
class King(Piece):

    def move(self):
        pass

@dataclass
class Rook(Piece):

    def move(self):
        pass

@dataclass
class Bishop(Piece):

    def move(self):
        pass

@dataclass
class Queen(Piece):

    def move(self):
        pass



@dataclass
class Board:
    game_state: int
    board = [[Rook("black"), Knight("black"), Bishop("black"), Queen("black"), King("black"), Bishop("black"), Knight("black"), Rook("black")],
             [Pawn("black", 2) for _ in range(8)],
             [" " for _ in range(8)],
             [" " for _ in range(8)],
             [" " for _ in range(8)],
             [" " for _ in range(8)],
             [Pawn("white", 2) for _ in range(8)],
             [Rook("white"), Knight("white"), Bishop("white"), Queen("white"), King("white"), Bishop("white"), Knight("white"), Rook("white")]
            ]

    def print_state_of_board(self):
        if self.game_state == 0:
            board = self.board
            for i in range(len(board)):
                print(board[i])


    def update_board_state(self, piece: Piece):
        pass


@dataclass
class Jeu:

    def play_turn(self):
        pass