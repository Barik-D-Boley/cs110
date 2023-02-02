from byubit import Bit


@Bit.worlds('clear-green', 'clear-green2')
def run(bit):
    while bit.front_clear():
        if bit.is_green() and (not bit.left_clear() or not bit.right_clear()):
            bit.paint(None)
        bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)