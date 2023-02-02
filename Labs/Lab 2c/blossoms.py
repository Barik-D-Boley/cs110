from byubit import Bit


@Bit.worlds('blossoms', 'blossoms2')
def go(bit):
    while bit.front_clear():
        bit.move()
        if bit.right_clear():
            depth = 0
            left = 1

            bit.right()
            while bit.front_clear():
                depth += 1
                bit.move()
            bit.left()

            # Fill pool
            for i in range(depth):
                while bit.front_clear():
                    bit.paint('blue')
                    bit.move()
                bit.paint('blue')

                if not left % 2 and bit.right_clear():
                    left += 1

                    bit.right()
                    bit.move()
                    bit.right()
                elif left % 2 and bit.left_clear():
                    left += 1

                    bit.left()
                    bit.move()
                    bit.left()

            # Get to pool edge
            if not left % 2:
                bit.right()
                bit.right()
            while bit.right_clear():
                bit.move()

            # Make Tree
            bit.left()
            bit.paint('green')
            bit.move()
            bit.paint('green')
            bit.move()
            bit.paint('red')
            bit.left()
            bit.move()
            bit.paint('red')
            bit.right()
            bit.move()
            bit.right()
            bit.move()
            bit.paint('red')
            bit.move()
            bit.right()
            bit.move()
            bit.paint('red')
            bit.right()
            bit.move()
            bit.left()
            bit.move()
            bit.move()
            bit.left()


if __name__ == '__main__':
    go(Bit.new_bit)