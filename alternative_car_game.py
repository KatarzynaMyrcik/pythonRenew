#game Car
#car is stopped when the state =0, car is started when the state is 1
print('Welcome in my car game!')
print("you can start. If you don't know the options please type [h]elp.")
print("What do you want to do? ")
action = ''
state = 0

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
        if state == 0:
            print('the car is starting')
            state = 1
        else:
            print('the car is already started')
    elif action == 'stop':
        if state == 0:
            print("car is already stopped")
        else:
            print('the car is stopped')
            state = 0
    elif action == 'q':
        print('OK. Thank you! Have a nice day!')
        break
    else:
        print("I don't understand. SOrry. If you don't remember the options please try to set [h]elp")
