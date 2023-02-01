from byubit import Bit


@Bit.worlds('soccer', 'soccer2')
def go(bit):
    global left
    left = 0

    bit.move()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()
    bit.left()
    while 1:
        while bit.front_clear():
            bit.paint('green')
            bit.move()
        bit.paint('green')
        if not left:
            global left
            left = 1

            bit.right()
            bit.move()
            bit.right()
        elif left:
            global left
            left = 0

            bit.left()
            bit.move()
            bit.left()


if __name__ == '__main__':
    go(Bit.new_bit)