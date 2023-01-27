from byubit import Bit
from Library.bit_commands import *


@Bit.worlds('fix-reds')
def go(bit):
    while not bit.is_green():
        bit.move()

    while bit.front_clear():
        bit.move()
        if bit.is_red():
            bit.paint('blue')


if __name__ == '__main__':
    go(Bit.new_bit)