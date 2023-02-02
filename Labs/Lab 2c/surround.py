from byubit import Bit


@Bit.worlds('surround', 'surround2')
def run(bit):
    while bit.front_clear():
        if not bit.right_clear() and bit.is_empty():
            for _ in range(4):
                while not bit.right_clear():
                    bit.paint('green')
                    bit.move()
                bit.right()
                bit.move()
        bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)