// import 'package:color/color.dart' as c;
import 'package:flutter/material.dart';

import 'cell.dart';
import 'board.dart';

/// One of the nine shapes within a [Board], that contains several [Cell]s.
class Shape {
  final int index;
  final List<Coordinate> cellCoords;
  final Color colour;

  // TODO convert cells to getter that pulls from Board
  // late final List<Cell> cells;

  Shape({required this.index, required this.cellCoords, required this.colour});

  /// Gets whether the [Shape] is a special shape, where a star or dot can be instantly located.
  bool get isSpecial =>
      throw UnimplementedError('Shape.isSpecial is not yet implemented.');
}

/// Gets a list of nine [Color]s for use in [Shape]s.
///
/// The [Color]s are spaced regularly around the colour wheel to have good
/// contrast against each other.
List<Color> get shapeColours {
  // throw UnimplementedError('shapeColours is not yet implemented.');

  Color grey = Colors.grey;

  return List<Color>.generate(Board.dimension, (_) => grey);

  // double startH = 0;
  // double startS = 0;
  // double startL = 0;
  //
  // // Step round the hue circle by 40 degrees per colour, to get 9 regularly spaced colours.
  // final int delta = 40;
  //
  // List<c.Color> hslColors = List<c.Color>.generate(
  //   9,
  //   (int index) => c.Color.hsl(
  //     startH + index * delta,
  //     startS,
  //     startL,
  //   ),
  // );
  //
  // return List<Color>.from(
  //   hslColors.map(
  //       // FIXME fix colour output
  //       (c.Color hsl) => Color.from(alpha: 255, red: 0, green: 0, blue: 255)),
  // );
  //
  // // TODO remove dead colour code
  // // return List.generate(9, (int index) => const Color(0xFF42A5F5)
  // //     // Color.hsl(startH + index * delta, startS, startL)
  // //     //     Color.from(
  // //     //   alpha: 0,
  // //     //   red: 0,
  // //     //   green: 0,
  // //     //   blue: 255,
  // //     // ),
  // //     );
}

/// Defines a list of standard colours to be used for Shapes.
List<Color> standardColours = [
  Colors.blue[50]!,
  Colors.purple[100]!,
  Colors.blue[200]!,
  Colors.orange[50]!,
];

/// Gets a list of nine empty [Shape]s.
List<Shape> get testShapes {
  List<Shape> shapes = [
    Shape(
      index: 0,
      cellCoords: [
        Coordinate(x: 0, y: 0),
        Coordinate(x: 1, y: 0),
        Coordinate(x: 2, y: 0),
        Coordinate(x: 3, y: 0),
        Coordinate(x: 0, y: 1),
        Coordinate(x: 1, y: 1),
        Coordinate(x: 3, y: 1),
        Coordinate(x: 0, y: 2),
        Coordinate(x: 1, y: 2),
        Coordinate(x: 1, y: 3),
        Coordinate(x: 3, y: 3),
        Coordinate(x: 1, y: 4),
        Coordinate(x: 2, y: 4),
        Coordinate(x: 3, y: 4),
        Coordinate(x: 1, y: 5),
        Coordinate(x: 2, y: 5),
      ],
      colour: standardColours[0],
    ),
    Shape(
      index: 1,
      cellCoords: [
        Coordinate(x: 4, y: 0),
        Coordinate(x: 5, y: 0),
        Coordinate(x: 4, y: 1),
        Coordinate(x: 5, y: 1),
        Coordinate(x: 6, y: 1),
        Coordinate(x: 7, y: 1),
        Coordinate(x: 5, y: 2),
        Coordinate(x: 6, y: 2),
        Coordinate(x: 7, y: 2),
        Coordinate(x: 5, y: 3),
        Coordinate(x: 6, y: 3),
        Coordinate(x: 6, y: 4),
      ],
      colour: standardColours[1],
    ),
    Shape(
      index: 2,
      cellCoords: [
        Coordinate(x: 6, y: 0),
        Coordinate(x: 7, y: 0),
        Coordinate(x: 8, y: 0),
      ],
      colour: standardColours[2],
    ),
    Shape(
      index: 3,
      cellCoords: [
        Coordinate(x: 2, y: 1),
        Coordinate(x: 2, y: 2),
        Coordinate(x: 2, y: 3),
        Coordinate(x: 3, y: 2),
      ],
      colour: standardColours[2],
    ),
    Shape(
      index: 4,
      cellCoords: [
        Coordinate(x: 4, y: 2),
        Coordinate(x: 4, y: 3),
        Coordinate(x: 4, y: 4),
      ],
      colour: standardColours[3],
    ),
    Shape(
        index: 5,
        cellCoords: [
          Coordinate(x: 6, y: 8),
          Coordinate(x: 7, y: 3),
          Coordinate(x: 7, y: 4),
          Coordinate(x: 7, y: 5),
          Coordinate(x: 7, y: 6),
          Coordinate(x: 7, y: 7),
          Coordinate(x: 7, y: 8),
          Coordinate(x: 8, y: 1),
          Coordinate(x: 8, y: 2),
          Coordinate(x: 8, y: 3),
          Coordinate(x: 8, y: 4),
          Coordinate(x: 8, y: 5),
          Coordinate(x: 8, y: 6),
          Coordinate(x: 8, y: 7),
          Coordinate(x: 8, y: 8),
        ],
        colour: standardColours[0]),
    Shape(
      index: 6,
      cellCoords: [
        Coordinate(x: 0, y: 3),
        Coordinate(x: 0, y: 4),
        Coordinate(x: 0, y: 5),
        Coordinate(x: 0, y: 6),
        Coordinate(x: 0, y: 7),
        Coordinate(x: 0, y: 8),
        Coordinate(x: 1, y: 6),
        Coordinate(x: 1, y: 7),
        Coordinate(x: 1, y: 8),
        Coordinate(x: 2, y: 6),
        Coordinate(x: 2, y: 7),
        Coordinate(x: 2, y: 8),
        Coordinate(x: 3, y: 7),
      ],
      colour: standardColours[1],
    ),
    Shape(
      index: 7,
      cellCoords: [
        Coordinate(x: 3, y: 5),
        Coordinate(x: 3, y: 6),
        Coordinate(x: 4, y: 5),
        Coordinate(x: 4, y: 6),
        Coordinate(x: 4, y: 7),
        Coordinate(x: 5, y: 4),
        Coordinate(x: 5, y: 5),
        Coordinate(x: 5, y: 6),
        Coordinate(x: 5, y: 7),
        Coordinate(x: 6, y: 5),
        Coordinate(x: 6, y: 6),
        Coordinate(x: 6, y: 7),
      ],
      colour: standardColours[2],
    ),
    Shape(
      index: 8,
      cellCoords: [
        Coordinate(x: 3, y: 8),
        Coordinate(x: 4, y: 8),
        Coordinate(x: 5, y: 8),
      ],
      colour: standardColours[3],
    ),
  ];

  return shapes;
}
