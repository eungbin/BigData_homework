def enter(client="galaxy", count=3):
    return "Client:{0}, Count:{1}".format(client, count)

print(enter())

print(enter("iphone", 4))

def union(*args):
    print(args)

union(1, 2, 3)

def union2(**args):
    print(args)

union2(id='ppp', key='park')

f = lambda  x:x*x
print(f(5))

print( (lambda c:c+10)(30) )