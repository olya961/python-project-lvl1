#!/usr/bin/env python
import prompt
from random import randint


def brain_even():
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    i = 0
    while i < 3:
        random_number = randint(1, 100)
        if random_number % 2 == 0:
            is_number_even = 'yes'
        else:
            is_number_even = 'no'
        print('Question: ', random_number)
        user_answer = prompt.string('Your answer? ')
        if user_answer == is_number_even:
            print('Correct!')
            i = i + 1
        else:
            print(user_answer, " is wrong answer ;(. Correct answer was ", is_number_even, ".")
            print("Let's try again, {}!".format(name))
            i = 0
    print('Congratulations, {}!'.format(name))


def main():
    print("Welcome to the Brain Games!")
    brain_even()


if __name__ == '__main__':
    main()
