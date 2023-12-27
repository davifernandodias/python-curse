def generator(n=0):
    yield 1 # yield pausa a fuction
    print('continuando')
    yield 2
gen = generator(n=0)
print(next(gen))
print(next(gen))

