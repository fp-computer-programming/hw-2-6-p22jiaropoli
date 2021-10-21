# Author JRI 9/26/21

text1 = input("what is the radius?")
radius = int(text1)

text2 = input("what is the height?")
height = int(text2)

volume = (radius ** 2) * height *3.1415
print(volume)

surface_area = (2 * 3.1415 * (radius ** 2)) + (2 * 3.1415 * radius * height)
print(surface_area)