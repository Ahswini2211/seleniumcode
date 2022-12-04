class calc():

    num = 400

    def getdata(self, a , b):

        self.firstnumber = a

        self.secondnumber = b

        print("hi i am inside a function")

    def summation(self):
         return self.firstnumber + self.secondnumber + calc.num + self.thirdnumber + self.fourthnumber

    def __init__(self,c,d):
        self.thirdnumber = c
        self.fourthnumber = d
        print("i am running first")


obj = calc(10,40)
obj.getdata(30,10)
print(obj.summation())
