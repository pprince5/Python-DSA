# copy over your a1_partd.py file here
#    Main Author(s): Kiran Dhillon
#    Main Reviewer(s): Kexian Guo, Prince

from a1_partc import Queue

def get_overflow_list(grid):
    rows = len(grid)
    cols = len(grid[0])
    overflow_cells = []

    def count_neighbors(row, col):
        neighbors = 0
        if row > 0:
            neighbors += 1
        if row < rows - 1:
            neighbors += 1
        if col > 0:
            neighbors += 1
        if col < cols - 1:
            neighbors += 1
        return neighbors

    for row in range(rows):
        for col in range(cols):
            cell_value = abs(grid[row][col])
            neighbors = count_neighbors(row, col)
            if cell_value >= neighbors:
                overflow_cells.append((row, col))

    return overflow_cells if overflow_cells else None

def overflow(grid, a_queue):
    overflow_cells = get_overflow_list(grid)
    type_check = True
    for row in grid:
        for val in row:
            type_check = type(val) == int
            if not type_check:
                break
        if not type_check:
            break

    if not type_check:
        raise "Error: grid contains an non-number value"
    else:
        init_sign = None
        all_same_sign = True
        if overflow_cells:
            for row in grid:
                for val in row:
                    if val:
                        is_positive = val > 0
                        if init_sign is None:
                            init_sign = is_positive
                        elif init_sign != is_positive:
                            all_same_sign = False

        if not all_same_sign:
            for row, col in overflow_cells:
                init_sign = grid[row][col] > 0
                grid[row][col] = 0

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for row, col in overflow_cells:
                for dir_row, dir_col in directions:
                    row_to_change = row + dir_row
                    col_to_change = col + dir_col
                    if 0 <= row_to_change < len(grid) and 0 <= col_to_change < len(grid[0]):
                        grid[row_to_change][col_to_change] = abs(grid[row_to_change][col_to_change]) + 1
                        grid[row_to_change][col_to_change] *= 1 if init_sign else -1

            modified_grid = []
            for row in grid:
                modified_grid = [[val for val in row] for row in grid]
            a_queue.enqueue(modified_grid)
            return overflow(grid, a_queue) + 1

        return 0
