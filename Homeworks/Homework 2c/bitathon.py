from byubit import Bit


@Bit.worlds('bitathon', 'bitathon2')
def run(bit):
    # Mountain
    while not bit.is_blue():
        bit.paint('green')
        if bit.right_clear():
            bit.right()
        elif not bit.front_clear():
            bit.left()
        bit.move()
    bit.left()

    # Water
    while bit.front_clear():
        bit.move()
    bit.left()
    bit.move()
    bit.right()

    # Bike
    while bit.front_clear():
        bit.move()
        bit.paint('red')


if __name__ == '__main__':
    run(Bit.new_bit)