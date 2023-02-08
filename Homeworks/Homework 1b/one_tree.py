from byubit import Bit


def bit_move(bit, blocks):
    for _ in range(blocks):
        bit.move()


def bit_paint_and_move(bit, blocks, color):
    for i in range(blocks):
        bit.paint(color)
        if i < blocks-1 or blocks == 1:
            bit.move()


@Bit.worlds("one_tree")
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


if __name__ == '__main__':
    one_tree(Bit.new_bit)