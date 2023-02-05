from byubit import Bit


def color_bar(bit):
    if bit.is_blue():
        bit.left()
        while bit.front_clear():
            bit.move()
            bit.paint('blue')
        bit.right()
        bit.right()
        while bit.front_clear():
            bit.move()
        bit.left()
    elif bit.is_red():
        bit.left()
        while bit.front_clear():
            bit.move()
            bit.paint('red')
        bit.right()
        bit.right()
        while bit.front_clear():
            bit.move()
        bit.left()
    elif bit.is_green():
        bit.left()
        while bit.front_clear():
            bit.move()
            bit.paint('green')
        bit.right()
        bit.right()
        while bit.front_clear():
            bit.move()
        bit.left()


@Bit.worlds('color-bars', 'color-bars2')
def run(bit):
    while bit.front_clear():
        color_bar(bit)
        bit.move()
    color_bar(bit)


if __name__ == '__main__':
    run(Bit.new_bit)