from byubit import Bit


@Bit.worlds('lines')
def run(bit):
    turn_left = 1
    paint_red = 0
    paint_green = 0
    paint_blue = 0

    # Paints the lines and goes to the next line
    while bit.front_clear() or (turn_left and bit.left_clear()) or (not turn_left and bit.right_clear()):
        if bit.is_red():
            paint_red += 1
        elif bit.is_green():
            paint_green += 1
        elif bit.is_blue():
            paint_blue += 1

        while paint_red:
            bit.paint('red')
            bit.move()
            if bit.is_red():
                paint_red -= 1
        while paint_green:
            bit.paint('green')
            bit.move()
            if bit.is_green():
                paint_green -= 1
        while paint_blue:
            bit.paint('blue')
            bit.move()
            if bit.is_blue():
                paint_blue -= 1

        if turn_left and bit.left_clear() and not bit.front_clear():
            turn_left -= 1
            bit.left()
            bit.move()
            bit.left()
        elif not turn_left and bit.right_clear() and not bit.front_clear():
            turn_left += 1
            bit.right()
            bit.move()
            bit.right()
        bit.move()

    # Resets the triangle at the beginning
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()
    bit.left()


if __name__ == '__main__':
    run(Bit.new_bit)

