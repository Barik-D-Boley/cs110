from byubit import Bit


@Bit.worlds('escape', 'escape2')
def run(bit):
    gem_color = bit.get_color()
    bit.paint('blue')
    while not bit.is_green():
        while bit.front_clear():
            bit.paint('blue')
            bit.move()
        if bit.left_clear():
            bit.left()
        elif bit.right_clear():
            bit.right()
    while bit.is_green():
        bit.move()
    bit.right()
    bit.move()
    bit.paint(gem_color)
    bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)