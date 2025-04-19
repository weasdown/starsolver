# Shape class

import starsolver.cell as c


class Shape:
    def __init__(self, index: int, cell_coords: list[c.Coordinate], colour: int):
        """A single coloured shape within a Board, that contains several c.Cells."""
        self.index: int = index
        # self.cells: list[c.Cell] = [default_board.cell_from_coord(coord) for coord in cell_coords]  # FIXME
        self.colour: int = colour

    @property
    def is_special(self) -> bool:
        raise NotImplementedError
