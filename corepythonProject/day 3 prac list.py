home = ["mobile","tv","laptop","wifi","tab"]
print(home)
print(home[3])
print(home[-1])

home.append("smartwatch")
print(home)

home.insert(3,"powerbank")
print(home)
home.insert(0,"charger")
print(home)
home.insert(-3,"mouse")
print(home)

home.remove("powerbank")
print(home)
home.remove("mouse")
print(home)

home.reverse()
print(home)


