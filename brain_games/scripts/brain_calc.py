#!/usr/bin/env python
import prompt
from random import randint, choice


def brain_calc():
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    print("What is the result of the expression?")
    i = 0
    while i < 3:
        a = randint(1, 10)
        b = randint(1, 10)
        random_op = choice([a + b, a - b, a * b])
        if random_op == a + b:
            string_op = str(a) + ' + ' + str(b)
        elif random_op == a - b:
            string_op = str(a) + ' - ' + str(b)
        else:
            string_op = str(a) + ' * ' + str(b)
        print('Question:', string_op)
        user_answer = prompt.integer('Your answer: ')
        if user_answer == random_op:
            print('Correct!')
            i = i + 1
        else:
            print('{} is wrong answer ;(.'.format(user_answer), end=' ')
            print('Correct answer was {}.'.format(random_op))
            print("Let's try again, {}!".format(name))
            break
    if i == 3:
        print('Congratulations, {}!'.format(name))


def main():
    print('Welcome to the Brain Games!')
    brain_calc()


if __name__ == '__main__':
    main()
