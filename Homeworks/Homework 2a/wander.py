from byubit import Bit


@Bit.worlds('wander', 'wander2')
def go(bit):
    while bit.front_clear() or bit.is_blue() or bit.is_green():
        if bit.is_green():
            bit.left()
            bit.move()
        elif bit.is_blue():
            bit.right()
            bit.move()
        else:
            bit.paint('red')
            bit.move()
    bit.paint('red')


if __name__ == '__main__':
    go(Bit.new_bit)
