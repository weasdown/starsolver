# Star Solver

A Python solver for "Star Battle"/"Two Not Touch" puzzles. Valid only for a 9x9 grid (so 18 stars).

General guidance on the terminology of these puzzles and how to solve them is available on [Jim Bumgardner's 
("Krazy Dad") site](https://krazydad.com/twonottouch/).

## Pseudocode

- When adding star:
    1. Set cell to starred
    2. Check whether grid solved
    3. Set adjacent cells to dotted
    4. Update cell groups for:
        a. shape
        b. row
        c. column
    5. Check whether new groups allow extra star in:
        a. shape
        b. row
        c. column

## Theory
One way I could represent the different rows, columns and shapes of a board is with an [intersection graph](https://en.wikipedia.org/wiki/Intersection_graph), or, perhaps, a more specific [interval graph](https://en.wikipedia.org/wiki/Interval_graph). 
A [contact graph](https://en.wikipedia.org/wiki/Contact_graph) may be more appropriate.
