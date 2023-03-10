from byubit import Bit


def bit_move(bit, blocks):
    for _ in range(blocks):
        bit.move()


def bit_paint_and_move(bit, blocks, color):
    for i in range(blocks):
        bit.paint(color)
        if i < blocks-1 or blocks == 1:
            bit.move()


@Bit.empty_world(8, 8)
def picasso(bit):
    bit.left()
    bit_paint_and_move(bit, 8, 'black')
    bit.right()
    bit_paint_and_move(bit, 8, 'black')
    bit.right()
    bit_paint_and_move(bit, 8, 'black')
    bit.right()
    bit_paint_and_move(bit, 4, 'black')
    bit.move()
    bit_paint_and_move(bit, 3, 'red')
    bit.right()
    bit.move()
    bit_paint_and_move(bit, 3, 'red')
    bit_move(bit, 2)
    bit_paint_and_move(bit, 2, 'black')
    bit.right()
    bit.move()
    bit_paint_and_move(bit, 1, 'black')
    bit_paint_and_move(bit, 2, 'red')
    bit.move()
    bit_paint_and_move(bit, 2, 'black')
    bit.right()
    bit.move()
    bit_paint_and_move(bit, 1, 'green')
    bit_paint_and_move(bit, 2, 'black')
    bit.move()
    bit_paint_and_move(bit, 1, 'green')
    bit.paint('black')
    bit.right()
    bit.move()
    bit_paint_and_move(bit, 4, 'red')
    bit.right()
    bit.move()
    bit_paint_and_move(bit, 1, 'red')
    bit_move(bit, 2)
    bit.right()
    bit_move(bit, 3)
    bit.paint('red')
    bit.right()
    bit_move(bit, 2)
    bit_paint_and_move(bit, 1, 'red')
    bit.paint('green')
    bit.right()
    bit.move()
    bit_paint_and_move(bit, 2, 'red')
    bit.right()
    bit_move(bit, 2)
    bit.right()
    bit.move()
    bit.paint('green')


if __name__ == '__main__':
    picasso(Bit.new_bit)