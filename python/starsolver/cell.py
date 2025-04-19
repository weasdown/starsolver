# Cell library

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import starsolver.board as b


@dataclass
class Coordinate:
    """A Cell coordinate."""
    x: int
    y: int

    @property
    def is_within_board(self) -> bool:
        """Returns whether the Coordinate is within the Board, so is valid."""

        def component_within_board(x_or_y: int) -> bool:
            if (x_or_y >= b.Board.dimension) or (x_or_y < 0):
                return False
            else:
                return True

        if component_within_board(self.x) and component_within_board(self.y):
            return True
        else:
            return False

    def __repr__(self):
        return f'({self.x}, {self.y})'


class CellStatus(Enum):
    """The three possible statuses for a Cell."""
    blank = 0
    dot = 1
    star = 2


class Cell:
    def __init__(self, coord: Coordinate, status: CellStatus = CellStatus.blank):
        """A single cell in a board."""
        self.coord: Coordinate = coord
        self.row_index: int = self.coord.x
        self.column_index: int = self.coord.y

        self.status: CellStatus = status

    def __repr__(self) -> str:
        return f'Cell{self.coord}'

    def adjacents(self, board: b.Board) -> list[Cell]:
        adjacents_coords: list[Coordinate] = self.adjacent_coords

        cells: list[Cell] = list(map(board.cell_from_coord, adjacents_coords))
        return cells

    @property
    def adjacent_coords(self) -> list[Coordinate]:
        all_adjacents = [Coordinate(self.coord.x - 1, self.coord.y + 1),
                         Coordinate(self.coord.x, self.coord.y + 1),
                         Coordinate(self.coord.x + 1, self.coord.y + 1),
                         Coordinate(self.coord.x - 1, self.coord.y),
                         Coordinate(self.coord.x + 1, self.coord.y),
                         Coordinate(self.coord.x - 1, self.coord.y - 1),
                         Coordinate(self.coord.x, self.coord.y - 1),
                         Coordinate(self.coord.x + 1, self.coord.y - 1)]

        filtered_adjacents: list[Coordinate] = [coord for coord in all_adjacents if coord.is_within_board]
        return filtered_adjacents

    def dot(self):
        self.status = CellStatus.dot

    def dot_adjacents(self, board: b.Board):
        """Dot all the Cells adjacent to this Cell."""
        for cell in self.adjacents(board):
            cell.dot()

    def star(self):
        self.status = CellStatus.star
