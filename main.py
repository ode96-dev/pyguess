from random import randint

lower_num, higher_num = 1, 10
random_number:int = randint(lower_num, higher_num)
print(f"Guess a number between {lower_num} to {higher_num}")

while True:
    try:
        user_guess: int = int(input("Guess: "))
    except ValueError as e:
        print('Please enter a valid number')
    if user_guess > random_number:
        print('You enter a higher number')
    elif user_guess < random_number:
        print('You entered a lower number')
    else:
        print('Correct Guess!')
        break

