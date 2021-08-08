import prompt
from random import randint


def brain_gcd():
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    print('Find the greatest commom divisor of given numbers.')
    i = 0
    while i < 3:
        a = randint(1, 20)
        b = randint(1, 20)
        if a <= b:
            min_number = a
        else:
            min_number = b
        divisor = 1
        while divisor <= min_number:
            if a % divisor == 0 and b % divisor == 0:
                divisor_max = divisor
                divisor = divisor + 1
            else:
                divisor = divisor + 1
        print('Question:', a, b)
        user_answer = prompt.integer('Your answer: ')
        if user_answer == divisor_max:
            print('Correct!')
            i = i + 1
        else:
            print('{} is wrong answer ;(. Correct answer was {}.'.format(user_answer, divisor_max))
            print("Let's try again, {}!".format(name))
            i = 0
    print('Congratulations, {}!'.format(name))


def main():
    print('Welcome to the Brain Games!')
    brain_gcd()


if __name__ == '__main__':
    main()
