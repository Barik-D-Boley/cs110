from byubit import Bit


@Bit.worlds('blue-s', 'big-blue-s')
def run(bit):
    while bit.front_clear():
        if bit.is_green():
            # Top part of S
            bit.left()
            while bit.front_clear():
                bit.paint('blue')
                bit.move()
            bit.right()
            while bit.front_clear():
                bit.paint('blue')
                bit.move()
            bit.right()
            bit.right()
            bit.paint('blue')
            while bit.front_clear():
                bit.move()
            bit.left()
            while bit.front_clear():
                bit.move()
            bit.left()

            # Bottom part of S
            bit.move()
            bit.paint('blue')
            bit.right()
            while bit.front_clear():
                bit.paint('blue')
                bit.move()
            bit.right()
            while bit.front_clear():
                bit.paint('blue')
                bit.move()
            bit.right()
            bit.right()
            bit.paint('blue')
            while bit.front_clear():
                bit.move()
            bit.left()
            while bit.front_clear():
                bit.move()
            bit.right()
        bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)