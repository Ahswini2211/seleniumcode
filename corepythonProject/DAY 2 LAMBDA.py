x = lambda a,b,c: a+b+c
print(x(5,45,45))

def myfunc(n):
    return  lambda a: a * n
output = myfunc(5)
print(output(11))

def test(a):
    return lambda n: a * n
B = test(4)
D = test(3)
print(B(11))
print(D(10))

def demo():
    x = lambda a: a + 10
    print(x(200))
demo()


