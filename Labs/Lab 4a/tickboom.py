import re


# Once it reaches a digit
def f1(text):
    result = ''
    for character in text:
        if re.compile('\d').match(character):
            result += 'BOOM'
            break
        else:
            result += 'tick'
    return result


# Once it reaches a lower case letter
def f2(text):
    result = ''
    for character in text:
        if re.compile('[a-z]').match(character):
            result += 'BOOM'
            break
        else:
            result += 'tick'
    return result


# Any letter
def f3(text):
    result = ''
    for character in text:
        if re.compile('[a-zA-Z]').match(character):
            result += 'BOOM'
            break
        else:
            result += 'tick'
    return result


# Any whitespace
def f4(text):
    result = ''
    for character in text:
        if re.compile('\s').match(character):
            result += 'BOOM'
            break
        else:
            result += 'tick'
    return result


def main():
    text = 'a!_pA35S222y'
    value = f1(text)
    if value != 'tickticktickticktickBOOM':
        print(f"Error on f1 with {text}")
        return

    text = 'gh 9af380Pb'
    value = f1(text)
    if value != 'tickticktickBOOM':
        print(f"Error on f1 with {text}")
        return

    text = '8F Pan2M'
    value = f2(text)
    if value != 'ticktickticktickBOOM':
        print(f"Error on f2 with {text}")
        return

    text = 'Pa88s!990'
    value = f2(text)
    if value != 'tickBOOM':
        print(f"Error on f2 with {text}")
        return

    value = f3('8 $A\t3hs')
    if value != 'tickticktickBOOM':
        print("Error on #3")
        return

    value = f3('8 $\t3pTYe')
    if value != 'tickticktickticktickBOOM':
        print("Error on #4")
        return

    value = f4('m6!%P 7p ')
    if value != 'tickticktickticktickBOOM':
        print("Error on #5")
        return

    value = f4('2F!%P\tG    ')
    if value != 'tickticktickticktickBOOM':
        print("Error on #6")
        return

    print("Good job!")




if __name__ == '__main__':
    main()