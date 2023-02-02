from byubit import Bit


@Bit.worlds("grassy_field", "big_grassy_field")
def run(bit):
    left = 0
    bit.left()

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


if __name__ == '__main__':
    run(Bit.new_bit)