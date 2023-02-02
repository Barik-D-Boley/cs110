from byubit import Bit


@Bit.worlds('soccer', 'soccer2')
def go(bit):
    while bit.front_clear():
        left = 0

        # Goes to bottom left corner
        bit.move()
        bit.right()
        while bit.front_clear():
            bit.move()
        bit.left()
        bit.left()

        # Paints the field
        while bit.is_empty():
            while bit.front_clear():
                bit.paint('green')
                bit.move()
            bit.paint('green')
            if not left % 2 and bit.right_clear():
                left += 1

                bit.right()
                bit.move()
                bit.right()
            elif left % 2 and bit.left_clear():
                left += 1

                bit.left()
                bit.move()
                bit.left()

        # Resets at next gate
        bit.right()
        bit.right()
        while (not bit.right_clear() and left % 2) or (not bit.left_clear() and not left % 2):
            bit.move()
        if left % 2:
            bit.right()
            bit.move()
        elif not left % 2:
            bit.left()
            bit.move()


if __name__ == '__main__':
    go(Bit.new_bit)