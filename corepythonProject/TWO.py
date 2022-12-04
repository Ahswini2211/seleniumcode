import ONE

print("Top level in TWO.py")

ONE.func()

if __name__== '__main__':
    print("TWO.py is being run directly")

else:
    print("TWO.py has been imported")