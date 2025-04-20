from board import Board
from cell import Cell, Coordinate


class ProbabilisticBoard(Board):
    def __init__(self):
        """A Board where each cell is a ProbabilisticCell that has an assigned probability of being a star."""
        super().__init__()

        # FIXME add a ProbabilisticFilling class that gives each cell in a filling a p_star.
        starting_cell_probability: float = self.s / self.n

        p_cells: list[ProbabilisticCell] = []
        for index, cell in enumerate(self.cells):
            probabilistic_cell: ProbabilisticCell = ProbabilisticCell(cell.coord,
                                                                      starting_cell_probability)
            p_cells.append(probabilistic_cell)

        self.cells: list[ProbabilisticCell] = p_cells


class ProbabilisticCell(Cell):
    def __init__(self, coord: Coordinate, p_star: float) -> None:
        """A Cell with an assigned probability of being a star."""
        assert (p_star <= 1) and (p_star >= 0)

        super().__init__(coord)

        self.p_star: float = p_star
        self.p_dot: float = 1 - p_star

    def __repr__(self) -> str:
        return f'ProbabilisticCell({self.coord}, {self.p_star})'

    @property
    def probability(self) -> float:
        """Gets the probability that this is a star."""
        return self.p_star
