from byubit import Bit


@Bit.worlds('invert', 'invert2', 'invert-careful')
def go(bit):
    while bit.front_clear():
        bit.move()
        if bit.is_empty():
            bit.paint('blue')
        elif bit.is_blue():
            bit.erase()


if __name__ == '__main__':
    go(Bit.new_bit)