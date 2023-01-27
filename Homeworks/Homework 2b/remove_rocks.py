from byubit import Bit


@Bit.worlds('remove-rocks', 'remove-rocks2')
def run(bit):
    green_count = 0
    while bit.front_clear():
        if bit.is_green():
            green_count += 1
        if green_count == 1 and bit.is_blue():
            bit.paint(None)
        bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)