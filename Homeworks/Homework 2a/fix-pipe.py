from byubit import Bit


@Bit.worlds('fix-pipe')
def go(bit):
    while bit.front_clear():
        if bit.right_clear():
            bit.right()
            bit.move()
            bit.paint('blue')
            bit.left()
            bit.left()
            bit.move()
            bit.right()
        elif bit.left_clear():
            bit.left()
            bit.move()
            bit.paint('blue')
            bit.right()
            bit.right()
            bit.move()
            bit.left()

        if bit.front_clear():
            bit.move()
    # Checks last square for empty squares once
    if bit.right_clear():
        bit.right()
        bit.move()
        bit.paint('blue')
        bit.left()
        bit.left()
        bit.move()
        bit.right()
    elif bit.left_clear():
        bit.left()
        bit.move()
        bit.paint('blue')
        bit.right()
        bit.right()
        bit.move()
        bit.left()


if __name__ == '__main__':
    go(Bit.new_bit)