from byubit import Bit


@Bit.worlds('red-roses', 'red-roses2')
def run(bit):
    while bit.front_clear():
        if bit.is_green():
            bit.paint('red')
        if bit.is_blue():
            bit.paint('red')
        bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)