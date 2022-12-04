x = lambda a,b,c : a+b+c
print(x(5,45,45))

x = lambda p,q,s: p*q*s
print(x(10,5,25))

def myfun(n):
    return lambda a:a*n
output = myfun(5)
print(output(11))

def myfun(s):
    return lambda a : a + s
output = myfun(10)
print(output(5))

def test(a):
    return lambda n : a*n
b = test(4)
d = test(3)
print(b(11))
print(d(10))

def test(s):
    return  lambda a,: a*s
p = test(10)
q = test(20)

print(p(8))
print(q(5))


def demo():
   x = lambda a:a + 10
   print(x(200))
demo()

def demo():
    x = lambda s:s - 10
    print(x(100))
demo()
