from byubit import Bit


@Bit.worlds('go-to-lake', 'go-to-another-lake')
def go(bit):
    pass


if __name__ == "__main__":
    go(Bit.new_bit)
