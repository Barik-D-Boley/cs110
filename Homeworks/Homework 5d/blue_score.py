import re


class BlueScore:
    def __init__(self, phrase, score):
        self.phrase = phrase
        self.score = score


def main():
    phrases = []
    blue_scores = set()

    while True:
        phrase = input('Phrase: ')
        if phrase == '':
            break
        phrases.append(BlueScore(phrase, 0))

    for blue_score in phrases:
        blue_score.score = len(re.findall(r'\b(?:byu|cougars?|blue)\b\S*', blue_score.phrase, flags=re.I|re.M))
        blue_scores.add(blue_score.score)

    for score in blue_scores:
        print(f'{score}:')
        for phrase in [x.phrase for x in phrases if x.score == score]:
            print(phrase)
        print('')


if __name__ == '__main__':
    main()