class calc():
    num = 100

    def getdata(self, a, b):

        self.firstnumber = a

        self.secondnumber = b

        print("hi i am inside a function")

    def summation(self):
        return self.firstnumber + self.secondnumber + calc.num + self.thirdnumber + self.fourthnumber

    def __init__(self,c,d):
        self.thirdnumber = c
        self.fourthnumber = d
        print("i am running first")

obj = calc(10,20)
obj.getdata(20,20)
print(obj.summation())