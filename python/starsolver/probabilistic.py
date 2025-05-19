# from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LinearLocator

# import python.starsolver.board as b
import cell as c
# from board import Board
import board as b


# from python.starsolver.cell import Cell, Coordinate


class ProbabilisticBoard(b.Board):
    def __init__(self):
        """A Board where each cell is a ProbabilisticCell that has an assigned probability of being a star."""
        super().__init__()

        # self.rows: list[cg.Row] = [cg.Row(index) for index in range(Board.dimension)]

        # FIXME add a ProbabilisticFilling class that gives each cell in a filling a p_star.
        starting_cell_probability: float = self.s / self.n

        p_cells: list[c.ProbabilisticCell] = []
        for index, cell in enumerate(self.cells):
            probabilistic_cell: c.ProbabilisticCell = c.ProbabilisticCell(cell.coord,
                                                                          starting_cell_probability)
            p_cells.append(probabilistic_cell)

        self.cells: list[c.ProbabilisticCell] = p_cells

    def plot_probability_surface(self) -> None:
        """Plots a 3D surface showing the probability that each cell in the board is a star."""
        _matplotlib_template()  # FIXME remove _matplotlib_template() call

        fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

        # Make data.
        # x, y = np.arange(0, self.dimension, 1)
        # x, y = np.meshgrid(x, y)

        horizontal_axes_limits = range(1, self.dimension + 1)  # Horizontal limits are set by the board dimension.
        x = np.meshgrid(horizontal_axes_limits, horizontal_axes_limits)
        y = x

        # X = np.arange(-5, 5, 0.25)
        # Y = np.arange(-5, 5, 0.25)
        # X, Y = np.meshgrid(X, Y)

        # FIXME fix ProbabilisticBoard.rows, columns attributes so __get_item__() works properly
        z: np.ndarray = self[1][1].probability  # np.ndarray([])

        pass

        for cell in self.cells:
            data: tuple = cell.data
            # np.append(x, data[0])
            # np.append(y, data[1])
            np.append(z, data[2])

        # TODO remove old code
        # R = np.sqrt(X ** 2 + Y ** 2)
        # Z = np.sin(R)

        # Plot the surface.
        surf = ax.plot_surface(x, y, z,
                               # cmap=plt.colormaps['coolwarm'],
                               linewidth=0, antialiased=False)

        # Customize the z axis.
        ax.set_zlim(0, 1)  # Set Z-axis limits to min and max for a probability.
        # A StrMethodFormatter is used automatically
        ax.zaxis.set_major_formatter('{x:.02f}')

        # Add a color bar which maps values to colors.
        fig.colorbar(surf, shrink=0.5, aspect=5)

        plt.show()


# FIXME remove _matplotlib_template() once useful parts copied into plot_probability_surface()
def _matplotlib_template():
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    # Make data.
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=plt.colormaps['coolwarm'],
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    # A StrMethodFormatter is used automatically
    ax.zaxis.set_major_formatter('{x:.02f}')

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    # plt.show()


if __name__ == '__main__':
    p_board: ProbabilisticBoard = ProbabilisticBoard()
    p_board.plot_probability_surface()
