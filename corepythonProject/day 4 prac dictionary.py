laptop = {"dell":50000,"hp":40000,"asus":35000,"lenovo":30000}
print(laptop)

laptop["dell"] = 45000
print(laptop)

print(laptop.keys())
print(laptop.values())

windows = laptop.copy()
print(windows)

#del laptop["hp"]
#print(laptop)

#laptop.clear()
#print(laptop)

home = {"moble" : 100,"chager" : 80,"fiter": 200,"tv" : 400}
print(home)

home["chager"] = 300
print(home)

print(home.keys())
print(home.values())

house = home.copy()
print(house)

del home["tv"]
print(home)

#print(home[3])

home.clear()
print(home)