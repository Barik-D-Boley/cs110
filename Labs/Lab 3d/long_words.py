def main():
    words = ['completely', 'fun', 'program', 'to', 'write', 'hahaha']
    long_words = []

    for i in range(len(words)):
        if len(words[i]) > 5:
            long_words.append(words[i])

    for i in range(len(long_words)):
        print(f' - {long_words[i]}')


if __name__ == '__main__':
    main()
