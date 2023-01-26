from byubit import Bit

def bit_move(bit, blocks):
    for _ in range(blocks):
        bit.move()

@Bit.empty_world(5, 8)
def one_firework(bit):
    bit.left()
    bit_move(bit, 5)
    bit.right()
    bit.move()
    bit.paint('green')
    bit.move()
    bit.right()
    bit.move()
    bit.paint('red')
    bit.move()
    bit.paint('green')
    bit.left()
    bit.move()
    bit.left()
    bit_move(bit, 2)
    bit.paint('green')
    bit.right()
    bit.move()
    bit.right()
    bit_move(bit, 5)
    bit.left()

if __name__ == '__main__':
    one_firework(Bit.new_bit)