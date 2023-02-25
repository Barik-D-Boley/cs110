class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def main():
    all_players = []
    bigs_roster = []
    bigs_youngest = None
    bigs_oldest = None
    littles_roster = []
    littles_youngest = None
    littles_oldest = None

    while True:
        name = input('Enter player name: ')
        if name == '':
            break
        age = int(input('Enter player age: '))
        all_players.append(Player(name, age))

    for i in range(len(all_players)):
        if all_players[i].age > 10:
            bigs_roster.append(all_players[i])
            if not bigs_youngest or all_players[i].age < bigs_youngest.age:
                bigs_youngest = all_players[i]
            if not bigs_oldest or all_players[i].age > bigs_oldest.age:
                bigs_oldest = all_players[i]
        else:
            littles_roster.append(all_players[i])
            if not littles_youngest or all_players[i].age < littles_youngest.age:
                littles_youngest = all_players[i]
            if not littles_oldest or all_players[i].age > littles_oldest.age:
                littles_oldest = all_players[i]

    print(f'Team Bigs')
    print(f'Total members: {len(bigs_roster)}')
    print(f'Average age: {int(round((sum(player.age for player in bigs_roster))/len(bigs_roster), 0))}')
    print(f'Youngest age: {bigs_youngest.age}')
    print(f'Oldest age: {bigs_oldest.age}')
    print('Members')
    for i in range(len(bigs_roster)):
        print(f' - {bigs_roster[i].name} {bigs_roster[i].age}')

    print(f'Team Littles')
    print(f'Total members: {len(littles_roster)}')
    print(f'Average age: {int(round((sum(player.age for player in littles_roster)) / len(littles_roster), 0))}')
    print(f'Youngest age: {littles_youngest.age}')
    print(f'Oldest age: {littles_oldest.age}')
    print('Members')
    for i in range(len(littles_roster)):
        print(f' - {littles_roster[i].name} {littles_roster[i].age}')


if __name__ == '__main__':
    main()