def mult(*args):
    ac = 1
    for n in args:
      ac *= n
    print(ac)
    def imparandpar():
        if ac % 2 == 0:
            return f'I AM PAR'
        return f'I AM IMPAR'

    result = imparandpar()
    print(result)
        
mult(1,2)

# entendo mais sobre return
# RETURN SERIA PARA PEGAR UM VALOR E ATRIBUIR NUMA VARIAVEL