import 'package:starsolver_flutter/logic.dart';

// Ignore the "Don't invoke 'print' in production code." lint.
// ignore_for_file: avoid_print

void main() {
  Board board = Board(shapes: testShapes);

  print(board);
}
