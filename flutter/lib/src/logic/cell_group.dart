import 'board.dart';
import 'cell.dart';

/// The most generic form of cell group.
class CellGroup {
  List<Cell> cells;

  CellGroup({required this.cells});

  /// Gets the number of stars in the [CellGroup].
  ///
  /// For a complete [Board], each [Row] or [Column] must have exactly 2 stars,
  /// meaning the whole [Board] must have exactly 18 stars.
  int get numStars =>
      cells.where((Cell cell) => cell.status == CellStatus.star).length;
}

/// A cell group where all the cells are in a line of width one cell.
class LinearCellGroup extends CellGroup {
  final int index;

  LinearCellGroup({required this.index, required super.cells});

  Cell operator [](int index) => cells[index];
}

/// A column in a [Board].
class Column extends LinearCellGroup {
  Column({required super.index})
      : super(
          cells: List<Cell>.from(
            List<int>.generate(Board.dimension, (int index) => index).map(
              (int vertIndex) =>
                  Cell(coord: Coordinate(x: index, y: vertIndex)),
            ),
          ),
        );

  /// Constructor to build a [Column] from a list of [Cell]s.
  Column.fromCells({required super.index, required super.cells});
}

/// A row in a [Board].
class Row extends LinearCellGroup {
  /// Basic constructor.
  Row({
    required super.index,
  }) : super(
          cells: List<Cell>.from(
            List<int>.generate(Board.dimension, (int index) => index).map(
              (int horizIndex) =>
                  Cell(coord: Coordinate(x: horizIndex, y: index)),
            ),
          ),
        );

  /// Constructor to build a [Row] from a list of [Cell]s.
  Row.fromCells({required super.index, required super.cells});
}
