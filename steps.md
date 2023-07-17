### Steps:

* Make a grid of cell with 4 walls
* Choose a random cell and mark it as visited
* While there are unvisited cells
    * Choose a random visited cell
    * If this cell has unvisited neighbours
        * Choose a random unvisited neighbour
        * Remove the wall between the cell and the neighbour
        * Mark the neighbour as visited
        * Add the neighbour to the list of visited cells
    * Else
        * Remove the cell from the list of visited cells
* Return the grid