
def print_grid(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:  # Add horizontal separator for 3x3 subgrids
            print("├───────┼───────┼───────┤")
        for j in range(9):
            if j % 3 == 0 and j != 0:  # Add vertical separator for 3x3 subgrids
                print("│", end=" ")
            print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
        print()  # Newline after each row


def is_valid(grid, row, col, num):
    # Check row
    if num in grid[row]:
        return False
    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False
    # Check 3x3 subgrid
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


def is_initial_grid_valid(grid):
    for row in range(9):
        for col in range(9):
            num = grid[row][col]
            if num != 0:
                grid[row][col] = 0
                if not is_valid(grid, row, col, num):
                    print(f"Invalid number {num} at position ({row+1}, {col+1})")
                    return False
                grid[row][col] = num

    return True


def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0  # Backtrack

                return False

    return True


def main():
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Input Sudoku:")
    print_grid(sudoku_grid)

    if not is_initial_grid_valid(sudoku_grid):
        print("\nThis Sudoku puzzle is invalid. Please check the initial values.")
        return

    if solve_sudoku(sudoku_grid):
        print("\nSolved Sudoku:")
        print_grid(sudoku_grid)
    else:
        print("\nNo solution exists for this Sudoku puzzle.")


if __name__ == "__main__":
    main()
