from byubit import Bit
from Library.bit_commands import *


@Bit.empty_world(5, 3)
def go(bit):
    # Part 1
    bit.left()
    bit.move()
    bit.right()
    bit_paint_and_move(bit, 4, 'red')
    bit.move()
    bit.paint('blue')
    # Reset part 1
    bit.right()
    bit.right()
    bit_paint_and_move(bit, 5, None)
    bit.left()
    bit.move()
    bit.left()
    # Part 2
    bit_paint_and_move(bit, 1, 'red')
    bit_paint_and_move(bit, 1, 'green')
    bit_paint_and_move(bit, 3, 'blue')


if __name__ == '__main__':
    go(Bit.new_bit)