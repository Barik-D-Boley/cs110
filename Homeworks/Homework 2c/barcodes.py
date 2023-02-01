from byubit import Bit


@Bit.worlds('barcode', 'barcode2')
def run(bit):
    while bit.front_clear():
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
        bit.move()
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


if __name__ == '__main__':
    run(Bit.new_bit)