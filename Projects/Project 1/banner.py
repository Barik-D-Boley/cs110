from byubit import Bit


@Bit.worlds("banner", "another_banner")
def banner(bit):
    left = 0
    bit.left()

    while (bit.is_empty() or bit.is_red()) and bit.front_clear():
        while not bit.is_green() and bit.front_clear():
            bit.paint('red')
            bit.move()
        bit.paint('red')
        while bit.front_clear():
            bit.move()
        if not left % 2 and bit.right_clear():
            left += 1

            bit.right()
            bit.move()
            bit.right()
            while not bit.is_green():
                bit.move()
            bit.paint('red')
        elif left % 2 and bit.left_clear():
            left += 1

            bit.left()
            bit.move()
            bit.left()
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


if __name__ == '__main__':
    banner(Bit.new_bit)