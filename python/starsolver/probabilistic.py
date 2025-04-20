# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.ticker import LinearLocator
# from mpl_toolkits.mplot3d import Axes3D
#
#
# ## TODO remove ProbabilisticBoard
# # class ProbabilisticBoard(Board):
# #     def __init__(self):
# #         """A Board where each cell is a ProbabilisticCell that has an assigned probability of being a star."""
# #         super().__init__()
# #
# #         # FIXME add a ProbabilisticFilling class that gives each cell in a filling a p_star.
# #         starting_cell_probability: float = self.s / self.n
# #
# #         p_cells: list[ProbabilisticCell] = []
# #         for index, cell in enumerate(self.cells):
# #             probabilistic_cell: ProbabilisticCell = ProbabilisticCell(cell.coord,
# #                                                                       starting_cell_probability)
# #             p_cells.append(probabilistic_cell)
# #
# #         self.cells: list[ProbabilisticCell] = p_cells
#
#
# # FIXME remove _matplotlib_template() once useful parts copied into plot_probability_surface()
# def matplotlib_template():
#     fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
#     ax: Axes3D
#
#     # Make data.
#     X = np.arange(-5, 5, 0.25)
#     Y = np.arange(-5, 5, 0.25)
#     X, Y = np.meshgrid(X, Y)
#     R = np.sqrt(X ** 2 + Y ** 2)
#     Z = np.sin(R)
#
#     # Plot the surface.
#     surf = ax.plot_surface(X, Y, Z,
#                            # cmap=plt.colormaps['coolwarm'],
#                            linewidth=0, antialiased=False)
#
#     # Customize the z axis.
#     ax.set_zlim(-1.01, 1.01)
#     ax.zaxis.set_major_locator(LinearLocator(10))
#     # A StrMethodFormatter is used automatically
#     ax.zaxis.set_major_formatter('{x:.02f}')
#
#     # Add a color bar which maps values to colors.
#     fig.colorbar(surf, shrink=0.5, aspect=5)
#
#     # plt.show()
