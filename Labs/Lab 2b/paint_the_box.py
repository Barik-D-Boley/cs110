from byubit import Bit


@Bit.worlds('paint-the-box', 'paint-another-box')
def run(bit):
    for _ in range(4):
        while bit.front_clear():
            bit.paint('green')
            bit.move()
        bit.left()


if __name__ == '__main__':
    run(Bit.new_bit)