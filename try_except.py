try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("invalid value")
except ZeroDivisionError:
    print("Age connot be 0. You can't divide by 0")
