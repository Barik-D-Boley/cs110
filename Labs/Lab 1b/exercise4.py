from byubit import Bit

def bit_move(bit, blocks):
    for _ in range(blocks):
        bit.move()

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

@Bit.empty_world(17, 8)
def fireworks(bit):
    for i in range(3):
        one_firework(bit)
        print(i)
        if i < 2:
            bit_move(bit, 2)

if __name__ == '__main__':
    fireworks(Bit.new_bit)