from byubit import Bit
from Library.bit_commands import *


@Bit.worlds('paint-and-exit')
def run(bit):
    bit_paint_and_move(bit, 5, 'blue')
    bit.left()
    bit_paint_and_move(bit, 3, 'blue')
    bit.left()
    bit_paint_and_move(bit, 5, 'blue')
    bit.left()
    bit_paint_and_move(bit, 3, 'blue')
    bit.right()
    bit_move(bit, 4)
    bit.right()
    bit_move(bit, 3)


if __name__ == '__main__':
    run(Bit.new_bit)
