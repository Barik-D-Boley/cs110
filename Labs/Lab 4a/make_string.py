def make_a_string(the_list):
    the_list = [word.upper() for word in the_list]
    return '-'.join(the_list)


def main():
    the_list = ['yer','a','wizard','harry']
    print(make_a_string(the_list))
    the_list = ['what','does','the','fox','say']
    print(make_a_string(the_list))
    the_list = ['every','day','is','a','great','day','to','program']
    print(make_a_string(the_list))



if __name__ == '__main__':
    main()
