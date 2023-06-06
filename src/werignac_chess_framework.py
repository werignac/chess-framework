
'''
Basic components for a game of chess.

@author werignac
@version 6/5/2023
'''

from enum import Enum

'''
Interface for a generic square.
'''
class Square:
	def get_adjacency(self) -> set:
		pass
	def get_piece(self):
		pass

'''
Interface for a generic piece.
'''
class Piece:
	def get_possible_squares(self, square: Square) -> set:
		pass

	def get_adjacent_square(self, direction: Enum) -> Square:
		pass


'''
Interface for a generic board.
'''
class Board:
	def get_adjacency_types(self) -> type:
		pass
