from byubit import Bit


@Bit.worlds('flowers1', 'flowers2')
def run(bit):
    while bit.front_clear():
        if not bit.is_empty():
            flower_color = bit.get_color()
            bit.paint(None)
            while bit.is_empty():
                bit.move()
            bit.left()
            while not bit.is_empty():
                bit.move()
            bit.paint(flower_color)
            bit.right()
            bit.right()
            while bit.front_clear():
                bit.move()
            bit.left()
        bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)