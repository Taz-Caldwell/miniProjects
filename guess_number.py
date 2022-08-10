import random 

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print('Sorry, guess again too low.')
        elif guess > random_number:
            print('Sorry, too high.')
    print(f'Congradulations, {random_number} was the correct answer!')
             
guess(1000)