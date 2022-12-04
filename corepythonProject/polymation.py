class employee:
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 40

    def displaythenumberworkinghours(self):
        print(self.numberofworkinghours)

class Trainee(employee):

    def setnumberofworkinghours(self):
        self.numberofworkinghours = 45

    def resetnumberofworkinghours(self):
        super().setnumberofworkinghours()


emp = employee()
emp.setnumberofworkinghours()

print("number of working hours of employee;",end= '')
emp.displaythenumberworkinghours()





trainee = Trainee()
trainee.setnumberofworkinghours()
print("number of working hours for trainee:",end = '')
trainee.displaythenumberworkinghours()
trainee.resetnumberofworkinghours()
print("number of working hours has been reset",end= '')
trainee.displaythenumberworkinghours()