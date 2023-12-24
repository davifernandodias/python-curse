people = {
    'name': 'davi',
    'last_name': 'dias',
    'age': 19,
}

print(len(people)) # contar
print(" ")

print(list(people.keys())) # chaves
print(" ")

print(list(people.values())) # valores
print(" ")

print(list(people.items())) # itens
print(" ")

for chave, valor in people.items(): # percorrer chave e valor:
    print(chave,valor)
print(" ")

people.setdefault('idade', 0 ) # setar um valor
print(people['idade'])

