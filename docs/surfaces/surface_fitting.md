# Surface Fitting

This document examines how we can find the equation of a surface that fits a board.

We want to find a two-valued function `f(x,y)` that takes the `(x,y)` coordinate of a cell (indexed starting at 0) and 
gives the cell's value. The output of this function is `0` if the cell is dotted, `1` if it is starred, and undefined otherwise.

Throughout this document, we will use the image below as reference, taken from puzzle Easy #1 in the _Star Battle_ app.


<img width="300" height="300" alt="Completed board" src="https://github.com/user-attachments/assets/87cfd176-1d9d-44f9-a7b4-92833f117af8" />

_Easy #1_

## Method

### 1. Board row as a spectrum analyser plot
We can define the equation of a row `y` in the board by treating the cell values in that row as if they are peaks on a 
spectrum analyser display. In particular, let's assume that each cell represents a doubling in frequency, starting at 1 Hz. 
The formula for the frequency `F` of a cell `x` in a row is therefore:

<code>F(x) = 2<sup>x</sup></code>

This means the cell at index 0 (the leftmost cell) has a frequency of 1 Hz and the cell at index 8 (the rightmost cell) 
has a frequency of 256 Hz.

By looking at where the stars are in the row, we can determine the _frequency components_ for that row. 
For example, the first row in the reference image has one frequency component at index 2, so 4 Hz, and one component at 
index 4, so 16 Hz.


### 2. Extending to multiple rows
Now that we can find the equation for any single row, we wish to extend this to get the equation of a whole board.

Let us assign each row a unique binary value based on its index (with the index starting at 0). This value will then be 
used as a coefficient to be applied to each of the row's frequency components. The value `v` for a row with index `r` is therefore:

<code>v(r) = 2<sup>r</sup></code>

By reading down the columns of a board, we can therefore get a total value for each of the board's frequency components. 
For example, reading down the second column in the reference image (the column with a frequency of 2 Hz), we can see 
that there are stars at <code>r<sub>1</sub> = 3</code> and <code>r<sub>2</sub> = 5</code>. These give values of 
<code>v<sub>1</sub> = 2<sup>3</sup> = 8</code> and <code>v<sub>1</sub> = 2<sup>5</sup> = 32</code>. For the 2 Hz column, 
we therefore have a total value of 40. We can repeat this process for the other columns. For the reference image, this produces values as follows:

| Frequency (Hz) | Value          |
|----------------|----------------|
| 1              | 2 + 128 = 130  |
| 2              | 8 + 32 = 40    |
| 4              | 1 + 256 = 257  |
| 8              | 16 + 64 = 80   |
| 16             | 1 + 4 = 5      |
| 32             | 32 + 128 = 160 |
| 64             | 2 + 8 = 10     |
| 128            | 64 + 256 = 320 |
| 256            | 4 + 16 = 20    |

### 3. Board frequency fingerprint
The fact that we chose binary values for the rows means that each total value for a frequency component uniquely identifies the indices of the starred rows. 
For example, a value of 160 can only be made by having a star in the 32 row (index 5) and a star in the 128 row (index 7).

Finally, using these values as coefficients for the frequency components give us a **unique** _frequency fingerprint_ for the board. 
For example for the reference board,

`f = 130 x 1 Hz + 40 x 2 Hz + 257 x 4 Hz + 80 x 8 Hz + 5 x 16 Hz + 160 * 32 Hz + 10 * 64 Hz + 320 x 128 Hz + 640 x 256 Hz`

`= 130 sin(t) + 40 sin(2t) + 257 sin(4t) + 80 sin(8t) + 5 sin(16t) + 160 sin(32t) + 10 sin(64t) + 320 sin(128t) + 640 sin(256t)`

where `t` is a value that all the frequency components can be scaled by to get higher frequencies (`t` is 1 by default).