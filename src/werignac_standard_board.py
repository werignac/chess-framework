'''
Components for a standard game of chess.

@auhtor werignac
@version 6/5/2023
'''

import werignac_chess_framework as cf
from enum import Enum

class StandardAdjacency(Enum):
	UP: (0,1)
	DOWN: (0,-1)
	RIGHT: (1, 0)
	LEFT: (-1, 0)
	RIGHT_UP: (1, 1)
	LEFT_UP: (-1, 1)
	RIGHT_DOWN: (1, -1)
	LEFT_DOWN: (-1, -1)

'''
Square
'''

class StandardSquare(cf.Square):
	def __init__(self, _adjacency: dict):
		self.adjacency = _adjacency

	def get_adjacency(self) -> set:
		return set(self.adjacency.keys())

	def get_adjacent_square(self, direction: Enum) -> cf.Square:
		if direction in self.adjacency:
			return self.adjacency[direction]
		return None

'''
Pieces
'''

#TODO: Take piece movement out of pieces and into a piece mover or in rules.

class StandardPawn(cf.Piece):
	def __init__(self):
		self.has_moved = False


class StandardKnight(cf.Piece):


class StandardBishop(cf.Piece):
	def get_possible_squares(self, square, rules) -> set:
		possible_squares = set()

		for direction in {StandardAdjacency.RIGHT_UP, StandardAdjacency.LEFT_UP, StandardAdjacency.RIGHT_DOWN, StandardAdjacency.LEFT_DOWN}:
			current_square = square
			# TODO: turn into a standard movement function
			while current_square := square.get_adjacent_square(direction):
				# If we run into another piece this way...
				if other := current_square.get_piece():
					# If we can take it, do so and stop.
					if rules.can_take(self, other):
						possible_squares.add(square)
					# Otherwise, just stop.
					break
				# If there is no piece, we can move to this square
				# and look for the next
				possible_squares.add(square)

		return possible_squares

class StandardRook(cf.Piece):
	def get_possible_squares(self, square, rules) -> set:
		possible_squares = set()

		for direction in {StandardAdjacency.UP, StandardAdjacency.DOWN, StandardAdjacency.LEFT, StandardAdjacency.RIGHT}:
			current_square = square
			# TODO: turn into a standard movement function
			while current_square := square.get_adjacent_square(direction):
				# If we run into another piece this way...
				if other := current_square.get_piece():
					# If we can take it, do so and stop.
					if rules.can_take(self, other):
						possible_squares.add(square)
					# Otherwise, just stop.
					break
				# If there is no piece, we can move to this square
				# and look for the next
				possible_squares.add(square)

		return possible_squares


class StandardQueen(cf.Piece):
	def get_possible_squares(self, square, rules) -> set:
		possible_squares = set()

		for direction in {e.value for e in StandardAdjacency}:
			current_square = square
			# TODO: turn into a standard movement function
			while current_square := square.get_adjacent_square(direction):
				# If we run into another piece this way...
				if other := current_square.get_piece():
					# If we can take it, do so and stop.
					if rules.can_take(self, other):
						possible_squares.add(square)
					# Otherwise, just stop.
					break
				# If there is no piece, we can move to this square
				# and look for the next
				possible_squares.add(square)

		return possible_squares


class StandardKing(cf.Piece):
	def get_possible_squares(self, square, rules) -> set:
		possible_squares = set()

		for direction in {e.value for e in StandardAdjacency}:
			current_square = square
			# TODO: turn into a standard movement function
			if current_square := square.get_adjacent_square(direction):
				# If we run into another piece this way...
				if other := current_square.get_piece():
					# If we can take it, do so and stop.
					# TODO: Ensure Kings cannot get in range of other Kings
					if rules.can_take(self, other):
						possible_squares.add(square)
				else:
					# If there is no piece, we can move to this square
					# and look for the next
					possible_squares.add(square)

		return possible_squares



'''
Board
'''

class SquareBoard(cf.Board):
	def get_adjacency_types(self) -> type:
		return StandardAdjacency

