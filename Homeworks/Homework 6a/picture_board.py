def main():
    emoji_grid = []
    for i in range(5):
        emoji_grid.append('')

    print(f'{emoji_grid}\n')
    while True:
        slot = input('Slot: ')
        if slot == '':
            break
        slot = int(slot)
        emoji = input('Pic: ')
        emoji_grid[slot] = emoji
        print(f'{emoji_grid}\n')


if __name__ == '__main__':
    main()