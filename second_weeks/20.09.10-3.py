import pickle
with open('C:/Temp/test.txt', 'w') as f:
    f.write('This is Test.\n')
    f.write('The End')

fs = open('C:/Temp/test.txt', 'r')
test = fs.readlines()
fs.close()

for line in test:
    print(line)

colors = ['red', 'orange', 'blue']
with open('C:/Temp/colors', 'wb') as f2:
    pickle.dump(colors, f2)

del colors
with open('C:/Temp/colors', 'rb') as f3:
    print("colors : {0}".format(pickle.load(f3)))