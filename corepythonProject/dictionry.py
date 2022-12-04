camera = {"sony":500,"nikon":600,"canon":700}
print(camera)

camera["sony"] = 750
print(camera)

print(camera.keys())

print(camera.values())

demo = camera.copy()
print(demo)

#del camera["sony"]
#print(camera)

#camera.clear()
#print(camera)

print(camera[0])

