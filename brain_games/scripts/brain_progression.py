import prompt
from random import randint


def brain_progression():
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    print("What number is missing in the progression?")
    i = 0
    while i < 3:
        a = randint(1, 20)
        d = randint(1, 10)
        k = 1
        random_k = randint(1, 10)
        main_string = ' '
        while k <= 10:
            if k == random_k:
                main_string = main_string + ' ..'
                missed_a = a
            else:
                main_string = main_string + ' ' + str(a)
            a = a + d
            k = k + 1
        print('Question: ', main_string)
        user_answer = prompt.integer('Your answer? ')
        if user_answer == missed_a:
            print('Correct!')
            i = i + 1
        else:
            print("{} is wrong answer ;(. Correct answer was {}.".format(user_answer, missed_a))
            print("Let's try again, {}!".format(name))
            i = 0
    print('Congratulation, {}!'.format(name))


def main():
    print("Welcome to the Brain Games!")
    brain_progression()


if __name__ == '__main__':
    main()
