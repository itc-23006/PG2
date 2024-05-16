def print_transposed_grid(grid):
    for i in range(len(grid[0])):  # Iterate over the columns
        for j in range(len(grid)):  # Iterate over the rows
            print(grid[j][i], end='')
        print('')  # Move to the next line after printing each column

# Define the grid
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Call the function to print the transposed grid
print_transposed_grid(grid)
