import 'package:flutter/material.dart';

import '../logic/board.dart';
import 'board_widget.dart';

/// An app page that displays a puzzle.
class PuzzlePage extends StatefulWidget {
  final Board board;
  const PuzzlePage({super.key, required this.board});

  static const double spacingAround = 40.0;
  static const double buttonSpacing = 30.0;

  @override
  State<PuzzlePage> createState() => _PuzzlePageState();
}

class _PuzzlePageState extends State<PuzzlePage> {
  void onComplete() {
    showAdaptiveDialog(
        context: context,
        builder: (context) {
          return AlertDialog(
            title: const Text('Complete!'),
            content: const Text('Congratulations, you completed the puzzle!'),
            actions: <Widget>[
              ElevatedButton(
                style: TextButton.styleFrom(
                  textStyle: Theme.of(context).textTheme.labelLarge,
                ),
                child: const Text('Ok'),
                onPressed: () {
                  Navigator.of(context).pop();
                },
              ),
            ],
          );
        });
  }

  @override
  Widget build(BuildContext context) {
    BoardWidget boardWidget = BoardWidget(
      board: widget.board,
      spacingAround: PuzzlePage.spacingAround,
      onComplete: onComplete,
    );

    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text('Star Battle Puzzle'),
      ),
      body: Column(
        children: [
          // Reset button
          Align(
            alignment: Alignment.centerRight,
            child: Padding(
              padding: EdgeInsets.fromLTRB(0, PuzzlePage.buttonSpacing,
                  PuzzlePage.spacingAround, PuzzlePage.buttonSpacing),
              child: ElevatedButton(
                onPressed: () => setState(() {
                  boardWidget.clearAllCells();
                }),
                child: Text('Reset', style: TextStyle(fontSize: 18)),
              ),
            ),
          ),
          boardWidget
        ],
      ),
    );
  }
}
