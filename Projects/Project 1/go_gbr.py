from byubit import Bit


@Bit.worlds("go-go-go", "og-og-og")
def go_gbr(bit):
    while not bit.is_green():
        bit.paint('green')
        bit.move()
    bit.right()
    bit.move()
    while not bit.is_blue():
        bit.paint('blue')
        bit.move()
    bit.left()
    bit.move()
    while not bit.is_red():
        bit.paint('red')
        bit.move()


if __name__ == '__main__':
    go_gbr(Bit.new_bit)