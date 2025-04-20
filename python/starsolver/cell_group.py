# Classes for general groups of cells.

from board import Board, Cell, Coordinate


class CelLGroup:
    def __init__(self, cells: list[Cell]):
        """The most generic form of cell group."""
        self.cells: list[Cell] = cells


class LinearCellGroup(CelLGroup):
    def __init__(self, index: int, cells: list[Cell]):
        """A cell group where all the cells are in a line of width one cell."""
        super().__init__(cells)
        self.index: int = index

    def __getitem__(self, index: int) -> Cell:
        return self.cells[index]

# class Column(LinearCellGroup):
#     def __init__(self, index: int):
#         super().__init__(index, cells=[])
#         self.cells: list[Cell] = [Cell((self.index, vert_index))
#                                   for vert_index in range(Board.dimension)]
#
#     def __repr__(self):
#         return f'Column({self.index})'
#
#
# class Row(LinearCellGroup):
#     def __init__(self, index: int):
#         super().__init__(index, [])
#         self.cells: list[Cell] = [Cell((horiz_index, self.index)) for horiz_index in
#                                   range(Board.dimension)]
#
#     def __repr__(self):
#         return f'Row({self.index})'
