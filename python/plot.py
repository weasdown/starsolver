from starsolver.board import Board

if __name__ == '__main__':
    p_board: Board = Board.probabilistic()
    p_board.plot_probability_surface()
