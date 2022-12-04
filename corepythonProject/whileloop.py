temp = 77
while temp >= 68 and temp <=77:
    print("room temp is mantained at {}degree fahrenheit".format(temp))
    temp = temp  -1
while True:
    print("This loop runs forever")

while False:
    print("This loop runs forever")

number = 1
for row in range(1,4):
    for colum in range(1,4):
        print(number,end='')
        number = number + 1
        print()
    
