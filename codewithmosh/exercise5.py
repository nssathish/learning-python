secret_number = 9
guess_count = 0
guess_limit = 3
guessed = False

while guess_count < guess_limit:
    if int(input('Guess: ')) == secret_number:
        print('You won!!')
        break
    guess_count += 1
else:
    print('You lost!!')