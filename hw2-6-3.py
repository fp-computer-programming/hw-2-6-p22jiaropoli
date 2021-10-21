# Author JRI 9/26/21

text1 = input("How many free throws were scored?")
freethrows = int(text1)

text2 = input("How many baskets were scored?")
regularbaskets = int(text2)

text3 = input("How many three pointers were scored?")
threepointers = int(text3)

total = freethrows + (2 * regularbaskets) + (3 * threepointers)
print(total)