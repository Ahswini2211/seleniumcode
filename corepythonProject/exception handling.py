try:
    length = 10
    length/ width

except ZeroDivisionError:
    print("Division by zero is not possible")
except NameError:
    print("variable has been used before defining it")
except NameError:
    print("A new error has been found")
finally:
    print("will execute atleast once")

