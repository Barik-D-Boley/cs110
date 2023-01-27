from byubit import Bit


def move_to_tree(bit):
    """ Moves to the trunk """
    pass


def draw_trunk(bit):
    """ Draws the trunk (two red squares)  """
    pass


def draw_branches(bit):
    """ Draws the branches """
    pass


def go_back_down(bit):
    """ Moves back down to the ground, below the right-most branch, facing right. """
    pass


@Bit.worlds("one_tree")
def one_tree(bit):
    move_to_tree(bit)
    draw_trunk(bit)
    draw_branches(bit)
    go_back_down(bit)


if __name__ == '__main__':
    one_tree(Bit.new_bit)
