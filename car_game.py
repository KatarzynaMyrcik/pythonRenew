#game Car
print('Welcome in my car game!')
print("you can start. If you don't know the options please type [h]elp.")
print("What do you want to do? ")
action = ''
while action != 'q':
    action = input('> ').lower()
    if action == 'h':
        print("""You choose [h]elp
        In this game You have a possibility to:
        [start] a car
        [stop] a car
        [q]uit the game
        What do you want to do? """)
    elif action == 'start':
        print('the car is starting')
    elif action == 'stop':
        print('the car is stopped')
    else:
        print("I don't understand. SOrry. If you don't remember the options please try to set [h]elp")
else:
    print("OK. Thank you! Have a nice day!")
