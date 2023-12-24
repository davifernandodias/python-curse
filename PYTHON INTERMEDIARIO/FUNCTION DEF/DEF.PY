#def python():
#    print('varias')

#python()


#def soma(x,y):
#    print(x + y)

#soma(1,2)

def soma(*args):
    print(type(args))
    ac = 0
    for i in args:
        ac += i
    print(ac)

soma(1,2)

print(sum((1,2)))