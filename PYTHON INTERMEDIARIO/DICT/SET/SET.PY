#s1 = {1,2,3,4,4}
#l1 = [1,2,3,4,4,4,1]
#print(s1)

#for n in s1:
 #   print(n)

# METODH ÚTEIS

s1 = set()
s1.add('luiz') #ADD
s1.add(80) # ADD
s1.update(('hello world',1,2,3,4)) # ADICIONAR 
s1.discard(80) # DISCART ARGUMENTS
s1.clear() # CLEAR SET
print(s1)


# OPERADORES ÚTEIS

# | UNION / UNI OS SETS
# & INTERSECTION / PRESENTE EM AMBOS
# - DIVERGENTE / PRESENTE APENAS NO DA ESQUERDA
# ^ NÃO ESTÁ PRESENTE EM NENHUM SET
settest1 = {1,2,3}
settest2 = {2,10,20}
set_union = settest1.union(settest2) # unir |
print(set_union)
print(" ")

set_ambos = settest1.intersection(settest2) # valor presente em  ambos
print(set_ambos)
print(" ")

set_divergente = settest1-(settest2) # item presente apenas no da esquerda
print(set_divergente)
print(" ")

set_nao_tem_em_ambos = settest1^(settest2) # não ta presente em ambos
print(set_nao_tem_em_ambos)
print(" ")