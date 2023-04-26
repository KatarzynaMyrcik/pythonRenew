def find_max(my_number):
    numbers = [1,5,7,3,10,2]
    numbers.append(my_number)
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    print(maximum)
    if maximum ==my_number:
        print(f"Congrats: {my_number} is the biggest number in this set!")


def find_max_from_your_list(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
