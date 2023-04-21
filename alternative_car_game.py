#game Car
print('Welcome in my car game!')
print("you can start. If you don't know the options please type [h]elp.")
print("What do you want to do? ")
action = ''
while True:
    action = input('> ').lower()
    if action == 'h':
        print("""You chose [h]elp
In this game You have a possibility to:
[start] a car
[stop] a car
[q]uit the game
What do you want to do? """)
    elif action == 'start':
        print('the car is starting')
    elif action == 'stop':
        print('the car is stopped')
    elif action == 'q':
        print('OK. Thank you! Have a nice day!')
        break
    else:
        print("I don't understand. SOrry. If you don't remember the options please try to set [h]elp")
