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
        random_k = randint(1, 9)
        print('Question:', end=' ')
        while k <= 10:
            if k == random_k:
                print('..', end=' ')
                missed_a = a
            elif k == 10:
                print(a)
            else:
                print(a, end=' ')
            a = a + d
            k = k + 1
        user_answer = prompt.integer('Your answer? ')
        if user_answer == missed_a:
            print('Correct!')
            i = i + 1
        else:
            print("{} is wrong answer ;(. Correct answer was {}.".format(user_answer, missed_a))
            print("Let's try again, {}!".format(name))
            break
    if i == 3:
        print('Congratulations, {}!'.format(name))


def main():
    print("Welcome to the Brain Games!")
    brain_progression()


if __name__ == '__main__':
    main()
