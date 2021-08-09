import prompt
from random import randint


def greeting():
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    return name


def brain_prog():
    a = randint(1, 20)
    d = randint(1, 10)
    k = 1
    random_k = randint(1, 9)
    print('Question:', end=' ')
    while k <= 10:
        if k == random_k:
            print('..', end=' ')
            missed_a = a
            a = a + d
        if k == 10:
            print(a)
        else:
            print(a, end=' ')
            a = a + d
        k = k + 1
    return missed_a


def brain_game():
    name = greeting()
    i = 0
    while i < 3:
        correct_answer = brain_prog()
        user_answer = prompt.integer('Your answer? ')
        if user_answer == correct_answer:
            print('Correct!')
            i = i + 1
        else:
            print("{} is wrong answer ;(.".format(user_answer), end=' ')
            print("Correct answer was {}.".format(correct_answer))
            print("Let's try again, {}!".format(name))
            break
    if i == 3:
        print('Congratulations, {}!'.format(name))


def main():
    print("Welcome to the Brain Games!")
    brain_game()


if __name__ == '__main__':
    main()
