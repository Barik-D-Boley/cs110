from byubit import Bit


@Bit.worlds('y')
def paint_the_ys(bit):
    for _ in range(2):
        bit.paint('blue')
        for _ in range(2):
            bit.move()
            bit.right()
            bit.move()
            bit.left()
            bit.paint('blue')
        bit.right()
        bit.move()
        bit.paint('blue')
        bit.move()
        bit.paint('blue')
        bit.left()
        bit.move()
        bit.left()
        for _ in range(3):
            bit.move()
        bit.paint('blue')
        bit.move()
        bit.right()
        bit.move()
        bit.paint('blue')
        for _ in range(3):
            if bit.front_clear():
                bit.move()


if __name__ == '__main__':
    paint_the_ys(Bit.new_bit)