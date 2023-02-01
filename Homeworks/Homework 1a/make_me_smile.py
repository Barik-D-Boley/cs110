from byubit import Bit
from Library.bit_commands import *


@Bit.worlds('missing-smile')
def make_me_smile(bit):
    bit_move(bit, 2)
    bit.right()
    bit.move()
    bit_paint_and_move(bit, 1, 'blue')
    bit.right()
    bit.move()
    bit.left()
    bit_paint_and_move(bit, 3, 'blue')
    bit.move()
    bit.left()
    bit.move()
    bit.paint('blue')


if __name__ == '__main__':
    make_me_smile(Bit.new_bit)
