
def sudokuGame():
    # A simple Sudoku puzzle, where 0 means an empty cell.
    # A list of lists that hold the integers of the game
    grid = [
            [0, 5, 0, 0, 9, 2, 1, 4, 0],
            [0, 0, 4, 6, 0, 0, 0, 2, 0],
            [0, 7, 0, 5, 1, 4, 0, 0, 0],
            [4, 0, 0, 3, 2, 7, 0, 0, 5],
            [8, 0, 5, 0, 0, 1, 2, 7, 0],
            [0, 0, 2, 0, 8, 5, 0, 1, 0],
            [0, 4, 0, 0, 7, 0, 0, 5, 0],
            [5, 8, 9, 2, 0, 3, 0, 6, 0],
            [0, 2, 7, 0, 5, 0, 4, 0, 0]
    ]

    while not isGridFinished(grid):
        printGrid(grid)

        # Get user input
        try:
            row = int(input("Enter row (1-9): ")) - 1 # Minus 1 because python starts at 0
            col = int(input("Enter column (1-9): ")) - 1
            num = int(input("Enter number (1-9): "))

            # Validate input (keep the number within a desired range)
            if row < 0 or row > 8 or col < 0 or col > 8 or num < 1 or num > 9:
                print("Invalid input. Please enter numbers within the correct range.")
                continue

            # Check if the move is valid
            if grid[row][col] != 0: # if the cell is not equal (!=) to 0 then it is filled
                print("This cell is already filled.")
                continue

            if isValid(grid, row, col, num):
                grid[row][col] = num
            else:
                print("Invalid move. Please try again.")

        except ValueError:
            print("Invalid input. Please enter valid integers.")

    # When the grid is full the game is finished
    print("Congratulations! You've completed the Sudoku! Thanks for playing!")
    printGrid(grid)


# Function to make the grid ('|' dividers and '-' separators)
def printGrid(grid):
    for row in range(9):
        # Print the row with vertical dividers for subgrids
        for col in range(9):
            # Print a separator after every 3 columns
            if col % 3 == 0 and col != 0:
                print("|", end=" ")

            # Print the number 0 for empty cells
            print(grid[row][col] if grid[row][col] != 0 else "0", end=" ")

        # Add a line break after every 3 rows
        print()
        if (row + 1) % 3 == 0 and row != 8:
            print("-" * 21)  # Creates a horizontal line between the 9x9 grid


# Function to validate if the cell is taken or not
def isValid(grid, row, col, num):
    # Check if num is already in the row that is selected
    if num in grid[row]:
        print(f"Number {num} already exists in the row {row + 1}.") # adding 1 seen as python starts at 0
        return False

    # Check if num is already in the column that is selected
    for i in range(9):
        if grid[i][col] == num:
            print(f"Number {num} already exists in column {col + 1}.")
            return False
    return True


# Function that loops until all 0s are gone
def isGridFinished(grid):
    for row in grid:
        for num in row:
            if num == 0:
                return False
    return True # This loops until the game is finished, then it returns 'True' when no 0s are present

# Start the game
if __name__ == "__main__":
    sudokuGame()




