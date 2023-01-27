from byubit import Bit


@Bit.worlds('red-line')
def draw_line(bit):
    red_count = 0
    bit.move()
    while bit.left_clear() and bit.right_clear():
        if bit.is_red():
            red_count += 1
            bit.right()
            bit.move()
        if red_count == 1:
            bit.paint('red')
            bit.move()
        else:
            bit.move()


if __name__ == "__main__":
    draw_line(Bit.new_bit)