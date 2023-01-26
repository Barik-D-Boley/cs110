from byubit import Bit

def draw_one_dot(bit):
    bit.move()
    bit.move()
    bit.paint('blue')

@Bit.empty_world(8, 3)
def dots(bit):
    bit.left()
    bit.move()
    bit.right()
    bit.paint('blue')
    for _ in range(3):
        draw_one_dot(bit)
    bit.right()
    bit.move()
    bit.left()

if __name__ == '__main__':
    dots(Bit.new_bit)