from byubit import Bit


# Something isn't working right. Fix it!
@Bit.worlds('blue-square')
def go(bit):
    # Draw a square
    while bit.front_clear():
        bit.paint("blue")
        bit.move()
        bit.paint("blue")
        bit.move()
        bit.right()


if __name__ == '__main__':
    go(Bit.new_bit)
