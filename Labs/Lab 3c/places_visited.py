def main():
    places_visited = []

    while True:
        place = input('Enter a place: ')
        if place == '':
            break
        else:
            places_visited.append(place)

    print(f'I have visited:')

    for i in range(len(places_visited)):
        print(f' - {places_visited[i]}')


if __name__ == '__main__':
    main()
