from byubit import Bit
from Library.bit_commands import *


@Bit.worlds('maze')
def solve_maze(bit):
    bit_paint_and_move(bit, 3, 'green')
    bit.left()
    bit_paint_and_move(bit, 3, 'green')
    bit.right()
    bit_paint_and_move(bit, 4, 'green')
    bit.right()
    bit_paint_and_move(bit, 3, 'green')
    bit.move()


if __name__ == "__main__":
    solve_maze(Bit.new_bit)