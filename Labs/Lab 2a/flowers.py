from byubit import Bit


@Bit.worlds('flowers')
def go(bit):
    while bit.front_clear():
        bit.move()
        if bit.is_green():
            bit.left()
            bit.move()
            bit.paint('red')
            bit.right()
            bit.right()
            bit.move()
            bit.left()


if __name__ == '__main__':
    go(Bit.new_bit)
