# Board library

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import matplotlib.pyplot as plt
import numpy as np


class Board:
    dimension: int = 9  # Number of cells on a side of the Board.

    n: int = dimension  # Alias for dimension.
    s: int = 2  # The number of stars in each row, column and shape once solved.

    def __init__(self, shapes: list[dict[str, list[Coordinate] | int]] = None, probabilistic: bool = False):
        """A 9x9 board in which a puzzle takes place."""
        self.is_probabilistic: bool = probabilistic

        """A list of all the Rows in the Board."""
        self.rows: list[Row] = [Row(index) for index in range(self.dimension)] if not probabilistic else [
            Row.probabilistic(index) for index in range(self.dimension)]

        """A list of all the Columns in the Board."""
        self.columns: list[Column] = [Column(index) for index in range(self.dimension)] if not probabilistic else [
            Column.probabilistic(index) for index in range(self.dimension)]

        """A list of all the Cells in the Board."""
        self.cells: list[Cell | ProbabilisticCell] = [cell for row in self.rows for cell in row.cells]

        """A list of all the Shapes in the Board."""
        self.shapes: list[Shape] = self.build_shapes(shapes)

    @classmethod
    def probabilistic(cls):
        return Board(probabilistic=True)
        # TODO delete NotImplementedError
        # raise NotImplementedError('Board.probabilistic() constructor is not yet implemented.')

    def __getitem__(self, index: int) -> Row:
        return self.rows[index]

    @staticmethod
    def build_shapes(shapes: list[dict[str, list[Coordinate] | int]]):
        if shapes is None:
            return []
        else:
            return [Shape(index, shape_dict['coords'], shape_dict['colour'])
                    for (index, shape_dict) in enumerate(shapes)]

    def cell_from_coord(self, coord: Coordinate) -> Cell:
        return [cell for cell in self.cells if (cell.coord == coord)][0]

    def dot(self, coord: Coordinate) -> None:
        """Adds a dot in a given coordinate."""
        self[coord.y][coord.x].dot()

    @property
    def is_complete(self) -> bool:
        """Gets whether the Board has been completed and is valid."""
        raise NotImplementedError

    @property
    def is_valid(self) -> bool:
        """Gets whether the Board is valid."""
        raise NotImplementedError

    @property
    def num_blanks(self) -> int:
        """Gets how many blank cells are in the Board."""
        blank_cells: list[Cell] = [cell for cell in self.cells if cell.status == CellStatus.blank]
        return len(blank_cells)

    @property
    def num_dots(self) -> int:
        """Gets how many dotted cells are in the Board."""
        dotted_cells: list[Cell] = [cell for cell in self.cells if cell.status == CellStatus.dot]
        return len(dotted_cells)

    @property
    def num_stars(self) -> int:
        """Gets how many stars are in the Board."""
        starred_cells: list[Cell] = [cell for cell in self.cells if cell.status == CellStatus.star]
        return len(starred_cells)

    def plot_probability_surface(self) -> None:
        """Plots a 3D surface showing the probability that each cell in the board is a star."""
        if not self.is_probabilistic:
            raise AttributeError('plot_probability_surface() is not supported for a non-probabilistic Board.')

        fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

        # Make data.
        x = y = np.array(range(1, self.dimension + 1))  # Horizontal limits are set by the board dimension.
        x, y = np.meshgrid(x, y)

        z: np.ndarray = np.full((self.dimension, self.dimension), 0.0)

        for cell in self.cells:
            probability: float = cell.probability
            z[cell.coord.x, cell.coord.y] = probability

        # ## FIXME remove - testing only
        # # Star some cells
        # for coord in [(8, 6), (3, 2), (5, 7)]:
        #     self.star(Coordinate.from_tuple(coord))

        top = z
        bottom = np.zeros_like(top)

        # surf =
        ax.bar3d(x.ravel(), y.ravel(), bottom.ravel(), 1, 1,
                 np.array([cell.p_star for cell in self.cells]).ravel(),
                 color=[p_cell.colour for p_cell in self.cells],
                 shade=True,
                 cmap=plt.colormaps['coolwarm'])

        ax.set_title('Probability field')
        ax.set_xlabel('x coordinate')
        ax.set_ylabel('y coordinate')
        ax.set_zlabel('P(star)')

        # Customize the z axis.
        ax.set_zlim(0, 1)  # Set Z-axis limits to min and max for a probability.
        # A StrMethodFormatter is used automatically
        ax.zaxis.set_major_formatter('{x:.02f}')

        # # Add a color bar which maps values to colors.
        # fig.colorbar(surf, shrink=0.5, aspect=5)

        plt.show()

    def star(self, coord: Coordinate, dot_adjacents: bool = True) -> None:
        """Adds a star in a given coordinate. Optionally dots adjacent cells."""
        self[coord.y][coord.x].star(dot_adjacents, self)


