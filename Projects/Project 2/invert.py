from byubit import Bit


def invert_color(bit):
    if bit.is_empty():
        bit.paint('blue')
    elif bit.is_blue():
        bit.paint(None)

@Bit.worlds('invert', 'invert2')
def run(bit):
    turn_left = 1

    # Paints the lines and goes to the next line
    while bit.front_clear() or (turn_left and bit.left_clear()) or (not turn_left and bit.right_clear()):
        invert_color(bit)

        if turn_left and bit.left_clear() and not bit.front_clear():
            turn_left -= 1
            bit.left()
            bit.move()
            bit.left()
            invert_color(bit)
        elif not turn_left and bit.right_clear() and not bit.front_clear():
            turn_left += 1
            bit.right()
            bit.move()
            bit.right()
            invert_color(bit)
        bit.move()

    # Resets the triangle at the beginning
    invert_color(bit)
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


if __name__ == '__main__':
    run(Bit.new_bit)