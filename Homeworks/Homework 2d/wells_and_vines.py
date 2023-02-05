from byubit import Bit


@Bit.worlds('wells-and-vines')
def run(bit):
    while bit.front_clear():
        # Vines
        if bit.is_green():
            bit.left()
            while bit.front_clear():
                bit.paint('green')
                bit.move()
            bit.paint('green')
            bit.right()
            bit.right()
            while bit.front_clear():
                bit.move()
            bit.left()
        # Wells
        if bit.right_clear():
            bit.right()
            bit.move()
            depth = 1
            while bit.front_clear():
                bit.paint('blue')
                bit.move()
                depth += 1
            bit.paint('blue')
            bit.right()
            bit.right()
            for _ in range(depth):
                bit.move()
            bit.right()
        bit.move()



if __name__ == '__main__':
    run(Bit.new_bit)