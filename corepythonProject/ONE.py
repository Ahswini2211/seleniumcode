def func():
    print("func() in ONE.py")

print("Top level in ONE.py")

if __name__=='__main__':
     print('ONE.py is being run diretly')
else:
    print("ONE.py has been imported")