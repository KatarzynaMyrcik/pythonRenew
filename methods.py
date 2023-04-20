course = 'Python for beginners'
#I will test the methods(specific foncions) now
#change all the caracters to uppercase
print(course.upper())
#change all the caracters to lowercase
print(course.lower())
print(f'Initinal string was: {course}')
#IF I want to know f.ex. where is a caracter P in this expression I have to use methode find(). It return index of this letter
print(course.find('o'))
#test of replace() method
print(course.replace('P', 'Sr'))
#test of IN operator. It retun boolean value
print('Python' in course)