class Column:
    def __init__(self, index: int):
        self.index: int = index

        self.cells: list[Cell] = [Cell((self.index, vert_index))
                                  for vert_index in range(Board.n)]

    @classmethod
    def probabilistic(cls, index: int):
        column: Column = Column(index)
        p_cells: list[ProbabilisticCell] = [ProbabilisticCell(Coordinate(index, vert_index)) for vert_index in
                                            range(Board.n)]
        column.cells = p_cells
        return column

    def __getitem__(self, index: int) -> Cell:
        return self.cells[index]

    def __repr__(self):
        return f'Column({self.index})'


class Row:
    def __init__(self, index: int, probabilistic: bool = False):
        self.index: int = index

        self.is_probabilistic: bool = probabilistic

        self.cells: list[Cell | ProbabilisticCell] = [Cell((horiz_index, self.index)) for horiz_index in
                                                      range(Board.n)] if not probabilistic else [
            ProbabilisticCell(Coordinate(horiz_index, self.index)) for horiz_index in
            range(Board.n)]

    @classmethod
    def probabilistic(cls, index: int):
        row: Row = Row(index, probabilistic=True)
        p_cells: list[ProbabilisticCell] = [ProbabilisticCell(Coordinate(horiz_index, index)) for horiz_index in
                                            range(Board.n)]
        row.cells = p_cells
        return row

    def __getitem__(self, index: int) -> Cell:
        return self.cells[index]

    def __repr__(self):
        return f'Row({self.index})'


class Shape:
    def __init__(self, index: int, cell_coords: list[Coordinate], colour: int):
        """A single coloured shape within a Board, that contains several c.Cells."""
        self.index: int = index
        # self.cells: list[c.Cell] = [default_board.cell_from_coord(coord) for coord in cell_coords]  # FIXME
        self.colour: int = colour

    @property
    def is_special(self) -> bool:
        raise NotImplementedError


@dataclass
class Coordinate:
    """A Cell coordinate."""
    x: int
    y: int

    @property
    def is_within_board(self) -> bool:
        """Returns whether the Coordinate is within the Board, so is valid."""

        def component_within_board(x_or_y: int) -> bool:
            if (x_or_y >= Board.dimension) or (x_or_y < 0):
                return False
            else:
                return True

        if component_within_board(self.x) and component_within_board(self.y):
            return True
        else:
            return False

    @classmethod
    def from_tuple(cls, coords: tuple) -> Coordinate:
        return Coordinate(coords[0], coords[1])

    def __repr__(self):
        return f'({self.x}, {self.y})'

    @property
    def tuple(self) -> tuple:
        return self.x, self.y


class CellStatus(Enum):
    """The three possible statuses for a Cell."""
    blank = 0
    dot = 1
    star = 2


class Cell:
    def __init__(self, coord: tuple, status: CellStatus = CellStatus.blank, p_star: float | None = None):
        """A single cell in a board."""
        self.coord: Coordinate = Coordinate(coord[0], coord[1])
        self.row_index: int = self.coord.x
        self.column_index: int = self.coord.y

        self.status: CellStatus = status

        self.p_star: float | None = p_star

    @classmethod
    def probabilistic(cls, coord: tuple, probability: float, status: CellStatus = CellStatus.blank) -> Cell:
        return Cell(coord, status, probability)

    def __repr__(self) -> str:
        return f'Cell{self.coord}'

    def adjacents(self, board: Board) -> list[Cell]:
        adjacents_coords: list[Coordinate] = self.adjacent_coords

        cells: list[Cell] = [board[coord.y][coord.x] for coord in adjacents_coords]
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

    @property
    def colour(self) -> tuple:
        """
        Gets the RGB colour of the cell, depending on its p_star.

        `p_star = 1` gives pure green, `p_star = 0` gives pure red, and any other values are a linear interpolation between those two.
        """
        return (1 - self.p_star, self.p_star, 0) if self.p_star is not None else (0.5, 0.5, 0.5)

    def dot(self):
        self.status = CellStatus.dot
        self.p_star = 0

    def dot_adjacents(self, board: Board):
        """Dot all the Cells adjacent to this Cell."""
        for cell in self.adjacents(board):
            cell.dot()

    def star(self, dot_adjacents: bool = True, board: Board = None):
        self.status = CellStatus.star
        self.p_star = 1

        if dot_adjacents:
            if board is None:
                raise ValueError('If dot_adjacents is True (default), board must not be None.')
            self.dot_adjacents(board)


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

# # TODO merge ProbabilisticBoard into Board
# class ProbabilisticBoard(Board):
#     def __init__(self):
#         """A Board where each cell is a ProbabilisticCell that has an assigned probability of being a star."""
#         super().__init__()
#
#         # FIXME add a ProbabilisticFilling class that gives each cell in a filling a p_star.
#         starting_cell_probability: float = self.s / self.n
#
#         p_cells: list[ProbabilisticCell] = []
#         for index, cell in enumerate(self.cells):
#             probabilistic_cell: ProbabilisticCell = ProbabilisticCell(cell.coord,
#                                                                       starting_cell_probability)
#             p_cells.append(probabilistic_cell)
#
#         self.cells: list[ProbabilisticCell] = p_cells
