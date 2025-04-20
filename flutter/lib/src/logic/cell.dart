import 'package:starsolver_flutter/src/presentation/cell_widget.dart';

import 'board.dart';
import 'shape.dart';

/// An individual cell within a [Board].
class Cell {
  /// The [Coordinate] of the [Cell] in the [Board].
  ///
  /// Note that, to align with computer vision common practices, the origin is
  /// the **top left** [Cell] in the [Board].
  final Coordinate coord;

  /// A [CellStatus] value showing whether the [Cell] is blank, a dot or a star.
  CellStatus status;

  /// The [Shape] that this [Cell] is within.
  late final Shape? shape;

  Cell({required this.coord})
      : _status = CellStatus.blank,
        boundaries = CellBoundarySet(
          start: false,
          top: false,
          end: false,
          bottom: false,
        );

  /// Iterates the [Cell]'s [status] through the possible values of [CellStatus].
  void nextStatus() => status = status.nextStatus;

  /// Whether each edge of the [Cell] is the boundary of a [Shape].
  CellBoundarySet boundaries;

  /// The [Coordinate] of the [Cell] in the [Board].
  ///
  /// Note that, to align with computer vision common practices, the origin is
  /// the **top left** [Cell] in the [Board].
  final Coordinate coord;

  /// Sets the cell's [status] to [CellStatus.dot].
  dot() => _status = CellStatus.dot;

  /// Iterates the [Cell]'s [status] through the possible values of [CellStatus].
  void nextStatus() => _status = status.nextStatus;

  /// The [Shape] that this [Cell] is within.
  late final Shape? shape;

  /// Sets the cell's [status] to [CellStatus.star].
  star() => _status = CellStatus.star;

  /// A private, internal [CellStatus] value showing whether the [Cell] is blank, a dot or a star.
  CellStatus _status;

  /// Gets the cell's [CellStatus] value.
  CellStatus get status => _status;
}

/// Whether each edge of the [Cell] is the boundary of a [Shape].
class CellBoundarySet {
  final bool start;
  final bool top;
  final bool end;
  final bool bottom;

  CellBoundarySet(
      {required this.start,
      required this.top,
      required this.end,
      required this.bottom});

  /// Cell edges in the returned list are in the order `[start, top, end, bottom]`
  /// (to match against `Padding.fromLTRB()`)..
  List<bool> get values => List.unmodifiable([start, top, end, bottom]);
}

/// The three possible statuses for a Cell.
enum CellStatus {
  blank(text: ' ', value: 0),
  dot(text: '•', value: 1),
  star(text: '⭐', value: 2);

  final String text;
  final int value;

  const CellStatus({required this.text, required this.value});

  /// Gets the next value of [CellStatus], so it can be iterated when a
  /// [CellWidget] is tapped.
  CellStatus get nextStatus => CellStatus.values[value < 2 ? value + 1 : 0];
}

/// A [Cell]'s coordinate in the [Board].
class Coordinate {
  final int x;
  final int y;

  Coordinate({required this.x, required this.y});

  @override
  bool operator ==(Object other) {
    if (other is Coordinate && other.x == x && other.y == y) {
      return true;
    } else {
      return false;
    }
  }

  @override
  int get hashCode => Object.hash(x, y);

  ///Returns whether the Coordinate is within the Board, so is valid.
  bool isWithinBoard() {
    bool componentWithinBoard({required int xOrY}) {
      if ((xOrY >= Board.dimension) || (xOrY < 0)) {
        return false;
      } else {
        return true;
      }
    }

    if (componentWithinBoard(xOrY: x) || componentWithinBoard(xOrY: y)) {
      return true;
    } else {
      return false;
    }
  }

  /// Returns a [String] representation of the [Coordinate].
  @override
  String toString() => '($x, $y)';
}
