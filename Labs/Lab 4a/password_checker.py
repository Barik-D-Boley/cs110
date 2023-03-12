import re


def check_password(password):
    if re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$').match(password):
        return True
    else:
        return False



def main():
    print(check_password('password'))
    print(check_password('a87fRPesT'))
    print(check_password('a8P'))
    print(check_password('abFHaprucndPE8'))
    print(check_password('arPReSH!!$@'))
    print(check_password('Password1'))


if __name__ == '__main__':
    main()