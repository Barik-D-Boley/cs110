from byubit import Bit
from Library.bit_commands import *


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


@Bit.worlds("trees")
def draw_trees(bit):
    for i in range(3):
        one_tree(bit)
        if i < 2:
            bit.move()


if __name__ == '__main__':
    draw_trees(Bit.new_bit)