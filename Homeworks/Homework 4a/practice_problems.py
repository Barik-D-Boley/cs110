import re


# Count the number of whitespace characters in the string.
def count_whitespace(string):
    whitespace_filter = re.compile('\s')
    return len(list(filter(whitespace_filter.match, [*string])))


# Return a list of words with more than 3 unique uppercase letters.
def keep_big_words(words):
    capital_filter = re.compile('[A-Z]')
    big_words = []

    for i in range(len(words)):
        big_words.append(words[i]) if len(list(set(filter(capital_filter.match, [*words][i])))) > 2 else ''

    return big_words


# Return the word with the most punctuation.
def most_punctuation(words):
    punctuation_filter = re.compile('[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]')
    most_punctuated_sentence = None

    for i in range(len(words)):
        if not most_punctuated_sentence or len(list(filter(punctuation_filter.match, [*words][i]))) > len(list(filter(punctuation_filter.match, [*most_punctuated_sentence]))):
            most_punctuated_sentence = words[i]

    return most_punctuated_sentence


# Remove all punctuation from the string.
def remove_punctuation(string):
    not_punctuation_filter = re.compile('[^!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]')
    return ''.join(str(i) for i in list(filter(not_punctuation_filter.match, [*string])))


# Replace all digits in the string with asterisks.
def replace_digits_with_asterisks(string):
    digit_filter = re.compile('\d')
    new_string = []

    for i in range(len([*string])):
        new_string.append('*') if re.search(digit_filter, [*string][i]) else new_string.append([*string][i])

    return ''.join(str(i) for i in new_string)