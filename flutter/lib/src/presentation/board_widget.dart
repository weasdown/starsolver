import 'package:flutter/material.dart';

import '../logic/board.dart';
import '../logic/cell.dart';
import 'cell_widget.dart';

/// A widget to display a [Board].
class BoardWidget extends StatelessWidget {
  final Board board;
  final double spacingAround;

  final void Function() onComplete;

  const BoardWidget({
    super.key,
    required this.board,
    required this.spacingAround,
    required this.onComplete,
  });

  /// All the [CellWidget]s for this [BoardWidget].
  List<CellWidget> get cellWidgets => List<CellWidget>.from(
        board.cells.map((Cell cell) => CellWidget(
              cell: cell,
              board: board,
              onComplete: onComplete,
            )),
      );

  /// Amount of spacing between [CellWidget]s.
  final double spacingWithin = 0;

  /// Set all [cells] to blank.
  ///
  /// Sets the [Cell.status] of all [cells] to [CellStatus.blank].
  void clearAllCells() {
    for (Cell cell in board.cells) {
      cell.status = CellStatus.blank;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Flexible(
      child: Padding(
        padding: EdgeInsets.symmetric(horizontal: spacingAround),
        child: GridView.count(
          mainAxisSpacing: spacingWithin,
          crossAxisSpacing: spacingWithin,
          crossAxisCount: Board.dimension,
          children: cellWidgets,
        ),
      ),
    );
  }
}
