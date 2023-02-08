from byubit import Bit


def bit_move(bit, blocks):
    for _ in range(blocks):
        bit.move()


def bit_paint_and_move(bit, blocks, color):
    for i in range(blocks):
        bit.paint(color)
        if i < blocks-1 or blocks == 1:
            bit.move()


@Bit.worlds('boxes', 'boxes2')
def run(bit):
    while bit.front_clear():
        if not bit.is_empty():
            color = bit.get_color()
            for _ in range(4):
                bit_paint_and_move(bit, 4, color)
                bit.left()
            bit_move(bit, 4)
        if bit.front_clear():
            bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)