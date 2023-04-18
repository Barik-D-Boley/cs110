import sys
import re

BLOCKED = '*'
EMPTY = '.'
WIN = '!'


def print_grid(grid):
    # print(grid)
    for line in grid:
        print('a'.join(line), end='')


def read_grid(filename):
    with open(filename, 'r') as file:
        grid = []
        for line in file:
            line = line.split(' ')
            grid.append(line)
    return grid


def update_grid(grid, old_row, old_col, new_row, new_col, empty=None):
    grid[old_row][old_col] = '.'
    grid[new_row][new_col] = '@'


def is_blocked(grid, row, col, blocked_value):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])-1 or grid[row][col] == '*':
        return True


def play(grid):
    row = 0
    col = 0
    while True:
        print_grid(grid)
        action = input('Action: ')
        if not action:
            break

        action = action.lower()
        new_row = row
        new_col = col

        if action[0] == 'u':
            if not is_blocked(grid, row - 1, col, blocked_value=BLOCKED):
                new_row = row - 1

        elif action[0] == 'd':
            if not is_blocked(grid, row + 1, col, blocked_value=BLOCKED):
                new_row = row + 1

        elif action[0] == 'l':
            if not is_blocked(grid, row, col - 1, blocked_value=BLOCKED):
                new_col = col - 1

        elif action[0] == 'r':
            if not is_blocked(grid, row, col + 1, blocked_value=BLOCKED):
                new_col = col + 1

        elif action[0] == 'q':
            break

        if row != new_row or col != new_col:
            if grid[new_row][new_col] == WIN:
                update_grid(grid, row, col, new_row, new_col, empty=EMPTY)
                print_grid(grid)
                print('You win!')
                break
            else:
                update_grid(grid, row, col, new_row, new_col, empty=EMPTY)
                row = new_row
                col = new_col


def main(filename):
    grid = read_grid(filename)
    play(grid)


if __name__ == '__main__':
    main(sys.argv[1])
