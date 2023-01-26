from byubit import Bit
from Library.bit_commands import *


@Bit.worlds('dive-for-treasure', 'dive-for-deep-treasure')
def dive(bit):
    # Variables
    bit_info = str(bit).split('\n')
    board = bit_info[: -3]
    bit_start_coordinates = bit_info[: -2][len(bit_info[: -2])-1].split(' ')
    # Commands
    bit_move(bit, len(list(filter(lambda x: x == 'k', [*board[2]]))))
    bit.right()
    bit_move(bit, int(bit_start_coordinates[1])-1)
    bit.paint('blue')


if __name__ == "__main__":
    dive(Bit.new_bit)