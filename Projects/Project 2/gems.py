from byubit import Bit


@Bit.worlds('gems', 'gems2')
def run(bit):
    while bit.front_clear():
        if not bit.is_empty():
            pool_color = bit.get_color()
            bit.paint(None)

            while not bit.right_clear():
                bit.move()

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
                    bit.paint(pool_color)
                    bit.move()
                bit.paint(pool_color)

                if not left  and bit.right_clear():
                    left += 1

                    bit.right()
                    bit.move()
                    bit.right()
                elif left and bit.left_clear():
                    left -= 1

                    bit.left()
                    bit.move()
                    bit.left()

            # Get to pool edge
            if not left:
                bit.right()
                bit.right()
            while bit.right_clear():
                bit.move()
        bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)