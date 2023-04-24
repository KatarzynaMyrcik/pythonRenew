#how to delete duplicates from the list
numbers = [1,2,5,2,7,1,5,3,7,3]
numbers2 = []
#fonction fromkeys
#numbers2 = list(dict.fromkeys(numbers))
for number in numbers:
    if number not in numbers2:
        numbers2.append(number)
print(numbers2)
