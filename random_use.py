import random

for i in range(3):
    #random.random is a fonction from random method which generate a number between 0 - 1
    print(random.random())

for i in range(2):
    #generate a int number between 10 and 20
    print (random.randint(10, 20))

#choice one thing from a list
members = ['Ecik', 'Francek', 'Hanys', 'Gena']
leader = random.choice(members)
print(leader)
