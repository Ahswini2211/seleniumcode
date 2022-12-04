import five

print("top leve in six.py")

five.func()

if __name__=='__main__':
    print("six.py is being run directly")

else:
    print("six.py has been imported")