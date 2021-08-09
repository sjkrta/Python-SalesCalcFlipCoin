import random


def ask_user():
    global user_choice
    user_choice = 'a'
    choices = ('head', 'tail')
    while user_choice not in choices:
        user_choice = input('Head or Tail?\n').lower()


def flip():
    global Outcome
    random_number = random.randrange(1, 3)
    if random_number == 1:
        Outcome = 'head'
    else:
        Outcome = 'tail'


def ask_user_again():
    global user_mood
    user_mood = 'a'
    choices = ('y', 'n')
    while user_mood not in choices:
        user_mood = input('Wanna Try Again? (type y for yes and n for no)\n')
        if user_mood == 'y':
            game()


def win_loss():
    if user_choice == Outcome:
        print(f'Congrats it was {Outcome}, you are the winner!')
    elif user_choice != Outcome:
        print(f'Sorry, it was {Outcome}. Try Again.')


def game():
    ask_user()
    flip()
    win_loss()
    ask_user_again()


game()
