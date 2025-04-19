import 'package:flutter/material.dart';

import '../logic/board.dart';
import '../logic/cell.dart';

/// A widget to display a [Cell].
class CellWidget extends StatefulWidget {
  final Cell cell;
  final Board board;

  final void Function() onComplete;

  const CellWidget({
    super.key,
    required this.cell,
    required this.board,
    required this.onComplete,
  });

  @override
  State<CellWidget> createState() => _CellWidgetState();
}

class _CellWidgetState extends State<CellWidget> {
  final double size = 40;

  /// Sets the [widget.cell]'s [Cell.status] to [CellStatus.star].
  setStar() {
    setState(
      () => widget.cell.status = CellStatus.star,
    );

    if (widget.board.isComplete) {
      widget.onComplete();
    }
  }

  /// Sets the [widget.cell]'s [Cell.status] to the next [CellStatus] value,
  /// or [CellStatus.blank] if currently [CellStatus.star].
  setNextStatus() {
    CellStatus next = widget.cell.status.nextStatus;
    if (next == CellStatus.star) {
      setStar();
    } else {
      setState(() => widget.cell.status = next);
    }
  }

  /// Gets a [BorderDirectional] with [BorderSide]s corresponding to whether
  /// that side of the [CellWidget]'s [Cell] is a boundary between [Shape]s.
  BorderDirectional get borders {
    CellBorderSet cellBorders = CellBorderSet.fromCellBoundarySet(
      boundarySet: widget.cell.boundaries,
      boundaryBorderWidth: 3.0,
      nonBoundaryBorderWidth: 0.0,
    );

    return BorderDirectional(
      start: cellBorders.start,
      top: cellBorders.top,
      end: cellBorders.end,
      bottom: cellBorders.bottom,
    );
  }

  BorderSide borderForEdge(bool edge) {
    return BorderSide();
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: setNextStatus,
      onLongPress: setStar,
      child: Container(
        height: size,
        width: size,
        // TODO set borders per side based on Shape boundaries (including width)
        foregroundDecoration: BoxDecoration(border: borders),
        color: widget.cell.shape!.colour,
        child: Center(
          child: Text(
            widget.cell.status.text,
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 32),
          ),
        ),
      ),
    );
  }
}

/// Widget equivalent of [CellBoundarySet].
class CellBorderSet {
  late final BorderSide start;
  late final BorderSide top;
  late final BorderSide end;
  late final BorderSide bottom;

  final double boundaryBorderWidth;
  final double nonBoundaryBorderWidth;

  CellBorderSet.fromCellBoundarySet({
    required CellBoundarySet boundarySet,
    required this.boundaryBorderWidth,
    required this.nonBoundaryBorderWidth,
  }) {
    start = _borderSideFromBool(boundarySet.start);
    top = _borderSideFromBool(boundarySet.top);
    end = _borderSideFromBool(boundarySet.end);
    bottom = _borderSideFromBool(boundarySet.bottom);
  }

  List<BorderSide> get values => [start, top, end, bottom];

  BorderSide _borderSideFromBool(bool isBoundary) => BorderSide(
      width: isBoundary ? boundaryBorderWidth : nonBoundaryBorderWidth);
}
