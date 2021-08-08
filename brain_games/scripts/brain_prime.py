import prompt
from random import randint

def brain_prime():
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        a = randint(2, 15)
        main_str = ''
        k = 2
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
        if a == 1:
            check = 'no'
        print('Question: ', a)
        user_answer = prompt.string('Your answer: ')
        if user_answer == check:
            print('Correct!')
            i = i + 1
        else:
            print('{} is wrong answer ;(. Correct answer was {}.'.format(user_answer, check))
            print("Let's try again, {}!".format(name))
            i = 0
    print('Congratulations, {}!'.format(name))


def main():
    print("Welcome to the Brain Games")
    brain_prime()


if __name__ == '__main__':
    main()
