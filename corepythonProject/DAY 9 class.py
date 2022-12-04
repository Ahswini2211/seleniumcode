class calc():

  num = 200

  def getdata(self,a,b):
    self.fristnumber = a
    self.secondnumber = b

    print("hi i am inside a function")

  def summation(self):
    return self.fristnumber + self.secondnumber + calc.num

obj = calc()
obj.getdata(20,40)
print(obj.summation())



