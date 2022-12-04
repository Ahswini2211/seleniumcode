def func():
    print("func() in five.py")

print("top level in five.py")

if __name__=='__main__':
    print("five.py is being run directly")
else:
    print("five.py has been imported")
