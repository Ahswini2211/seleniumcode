from oops import child

class child1(child):
    num3= 100

    def __init__(self):
        child.__init__(self )

    def getcompdata(self):
        return self.num2 + self.num + self.summation()


obj = child1()
obj.getdata(10,20)
print(obj.getcompdata())