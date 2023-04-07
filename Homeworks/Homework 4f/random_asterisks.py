import random


def random_asterisks(text, frequency):
    text_list = text.split(' ')

    for i, word in enumerate(text_list):
        if random.random() < float(frequency):
            text_list[i] = '*' * len(text_list[i])

    text_list = ''.join(text_list)

    print(text_list)
    return text_list


if __name__ == '__main__':
    text = " ".join(["a" * i for i in range(1000)])
    print(text)
    result = random_asterisks(text, 1)
    print(result.count('*') / len(result) > 0.99)