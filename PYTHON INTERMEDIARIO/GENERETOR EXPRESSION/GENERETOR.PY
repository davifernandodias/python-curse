import sys
generator = (n for n in range(10000))
# diferença do iteravel para o generator // basicamente o generetor mais leve
print(sys.getsizeof(generator))

lista = [n for n in range(10000)]
print(sys.getsizeof(lista))

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))