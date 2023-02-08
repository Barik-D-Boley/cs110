from byubit import Bit


def bit_move(bit, blocks):
    for _ in range(blocks):
        bit.move()


def bit_paint_and_move(bit, blocks, color):
    for i in range(blocks):
        bit.paint(color)
        if i < blocks-1 or blocks == 1:
            bit.move()


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
