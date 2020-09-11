for i in range(5):
    print(i, end="\t")

numberList = [3, 6, 9, 12, 15, 18]

def odd(x):
    return x%2==1

relist = filter(odd, numberList)

print()

for i in relist:
    print(i, end="\t")
print()

for i in zip(numberList, [100, 200, 300, 400, 500, 600]):
    print(i, end="\t")
print()

def product(x):
    return x*2

print()
for i in map(product, numberList):
    print("Item:{0}".format(i))