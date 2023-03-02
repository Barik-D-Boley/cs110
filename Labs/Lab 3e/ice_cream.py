def main():
    ratings = [('chocolate', 10), ('banana nut', 8.5), ('vanilla', 6),
              ('chocolate', 9), ('banana nut', 9.3), ('vanilla', 7.5),
              ('chocolate', 8), ('banana nut', 10), ('vanilla', 4.1),
              ('chocolate', 10), ('banana nut', 10), ('vanilla', 10),
              ('chocolate', 9.3), ('banana nut', 7.5), ('vanilla', 8)
              ]
    flavors = ['chocolate', 'banana nut', 'vanilla']

    for flavor in flavors:
        flavor_ratings = []
        for i in range(len(ratings)):
            if flavor == ratings[i][0]:
                flavor_ratings.append(ratings[i])

        total_ratings = 0
        for i in range(len(flavor_ratings)):
            total_ratings += flavor_ratings[i][1]

        print(f'The average rating for {flavor} is {round(total_ratings / len(flavor_ratings), 1)}')




if __name__ == '__main__':
    main()