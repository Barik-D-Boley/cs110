from byubit import Bit
from Library.bit_commands import *


@Bit.worlds("one_tree")
def one_tree(bit):
    bit.left()
    bit_move(bit, 2)
    bit.right()
    bit.move()
    bit_paint_and_move(bit, 3, 'green')
    bit.left()
    bit.move()
    bit.left()
    bit.move()
    bit.left()
    bit_paint_and_move(bit, 2, 'green')
    bit.move()
    bit_paint_and_move(bit, 2, 'red')
    bit.left()
    bit.move()


if __name__ == '__main__':
    one_tree(Bit.new_bit)
