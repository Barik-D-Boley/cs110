from byubit import Bit


@Bit.worlds('go-to-lake', 'go-to-another-lake')
def go(bit):
    while bit.front_clear():
        if bit.is_red():
            bit.left()
            bit.move()
        if bit.is_empty():
            bit.paint('green')
            bit.move()


if __name__ == "__main__":
    go(Bit.new_bit)