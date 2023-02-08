from byubit import Bit


def bit_move(bit, blocks):
    for _ in range(blocks):
        bit.move()


def bit_paint_and_move(bit, blocks, color):
    for i in range(blocks):
        bit.paint(color)
        if i < blocks-1 or blocks == 1:
            bit.move()


@Bit.worlds("quilt")
def make_a_quilt(bit):
    for _ in range(3):
        bit.left()
        bit_paint_and_move(bit, 3, 'red')
        bit.right()
        bit.move()
        bit.right()
        bit_paint_and_move(bit, 3, 'green')
        bit.left()
        bit.move()
        bit.left()
        bit_paint_and_move(bit, 1, 'green')
        bit_paint_and_move(bit, 1, 'blue')
        bit.paint('green')
        bit.right()
        bit.move()
        bit.right()
        bit_paint_and_move(bit, 3, 'green')
        bit.left()
        bit.move()
    bit.left()
    bit_paint_and_move(bit, 3, 'red')
    bit.right()
    bit.right()
    bit_move(bit, 2)
    bit.left()


if __name__ == '__main__':
    make_a_quilt(Bit.new_bit)