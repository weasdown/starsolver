# Star Solver Plan
This document lists various methods and attributes that will be needed for the Star Solver classes.

## Needed methods:
### Cell
#### Methods
- Set dot
- Set star
- Set adjacent to dotted

- `is_dotted() -> bool`
- `is_star() -> bool` **Note:** this has a similar effect to Status attribute - both needed?

#### Attributes
- Status (`CellStatus` enum)

### CellHolder
Interface class for some Row, Column and Shape methods.

#### Methods
- Get cell groups (`list[CellGroup]`)

### Row/Column
Note that Row and Column will be separate classes as they will handle coordinates differently (one going horizontally, the other vertically).
- TBC

### CellGroup
A class representing a selection of cells that can hold some number of stars. This could be a whole Row/Column/Shape, or some subset of one of those.

#### Methods
- TBC

#### Attributes
- number_of_cells (`int > 0`)
- number_of_stars (`0 ≤ int ≤ 2`)

### Column
- TBC

### Shape
- TBC

#### Methods
- `update_cell_groups() -> list[CellGroup]`
- `update_special() -> bool` (also updates `Shape.is_special`)

#### Attributes
- is_special (`bool`)
- stars_placed (`0 ≤ int ≤ 2`)
- star_capacity_remaining (`0 ≤ int ≤ 2`)


### Board
#### Methods
- Is complete (`bool`)
- Is valid so far (`bool`)

#### Attributes
- Shapes (`list[Shape]`)

## Program flow
The flow of a solve attempt starts with initial setup of the various board classes. The program then loops through a series of methods to attempt to solve the puzzle.

### Setup
1. Generate list of shapes, including assigning all cells to correct Shape, Row and Column.
2. Check for special shapes and set is_special attribute in Shape if special.
3. TBC

### Methods loop
- As the program runs through the methods loop, it may jump to other methods as appropriate, e.g. if it stars a cell it will run the method to dot adjacent cells. This may be implemented as a method stack that gets updated as the program runs (**TBC**).
- If the program completes the loop without progress, it **must** declare "Puzzle cannot be solved with current algorithms" or similar to avoid an infinite loop.