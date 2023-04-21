#test of while
secret = 9
gues_count = 0
guess_limit= 3

while gues_count < guess_limit:
    guess = int(input('Guess the number[0 - 10]: '))
    gues_count += 1
    if guess ==secret:
        print("You won!")
        break
else:
    print('Sorry, you failed!')
