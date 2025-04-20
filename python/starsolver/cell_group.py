# Classes for general groups of cells.

import board as b
import cell as c


class CelLGroup:
    def __init__(self, cells: list[c.Cell]):
        """The most generic form of cell group."""
        self.cells: list[c.Cell] = cells


class LinearCellGroup(CelLGroup):
    def __init__(self, index: int, cells: list[c.Cell]):
        """A cell group where all the cells are in a line of width one cell."""
        super().__init__(cells)
        self.index: int = index

    def __getitem__(self, index: int) -> c.Cell:
        return self.cells[index]


class Column(LinearCellGroup):
    def __init__(self, index: int):
        super().__init__(index, cells=[])
        self.cells: list[c.Cell] = [c.Cell(c.Coordinate(self.index, vert_index))
                                    for vert_index in range(b.Board.dimension)]

    def __repr__(self):
        return f'Column({self.index})'


class Row(LinearCellGroup):
    def __init__(self, index: int):
        super().__init__(index, [])
        self.cells: list[c.Cell] = [c.Cell(c.Coordinate(horiz_index, self.index)) for horiz_index in
                                    range(b.Board.dimension)]

    def __repr__(self):
        return f'Row({self.index})'
