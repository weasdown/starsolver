# Board library

from __future__ import annotations

import cell as c
import cell_group as cg
import shape as s


class Board:
    dimension: int = 9  # Number of cells on a side of the Board.

    n: int = dimension  # Alias for dimension.
    s: int = 2  # The number of stars in each row, column and shape once solved.

    def __init__(self, shapes: list[dict[str, list[c.Coordinate] | int]] = None):
        """A 9x9 board in which a puzzle takes place."""
        self.rows: list[Row] = [Row(index) for index in range(self.dimension)]
        self.columns: list[Column] = [Column(index) for index in range(self.dimension)]

        """A list of all the Rows in the Board."""
        self.rows: list[cg.Row] = [cg.Row(index) for index in range(Board.dimension)]

        """A list of all the Columns in the Board."""
        self.columns: list[cg.Column] = [cg.Column(index) for index in range(Board.dimension)]

        """A list of all the Cells in the Board."""
        self.cells: list[c.Cell] = [cell for row in self.rows for cell in row.cells]

        """A list of all the Shapes in the Board."""
        self.shapes: list[s.Shape] = self.build_shapes(shapes)

    @classmethod
    def probabilistic(cls):
        raise NotImplementedError('Board.probabilistic() constructor is not yet implemented.')

    def __getitem__(self, index: int):
        return self.rows[index]

    @staticmethod
    def build_shapes(shapes: list[dict[str, list[c.Coordinate] | int]]):
        if shapes is None:
            return []
        else:
            return [s.Shape(index, shape_dict['coords'], shape_dict['colour'])
                    for (index, shape_dict) in enumerate(shapes)]

    def cell_from_coord(self, coord: c.Coordinate) -> c.Cell:
        return [cell for cell in self.cells if (cell.coord == coord)][0]

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
        blank_cells: list[c.Cell] = [cell for cell in self.cells if cell.status == c.CellStatus.blank]
        return len(blank_cells)

    @property
    def num_dots(self) -> int:
        """Gets how many dotted cells are in the Board."""
        dotted_cells: list[c.Cell] = [cell for cell in self.cells if cell.status == c.CellStatus.dot]
        return len(dotted_cells)

    @property
    def num_stars(self) -> int:
        """Gets how many stars are in the Board."""
        starred_cells: list[c.Cell] = [cell for cell in self.cells if cell.status == c.CellStatus.star]
        return len(starred_cells)


class Column:
    def __init__(self, index: int):
        self.index: int = index

        self.cells: list[c.Cell] = [c.Cell(c.Coordinate(self.index, vert_index))
                                    for vert_index in range(Board.n)]

    @classmethod
    def probabilistic(cls, index: int):
        column: Column = Column(index)
        p_cells: list[ProbabilisticCell] = [ProbabilisticCell(c.Coordinate(index, vert_index)) for vert_index in
                                            range(Board.n)]
        column.cells = p_cells
        return column

    def __getitem__(self, index: int) -> c.Cell:
        return self.cells[index]

    def __repr__(self):
        return f'Column({self.index})'


class Row:
    def __init__(self, index: int):
        self.index: int = index

        self.cells: list[c.Cell] = [c.Cell(c.Coordinate(horiz_index, self.index)) for horiz_index in
                                    range(Board.n)]

    @classmethod
    def probabilistic(cls, index: int):
        row: Row = Row(index)
        p_cells: list[ProbabilisticCell] = [ProbabilisticCell(c.Coordinate(horiz_index, index)) for horiz_index in
                                            range(Board.n)]
        row.cells = p_cells
        return row

    def __getitem__(self, index: int) -> c.Cell:
        return self.cells[index]

    def __repr__(self):
        return f'Row({self.index})'
