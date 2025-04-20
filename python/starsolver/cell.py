# Cell library

from __future__ import annotations

# from dataclasses import dataclass
from enum import Enum

from .board import Board, Cell, Coordinate


class CellStatus(Enum):
    """The three possible statuses for a Cell."""
    blank = 0
    dot = 1
    star = 2


class ProbabilisticCell(Cell):
    default_probability: float = Board.s / Board.n

    def __init__(self, coord: Coordinate, p_star: float = default_probability) -> None:
        """A Cell with an assigned probability of being a star."""
        assert (p_star <= 1) and (p_star >= 0)

        super().__init__(coord.tuple)

        self.p_star: float = p_star
        self.p_dot: float = 1 - p_star

    def __repr__(self) -> str:
        return f'ProbabilisticCell({self.coord}, {self.p_star})'

    @property
    def data(self) -> tuple:
        """Gets a tuple containing the cell's x coordinate, y coordinate and probability."""
        return self.coord.x, self.coord.y, self.p_star

    @property
    def probability(self) -> float:
        """Gets the probability that this is a star."""
        return self.p_star
