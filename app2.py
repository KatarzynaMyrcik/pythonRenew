import utiles

choice = input('''Do you wanna: 
[1] verify if your number is the greatest or 
[2] check which number from a list [1,4,2,7,3,1] is the greatest? 
> ''')
if choice == '1':
    my_number = int(input("give me a number, I'll check if it is greater tham numbers on my list: "))
    utiles.find_max(my_number)
else:
    numbers = [1,4,2,7,3,1]
    maxi = utiles.find_max_from_your_list(numbers)
    print(f" Max is {maxi}")
    #it is possible to use max fonction from python:
    print(max(numbers))
