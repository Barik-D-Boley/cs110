def pizza_time():
    print('Welcome to Papa John\'s!')
    name = input('What is your name? ')
    pizza_type = input('What kind of pizza do you want? ')
    toppings = input('What toppings do you want? ')
    print(f'{name} wants a {pizza_type} pizza with {toppings}!')


if __name__ == '__main__':
    pizza_time()
