import prompt
from random import randint


def cycle():
    k = 2
    a = randint(2, 15)
    print('Question:', a)
    main_str = ''
    while k < a:
        if a % k == 0:
            main_str = main_str + str(k)
        else:
            main_str = main_str
        k = k + 1
    if main_str == '':
        check = 'yes'
    else:
        check = 'no'
    return check


def brain_prime():
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        correct_answer = cycle()
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            i = i + 1
        else:
            print('{} is wrong answer ;(.'.format(user_answer), end=' ')
            print('Correct answer was {}.'.format(correct_answer))
            print("Let's try again, {}!".format(name))
            break
    if i == 3:
        print('Congratulations, {}!'.format(name))


def main():
    print("Welcome to the Brain Games")
    brain_prime()


if __name__ == '__main__':
    main()
