def criar_saudacao(saudacao):
    def saudar(name):
        return f'{saudacao}, {name}'
    return saudar


h1 = criar_saudacao('bom dia')
print(h1('luiz'))