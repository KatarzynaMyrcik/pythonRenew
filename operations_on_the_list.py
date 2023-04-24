#addition of number at the end
numbers = [5, 2, 1, 7, 1, 4]
numbers.append(20)
print(numbers)
#addition of number not at the end of list
numbers.insert(0, 10)
print(numbers)
#count the frequence of values on the list:
print(numbers.count(5))
#show index of a value
print(numbers.index(1))
#check if the value is on the list:
print(50 in numbers)
#remove of one item '1' from the list:
numbers.remove(1)
print(numbers)
numbers.remove(1)
print(numbers)
#remove the latest number form the list:
numbers.pop()
print(numbers)
#sort of numbers:
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
#creation of a copy of list:
numbers2 = numbers.copy()
print(numbers2)
#delete of everything in a table
numbers.clear()
print(numbers)
