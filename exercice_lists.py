#exercice lists
'''
names = ['John', 'Cindy', 'Elise', 'Hannah', 'Olgierd']
print(names[-3:4])
names[1] = 'Sindey'
print(names)
'''
#exercice : find the largest number in a list
numbers = [32, 1, 4343, 212, 43, 12, 4, 665]
max = numbers[0]
for x_number in numbers:
    if x_number > max:
        max = x_number
print(f'the result is {max}')
