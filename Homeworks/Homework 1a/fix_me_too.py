from byubit import Bit


@Bit.worlds('fix-me-too')
def do_more_fixing(bit):
    bit.move
    bit.paint('blue')
    bit.move()
    bit.paint('blue')
    bit.move()
    bit.left()
    bit.move()
    bit.paint(green)
    bit.left
    bit.move()
    bit.move()
    bit.right()
    bit.move()
    bit.pain('red')


if __name__ == '__main__':
    do_more_fixing(Bit.new_bit)
