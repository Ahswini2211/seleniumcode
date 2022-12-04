class calc():
    num = 100

    def getdata(self, a, b):

        self.firstnumber = a

        self.secondnumber = b

        print("hi i am inside a function")

    def summation(self):
        return self.firstnumber + self.secondnumber + calc.num


obj = calc()
obj.getdata(20, 10)
print(obj.summation())
