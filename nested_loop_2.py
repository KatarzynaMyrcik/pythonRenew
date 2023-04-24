#nested loop exercice
numbers = [5,2,5,2,2]
#szerokosc = (len(numbers)) -1
x = 0
#first option
for x in range(numbers[x]):
   print(numbers[x] * 'x')

#loop in loop version
for x in numbers:
    output= ''
    for y in range(x):
        output += 'x'
    print(output)
