def bit_move(bit, blocks):
    for _ in range(blocks):
        bit.move()


def bit_paint_and_move(bit, blocks, color):
    for i in range(blocks):
        bit.paint(color)
        if i < blocks-1 or blocks == 1:
            bit.move()


def get_bit_coordinates(bit):
    bit_info = str(bit).split('\n')
    return bit_info[: -2][len(bit_info[: -2]) - 1].split(' ')