from byubit import Bit
from Library.bit_commands import *


@Bit.worlds("boxes")
def stack_boxes(bit):
    for _ in range(3):
        bit_paint_and_move(bit, 2, 'red')
        bit.left()
        bit.move()
        bit.left()
        bit_paint_and_move(bit, 2, 'blue')
        bit.right()
        bit.move()
        bit.right()
        bit_paint_and_move(bit, 2, 'blue')
        bit.left()
        bit.move()
        bit.left()
        bit.move()
        bit.right()
        bit.right()


if __name__ == '__main__':
    stack_boxes(Bit.new_bit)
