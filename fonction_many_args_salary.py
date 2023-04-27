#funkcja ktora odbiera rozna ilosc argumentow, use of *args
def calculate_salary(*args, base: float) -> float:
    salary = base
    #beda wyswietlone jako tupla
    #print(args)
    for arg in args:
        salary = salary + salary*arg

    return salary


print(calculate_salary(0.1, 0.25, 0.3, base=1000))
print(calculate_salary(0.1, base=1000))
