from byubit import Bit


@Bit.worlds('scurry', 'scurry2')
def go(bit):
    while bit.left_clear() or bit.front_clear() or bit.right_clear():
        # Checks for an open turn if blocked
        if not bit.front_clear() and bit.left_clear():
            bit.left()
        elif not bit.front_clear() and bit.right_clear():
            bit.right()
        # Paints the block and moves
        if bit.is_green():
            bit.paint('blue')
        else:
            bit.paint('green')
        bit.move()
    # Paints final block
    if bit.is_green():
        bit.paint('blue')
    else:
        bit.paint('green')


if __name__ == '__main__':
    go(Bit.new_bit)